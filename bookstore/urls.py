from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.get_book, name='book_view'),
    path('book/<int:id>/', views.book_detail, name='book_detail_view'),
]