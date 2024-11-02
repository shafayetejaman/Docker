from django.shortcuts import render, redirect
from .models import Car, Comment, Brand
from .forms import CarForm, CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from profiles.models import History


# Create your views here.


def home(request, brand_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    brand = None

    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        cars = Car.objects.filter(brand=brand)

    return render(
        request,
        "show_cars/show_post_list.html",
        {
            "logged": request.user.is_authenticated,
            "cars": cars,
            "brands": brands,
            "current_brand": brand,
        },
    )


class CreatePostView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "show_cars/add_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().is_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class DetailPostView(DetailView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/detail_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all().order_by("created").reverse()
        comment_form = CommentForm()

        context["logged"] = self.request.user.is_authenticated
        context["comments"] = comments
        context["comment_form"] = comment_form

        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()

        return self.get(request, *args, **kwargs)


class DeletePostView(DeleteView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/delete_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class UpdatePostView(UpdateView):
    model = Car
    form_class = CarForm
    pk_url_kwarg = "id"
    template_name = "show_cars/Update_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


def buy_car(request, id):
    car = Car.objects.get(pk=id)
    car.quantity -= 1
    car.save()

    History.objects.create(car=car, user=request.user)
    
    return redirect("home")
