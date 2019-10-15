from django.urls import path,include
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleDeleteView,
    ArticleUpdateView
)

app_name='articles'

urlpatterns=[

    path('', ArticleListView.as_view(), name='article-list'),
    path('create/',ArticleCreateView.as_view(),name='article-create'),
    path('<int:id>/',ArticleDetailView.as_view(),name='article-detail'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(),name='article-delete'),
    path('<int:id>/update/',ArticleUpdateView.as_view(),name='article-update'),
    # path('',ArticleCreateView.as_view(),name='article-create'),
]