import django_tables2 as tables
from .models import Author

class AuthorTable(tables.Table):

    edit = tables.TemplateColumn('<a href="{% url "author_update" record.pk %}" class="btn btn-sm btn-primary">Edit</a>')
    delete = tables.TemplateColumn('<a href="{% url "author_delete" record.pk %}" class="btn btn-sm btn-danger">Delete</a>')

    class Meta:
        model = Author
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "biography", "birth_date", "contact_number", "edit", "delete")  # Columns to display


