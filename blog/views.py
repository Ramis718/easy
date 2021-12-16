from django.http.response import Http404
from django.shortcuts import render
#from django.http import HttpResponse

from . import models 


# def say_hello(request):
#     return HttpResponse('Hello Word')

# def get_real_posts(request):
#     context = {
#         'posts': Post.objects.all()

#     }  

#     return render(request, 'post_list.html', context)  

def get_posts(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})



def post_detail(request, id):
    try:
        post = models.Post.objects.get(id=id)
    except models.Post.DoesNotExist:
        raise Http404('Post does not exist, baby') 

    return render(request, 'post_detail.html', {'post': post})       