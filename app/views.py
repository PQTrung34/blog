from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world</h1>')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'