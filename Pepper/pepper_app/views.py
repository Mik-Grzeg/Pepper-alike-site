from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Category, Item, Subcategory
from .forms import ItemModelForm

# Create your views here.

class ItemCreateView(CreateView):
    """
    View to create an item
    """
    template_name = 'pepper_app/create_item.html'
    form_class = ItemModelForm
    success_url = reverse_lazy('pepper_app')
    queryset = Item.objects.all()

    def get_success_url(self):
        return '/pepper_app/'


def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
   # print(subcategories)
    return render(request, 'pepper_app/list.html', {'subcategories': subcategories})



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
