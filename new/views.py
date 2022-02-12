from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
class BlogList(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
class BlogCreate(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','text']
class BlogUp(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','text']
class BlogDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
