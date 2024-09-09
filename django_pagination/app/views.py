from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import CreateForm

def home(request):
    books = Book.objects.all().order_by('id')
    paginator = Paginator(books, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    return render(request, 'home.html', {'page': page_obj})


class BookCreate(CreateView):
    model = Book
    form_class = CreateForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')



def update(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':

        book.title = request.POST['title']
        book.discription = request.POST['discription']
        book.author = request.POST['author']
        book.published_year = request.POST['published_year']
        book.price = request.POST['price']
        book.genre = request.POST['genre']

        book.save()
        return redirect(reverse('home'))
    return render(request, 'update.html')


def delete(request, id):
    task = Book.objects.get(id=id)
    task.delete()
    return redirect(reverse('home'))