from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView,
    UpdateView
    )

from .models import Article
from .forms import ArticleForm


# Mixins..
# to use these classes in other main class..
class GetObjectMixin(object):

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class FormValidMixin(object):

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

# ******

class ArticleListView(ListView):
    template_name='articles/article_list.html'
    queryset=Article.objects.all()


class ArticleCreateView(FormValidMixin,CreateView):
    template_name='articles/article_create.html'
    form_class=ArticleForm
    queryset=Article.objects.all()


class ArticleDetailView(GetObjectMixin,DetailView):
    template_name='articles/article_detail.html'

class ArticleUpdateView(GetObjectMixin,FormValidMixin,UpdateView):
    template_name='articles/article_create.html'
    form_class=ArticleForm

class ArticleDeleteView(GetObjectMixin,DeleteView):
    template_name='articles/article_delete.html'
    
    def get_success_url(self):
        return reverse('articles:article-list')



    