from django.urls import path

from guest_book_app.views.base import home_page

urlpatterns = [
    path('', home_page, name='index')
]
