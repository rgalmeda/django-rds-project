from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django_tables2.config import RequestConfig

from django_tables2 import SingleTableView
from django_filters.views import FilterView
import django_filters

from .tables import AuthorTable
from .filters import AuthorFilter  # If using filters

# django login required
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden



@login_required
def index(request):
    return render(request, 'index.html', {})

# Views for Books
@login_required
def book_list(request):
    if not request.user.has_perm('books.can_access_specific_functionality'):
        return HttpResponseForbidden("You don't have permission to access this page.")
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})


# Views for Authors
@login_required
def author_list(request):
    if not request.user.has_perm('books.can_access_specific_functionality'):
        return HttpResponseForbidden("You don't have permission to access this page.")

    authors = Author.objects.all()
    author_filter = AuthorFilter(request.GET, queryset=authors)  # ✅ Apply filtering

    table = AuthorTable(author_filter.qs)  # ✅ Use the filtered queryset

    RequestConfig(request, paginate={"per_page": 2}).configure(table)  # ✅ Enable pagination

    return render(request, 'author_list.html', {
        'table': table,
        'filter': author_filter,  # ✅ Pass filter to template for search input
    })


class AuthorListView(SingleTableView, FilterView):
    table_class = AuthorTable  # ✅ Table for authors
    model = Author
    table_class = AuthorTable
    template_name = "author_list.html"
    filterset_class = AuthorFilter  # ✅ Connect filtering
    paginate_by = 2  # Paginate results (5 per page)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AuthorFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

@login_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})


@login_required
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})


@login_required
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})


@login_required
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_confirm_delete.html', {'author': author})
