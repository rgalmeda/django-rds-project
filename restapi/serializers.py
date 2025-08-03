from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #fields = ('__all__')
        fields = ('tittle', 'publication_year', 'isbn', 'author')

# {
#     "key":"value"
# }
