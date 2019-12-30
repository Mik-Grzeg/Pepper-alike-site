from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Category, Item, Subcategory
from .forms import ItemModelForm

from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin
from bootstrap_modal_forms.generic import BSModalLoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm

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


class SearchResultsView(ListView):
    template_name = 'pepper_app/items_list.html'
    context_object_name = 'items'
    model = Item

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(Q(title__icontains=query) |
                                          Q(description__icontains=query) |
                                          Q(category__name__icontains=query) |
                                          Q(subcategory__name__icontains=query)).order_by('-pub_date')
        return object_list


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


class SignUpView(PassRequestMixin, SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'pepper_app/signup.html'
    success_message = 'Success: Sign up succeeded. You can now log in.'
    success_url = reverse_lazy('items-list')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "pepper_app/login.html"
    success_message = "Success: You were successfully logged in."
    extra_context = dict(success_url=reverse_lazy('items-list'))


def load_subcategories(request):
    """
    Function used in dropdown chained list while creating new item.
    :param request:
    :return: Subcategories of chosen category
    """
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'pepper_app/dropdown_list.html', {'subcategories': subcategories})
