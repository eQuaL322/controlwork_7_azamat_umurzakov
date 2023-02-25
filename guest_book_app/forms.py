from django import forms
from django.core.exceptions import ValidationError


class GuestBookForm(forms.Form):
    author_name = forms.CharField(max_length=100, required=True, label="Имя")
    author_email = forms.EmailField(max_length=200, required=True, label="Email")
    description = forms.CharField(max_length=2000, required=True, label="Текст", widget=forms.Textarea)

    def clean_title(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 2 or len(author_name) == 0:
            raise ValidationError('Имя не должно быть пустым и длинее 2-х символов!')
        return author_name

    def clean_author_email(self):
        author_email = self.cleaned_data.get('author_email')
        if len(author_email) == 0:
            raise ValidationError('Email не должно быть пустым!')
        return author_email

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) == 0:
            raise ValidationError('Текст не должно быть пустым!')
        return description
