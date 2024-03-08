from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path("avto-list/", AvtoAPIView.as_view()),
    # path("avto-list/<int:f"{Avto['category']}">/", AvtoAPIView.as_view()),
    path("avto-detail/<int:pk>/", AvtoAPIView.as_view()),
    path("category-list/", CategoryAPIView.as_view()),
    path("category-detail/<int:pk>/", CategoryAPIView.as_view()),
    path("size-category-list/", SizeCategoryAPIView.as_view()),
    path("size-category-detail/<int:pk>/", SizeCategoryAPIView.as_view()),
    path("fura-katta-category/", FuraKattaCategoryAPIView.as_view(), name='Fura-katta-category'),
    path('fura-orta-category/', FuraOrtaCategoryAPIView.as_view(), name='Fura-orta-category'),
    path('fura-kichik-category/', FuraKichikCategoryAPIView.as_view(), name='Fura-kichik-category'),
    path('lexkavoy-katta-category/', LexkavoyKattaCategoryAPIView.as_view(), name='Lexkavoy-katta-category'),
    path('lexkavoy-orta-category/', LexkavoyOrtaCategoryAPIView.as_view(), name='Lexkavoy-orta-category'),
    path('lexkavoy-kichik-category/', LexkavoyKichikCategoryAPIView.as_view(), name='Lexkavoy-kichik-category'),
    path('selxoztexnika-katta-category/', SelxoztexnikaKattaCategoryAPIView.as_view(), name='selxoztexnika-katta-category'),
    path('selxoztexnika-orta-category/', SelxoztexnikaOrtaCategoryAPIView.as_view(), name='selxoztexnika-orta-category'),
    path('selxoztexnika-kichik-category/', SelxoztexnikaKichikCategoryAPIView.as_view(), name='selxoztexnika-kichik-category'),
    path('kamazzil-katta-category/', KamazzilKattaCategoryAPIView.as_view(), name='kamazzil-katta-category'),
    path('kamazzil-orta-category/', KamazzilOrtaCategoryAPIView.as_view(), name='kamazzil-orta-category'),
    path('kamazzil-kichik-category/', KamazzilKichikCategoryAPIView.as_view(), name='kamazzil-kichik-category'),
    path('isizutral-katta-category/', IsizutralKattaCategoryAPIView.as_view(), name='isizutral-katta-category'),
    path('isizutral-orta-category/', IsizutralOrtaCategoryAPIView.as_view(), name='isizutral-orta-category'),
    path('isizutral-kichik-category/', IsizutralKichikCategoryAPIView.as_view(), name='isizutral-kichik-category'),
    path('kara-katta-category/', KaraKattaCategoryAPIView.as_view(), name='kara-katta-category'),
    path('kara-orta-category/', KaraOrtaCategoryAPIView.as_view(), name='kara-orta-category'),
    path('kara-kichik-category/', KaraKichikCategoryAPIView.as_view(), name='kara-kichik-category'),
    path('avtopagruschik-katta-category/', AvtopagruschikKattaCategoryAPIView.as_view(), name='avtopagruschik-katta-category'),
    path('avtopagruschik-orta-category/', AvtopagruschikOrtaCategoryAPIView.as_view(), name='avtopagruschik-orta-category'),
    path('avtopagruschik-kichik-category/', AvtopagruschikKichikCategoryAPIView.as_view(), name='avtopagruschik-kichik-category'),
    path('karzinka/', CartAPIView.as_view(), name='karzinka'),
    path('cart/', ProductCartAPIView.as_view()),
]





