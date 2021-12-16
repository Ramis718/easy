from django.http.response import Http404
from django.shortcuts import render


from . import models 


def get_book(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})



def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        raise Http404('Post does not exist, baby') 

    return render(request, 'book_detail.html', {'book': book})       