from .models import Car, Brand, Comment
from django import forms


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email","text"]

