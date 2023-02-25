from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from guest_book_app.models import GuestBook


def home_page(request: WSGIRequest):
    records = GuestBook.objects.all().filter(status='active').order_by('-created_at')
    context = {
        'records': records
    }

    return render(request, 'index.html', context=context)
