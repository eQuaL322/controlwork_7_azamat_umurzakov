from django.urls import path

from guest_book_app.views.base import home_page
from guest_book_app.views.guests import add_guest_view, update_guest_view

urlpatterns = [
    path('', home_page, name='index'),
    path('guest/add/', add_guest_view, name='add_guest'),
    path('guest/<int:pk>/update/', update_guest_view, name='update_guest_view'),

]
