from django.shortcuts import render, get_object_or_404, redirect
import os
from django.http import Http404
import loader
from django.urls import reverse_lazy
from .forms import NewsForm
from .models import News,  Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


class HomeNews(ListView):
  model = News
  template_name = 'news/home_news_list.html'
  context_object_name = 'news'
  #extra_context ={'title' : 'Главная'}
  def get_context_data(self, *, object_list=None, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Главная Страница'
      return context
  def get_queryset(self):
      return News.objects.filter(is_published=True)






class NewsByCategory(ListView):
     model = News
     template_name = 'news/home_news_list.html'
     context_object_name = 'news'
     allow_empty = False
     def get_context_data(self, *, object_list=None, **kwargs):
         context = super().get_context_data(**kwargs)
         context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
         return context
     def get_queryset(self):
         return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

def index(request):
    news = News.objects.all()


    context = {
        'news': news,
        'title': 'Список новостей',

    }


    return render(request, template_name="index1.html",context=context)
#| Фильтр в html


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    return render(request, "category.html", {'news': news,  'category': category})

#def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)
#    news_item = get_object_or_404(News, pk=news_id)

#    return  render(request, 'view_news.html', {"news_item" : news_item})

class ViewNews(DetailView):
    model = News
    context_object_name='news_item'
    template_name = 'news/news_detail.html'



class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'add_news.html'
    #success_url = reverse_lazy('home')






    #pk_url_kwarg='news_id'
#def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#
#        if form.is_valid():
#            #news = News.objects.create(**form.cleaned_data)
 #           news = form.save()
#            return redirect(news)
#    else:
 #       form = NewsForm()
#    return render(request,  'add_news.html', {'form': form})


