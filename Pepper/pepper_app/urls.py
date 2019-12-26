from django.urls import path
from . import views



#app_name = 'pepper_app'
urlpatterns = [
    path('', views.ItemsListView.as_view(), name='items-list'),
    path('category/<slug:slugged_category>/', views.ItemsListView.as_view(), name='category-filtered-items-list'),
    path('subcategory/<slug:slugged_subcategory>/', views.ItemsListView.as_view(), name='subcategory-filtered-items'
                                                                                        '-list'),
    path('<int:id>/<slug:slugged_title>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('create/', views.ItemCreateView.as_view(), name='item-create'),
    path('categories', views.ItemsListView.as_view(), name='categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]