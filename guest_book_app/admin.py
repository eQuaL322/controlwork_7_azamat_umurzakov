from django.contrib import admin

from guest_book_app.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_email', 'description', 'status', 'created_at', 'modified_at')
    list_filter = ('id', 'author_name', 'author_email', 'status')
    search_fields = ('author_name', 'author_email', 'description')
    fields = ('author_name', 'author_email', 'description', 'status')


admin.site.register(GuestBook, GuestBookAdmin)
