from django.urls import path
from . import views
urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('items/<int:item_id>/', views.getById, name='getById'),
    path('items/<int:item_id>/delete/', views.deleteItem, name='deleteItem'),
    path('items/<int:item_id>/update/', views.updateItem, name='updateItem')
]