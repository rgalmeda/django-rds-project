from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('tittle', 'author', 'publication_year', 'isbn')


class AuthorForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    contact_number = forms.CharField(
        max_length=11,
        min_length=11,
        validators=[
            MinLengthValidator(11, message="Contact number must be exactly 12 digits."),
            RegexValidator(r'^\d+$', message="Only numbers are allowed.")
        ],
        widget=forms.TextInput(attrs={'input mode': 'numeric'}),
    )

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number must contain only digits.")
        if len(contact_number) != 11:
            raise forms.ValidationError("Contact number must be exactly 12 digits.")
        return contact_number

    class Meta:
        model = Author
        fields = ('name', 'biography', 'birth_date','contact_number')
