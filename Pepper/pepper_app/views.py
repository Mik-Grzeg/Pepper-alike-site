from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Category, Item, Subcategory
from .forms import ItemModelForm


# ------------------------------------------------------------------


class ItemsListView(ListView):
    """
    View with 10 latest steals,
    Choice of category,
    Nav bar with groups
    """

    template_name = 'pepper_app/items_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        _category_slug = self.kwargs.get("slugged_category")
        _subcategory_slug = self.kwargs.get("slugged_subcategory")

        # Checking if user filtered items by category or subcategory.
        if _subcategory_slug:
            # Getting queryset of items that belong to the subcategory.
            subcategory = Subcategory.objects.get(slugged_subcategory=_subcategory_slug)
            return Item.objects.filter(subcategory=subcategory).order_by("-pub_date")
        elif _category_slug:
            # Getting queryset of items that belong to the category.
            category = Category.objects.get(slugged_category=_category_slug)
            return Item.objects.filter(category=category).order_by('-pub_date')
        else:
            # User hasn't chosen any filter so every item is being displayed.
            return Item.objects.order_by('-pub_date')


class ItemDetailView(DetailView):
    """
    View with details of steal,
    Can be up/down voted, deleted
    """
    model = Item
    template_name = 'pepper_app/item_details.html'
    context_object_name = 'item'

    def get_object(self):
        slug_ = self.kwargs.get("slugged_title")
        return get_object_or_404(Item, slugged_title=slug_)


class ItemCreateView(CreateView):
    """
    View to create an item
    """
    template_name = 'pepper_app/create_item.html'
    form_class = ItemModelForm
    success_url = reverse_lazy('items-list')

    def get_success_url(self):
        return self.success_url

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


def load_subcategories(request):
    """
    Function used in dropdown chained list while creating new item.
    :param request:
    :return: Subcategories of chosen category
    """
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'pepper_app/dropdown_list.html', {'subcategories': subcategories})
