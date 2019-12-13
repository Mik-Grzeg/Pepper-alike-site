from django import forms

from .models import Item, Subcategory, Category


class ItemModelForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Title of the steal",
                                    "rows": 1,
                                    "cols": 50,
                                }))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "Few words about it"}))

    retail_price = forms.FloatField()

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
