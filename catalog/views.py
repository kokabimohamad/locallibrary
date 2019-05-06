from django.shortcuts import render
from django.views import generic
from .import models
from django.http import HttpResponse


# Returns a dictionary representing the template context. The keyword arguments provided will make up the returned context.
class Index(generic.TemplateView):

    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
    # This is frequently used to pass all kinds of data to a template: the user that is logged in, forms, querysets, etc. The template can then render these components accordingly.
        context=super().get_context_data(**kwargs)
        context['num_books']=models.Book.objects.all().count()
        context['num_instances']=models.BookInstance.objects.all().count()
        context['num_instances_available']=models.BookInstance.objects.filter(status__exact='a').count()
        context['num_authors']=models.Author.objects.all().count()
        return context

class BookListView(generic.ListView):
    model=models.Book
    template_name='catalog/book_list.html'

class BookDetailView(generic.DetailView):
    model=models.Book
    template_name='catalog/book_detail.html'
class AuthorListView(generic.ListView):
    model=models.Author
    template_name='catalog/author_list.html'
# class loginview(generic.DetailView):









# def index(request):
#     # return HttpResponse("<h1>hhhhhhhhhhhhhhhhhhh</h1>")
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_books=models.Book.objects.all().count()
#     num_instances=models.BookInstance.objects.all().count()
#     # Available books (status = 'a')
#     num_instances_available=models.BookInstance.objects.filter(status__exact='a').count()
#     num_authors=models.Author.objects.count()  # The 'all()' is implied by default.
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'catalog/index.html',
#
#     )

# Create your views here.
# context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
