from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from guest_book_app.forms import GuestBookForm
from guest_book_app.models import GuestBook


def add_guest_view(request: WSGIRequest):
    if request.method == "GET":
        form = GuestBookForm()
        return render(request, 'add_guest.html', context={
            'form': form
        })

    form = GuestBookForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_guest.html', context={
            'form': form
        })
    else:
        records = GuestBook.objects.create(**form.cleaned_data)
        return redirect('index')


def update_guest_view(request, pk):
    errors = {}
    guest = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        form = GuestBookForm(request.POST)
        if not form.is_valid():
            errors = form.errors
        else:
            guest.author_name = form.cleaned_data['author_name']
            guest.author_email = form.cleaned_data['author_email']
            guest.description = form.cleaned_data['description']
            guest.save()
            return redirect('index')
    else:
        form = GuestBookForm(initial={
            'author_name': guest.author_name,
            'author_email': guest.author_email,
            'description': guest.description,
        })
    return render(request, 'update_guest.html', context={
        'form': form,
        'guest': guest,
        'errors': errors,
    })


def delete_guest_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'delete_guest.html', context={'guest': guest})


def delete_confirm_guest(request, pk):
    task = get_object_or_404(GuestBook, pk=pk)
    task.delete()
    return redirect('index')
