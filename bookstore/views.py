from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from . import models, forms





def get_book(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})



def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
        try:
            comment = models.Comment.objects.filter(post_id=id).order_by('created_date')
        except models.Comment.DoesNotExist:
            return HttpResponse('No Comments') 
    except models.Book.DoesNotExist:
        raise Http404('Book does not exist, baby') 

    return render(request, 'book_detail.html', {'book': book, 'book_comment': comment})       



def add_book(request):
    method = request.method
    if method == 'BOOK':
        form = forms.BookForm(request.BOOK, request.FILES)
        print(form.data)
        models.Book.objects.create(title=form.data['title'], description=form.data['description'], image=form.data['image'])

        return HttpResponse('Book Created Successfully')

    else:
        form = forms.BookForm()

    return render(request, 'add_book.html', {'form': form})    



def add_comment(request):
    method = request.method
    if method == 'BOOK':
        form = forms.CommentForm(request.BOOK, request.FILES)
        print(form.data)
        if form.is_valid():
            forms.save()
            return HttpResponse('Comment created successfully')

    else:
        form = forms.CommentForm()

    return render(request, 'add_comments.html', {'form': form}) 
