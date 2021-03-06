from django.urls import path
from . import views


urlpatterns = [
    path('', views.ItemsListView.as_view(), name='items-list'),
    path('category/<slug:slugged_category>/', views.ItemsListView.as_view(), name='category-filtered-items-list'),
    path('subcategory/<slug:slugged_subcategory>/', views.ItemsListView.as_view(), name='subcategory-filtered-items'
                                                                                        '-list'),
    path('<int:id>/<slug:slugged_title>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('create/', views.ItemCreateView.as_view(), name='item-create'),
    path('categories/', views.ItemsListView.as_view(), name='categories'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]