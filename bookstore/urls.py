from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.get_book, name='book_view'),
    path('book/<int:id>/', views.book_detail, name='book_detail_view'),
    path('add-book/', views.add_book, name='add_book_view'),
    path('add-comments/', views.add_comments, name='add_comments_view')
]