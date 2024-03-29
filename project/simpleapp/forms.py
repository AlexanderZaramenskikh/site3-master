from django import forms
from django.core.exceptions import ValidationError

from .models import Product, News, Articles


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("content")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data



class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("content")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data