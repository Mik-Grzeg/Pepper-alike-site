from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import Category, Item
from .forms import ItemModelForm

# Create your views here.

class ItemCreateView(CreateView):
    """
    View to create an item
    """
    template_name = 'pepper/create_item.html'
    form_class = ItemModelForm
    queryset = Item.objects.all()


    def get_success_url(self):
        return '/pepper/'



class ItemsListView(ListView):
    """
    View with 10 latest steals,
    Chose of category,
    Nav bar with groups
    """
    pass

class ItemDetailView(DetailView):
    """
    View with details of steal,
    Can be up/down voted, deleted
    """
    pass
