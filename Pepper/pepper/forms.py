from django import forms

from .models import Item


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=[
            'category',
            'title',
            'description',
            'url',
            'slug',
            'pub_date',
            'original_price',
            'retail_price',
            'still_up_to_date',
            'img']
        exclude=['slug',
                 'pub_date',
                 'still_up_to_date']
