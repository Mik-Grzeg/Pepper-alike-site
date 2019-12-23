from django.urls import path
from . import views



#app_name = 'pepper_app'
urlpatterns = [
    path('', views.ItemsListView.as_view(), name='items-list'),
    path('<int:id>/<slug:slugged_title>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('create/', views.ItemCreateView.as_view(), name='item-create'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]