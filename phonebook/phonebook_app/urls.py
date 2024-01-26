from django.urls import path
from .views import contact_list, add_contact, edit_contact, delete_contact, search_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),
    path('search/', search_contact, name='search_contact'),
]
