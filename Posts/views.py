from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

class NewPostView(CreateView):
    model = Article
    template_name = 'create.html'
    fields = '__all__'

class DeletePostView(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class EditPostView(UpdateView):
    model = Article
    template_name = 'update.html'
    fields = ['title','text']

