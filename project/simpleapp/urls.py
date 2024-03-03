from django.urls import path

from .views import (ProductsList, ProductDetail , NewsDetail , NewsList, ProductCreate,
                    ProductUpdate, ProductDelete , NewsCreate , NewsUpdate , NewsDelete,
                    ArticlesCreate, ArticlesUpdate, ArticlesDelete, ArticlesList, NewsSearch,
                    ProtectedView)

urlpatterns = [
   path('products/', ProductsList.as_view(), name='product_list'),
   path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
   path('news/', NewsList.as_view(), name='news_list'),
   path('new/<int:pk>', NewsDetail.as_view(), name='new_detail'),
   path('product/create/', ProductCreate.as_view(), name='product_create'),
   path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('news/search/', NewsSearch.as_view(), name='news_search'),
   path('articles/', ArticlesList.as_view(), name='articles_list'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
   path('login/', ProtectedView.as_view(), name='login'),
]