from django import forms

from .models import Item, Subcategory, Category

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password']


class ItemModelForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Title of the steal",
                                    "rows": 1,
                                    "cols": 50,
                                }))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "Few words about it"}))

    class Meta:
        model = Item
        fields = (
            'category',
            'subcategory',
            'title',
            'description',
            'url',
            'pub_date',
            'original_price',
            'retail_price',
            'currency',
            'still_up_to_date',
            'img')
        exclude = (
            'slugged_title',
            'pub_date',
            'still_up_to_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = \
                    Subcategory.objects.filter(category_id=category_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')

    def clean(self):
        cleaned_data = super(ItemModelForm, self).clean()
        retail_price_field = cleaned_data.get("retail_price")
        original_price_field = cleaned_data.get("original_price")
        currency_field = cleaned_data.get("currency")

        if not retail_price_field and (currency_field or original_price_field):
            raise forms.ValidationError('Please fill retail price field.')
        elif retail_price_field and not currency_field:
            raise forms.ValidationError('Please fill currency field.')

        return cleaned_data
