from django import forms

from .models import Item, Subcategory, Category


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'category',
            'subcategory',
            'title',
            'description',
            'url',
            'slug',
            'pub_date',
            'original_price',
            'retail_price',
            'still_up_to_date',
            'img')
        exclude = ('slug',
                   'pub_date',
                   'still_up_to_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()
        #print(self.data)

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')
        #print(self.fields['subcategory'].queryset)

