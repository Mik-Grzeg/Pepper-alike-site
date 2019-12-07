from django.urls import path
from . import views
app_name = 'pepper'
urlpatterns = [
    #path('', views.BaseView.as_view(), name='base'),
    #path('<slug:slug>', views.DetailVies.as_view(), name='detail'),
    path('create/', views.ItemCreateView.as_view(), name='item-create')
]
