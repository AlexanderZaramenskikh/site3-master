from django_filters import FilterSet
from .models import Product, News, Articles


class ProductFilter(FilterSet):
   class Meta:
       model = Product
       fields = {
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': ['lt','gt',],
       }


class NewsFilter(FilterSet):
   class Meta:
       model = News
       fields = {
           'title': ['icontains'],
           'content': ['icontains'],
           'date': ['gt'],
       }


class ArticlesFilter(FilterSet):
   class Meta:
       model = Articles
       fields = {
           'title': ['icontains'],
           'content': ['icontains'],
           'date': ['gt'],
       }
