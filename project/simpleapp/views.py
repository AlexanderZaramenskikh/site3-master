from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy , resolve
from .models import News , Articles , Product , Post , Category , User
from datetime import datetime
from .filters import ProductFilter, NewsFilter
from .forms import ProductForm, NewsForm , ArticlesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, reverse, redirect

class PostCategoryView(ListView):
    model = Post
    template_name = 'news/category.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        self.id = resolve(self.request.path_info).kwargs['pk']
        c = Category.objects.get(id=self. id)
        queryset = Post.objects.filter(category=c)
        return queryset

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #user = self.request.user
        #category = Category.objects.get(id=self. id)
        #if not subscribed:
            #context['category'] = category

       # return context


class ProtectedView(LoginRequiredMixin, UpdateView):
    template_name = 'login.html'


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

class NewsList(ListView):
    model = Post
    ordering = 'date'
    template_name = 'news.html'
    context_object_name = 'News'
    paginate_by = 5

    def get_queryset(self):
        # self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(choice='NE').order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        # context['category'] = self.category

        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    ordering = '-date'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesList(ListView):
    model = Articles
    ordering = '-date'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ArticlesCreate(CreateView):
    form_class = ArticlesForm
    model = Articles
    template_name = 'articles_edit.html'


class ArticlesUpdate(UpdateView):
    form_class = ArticlesForm
    model = Articles
    template_name = 'articles_edit.html'


class ArticlesDelete(DeleteView):
    model = Articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')

