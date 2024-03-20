from django.shortcuts import render
from .models import *
from . import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView, Response
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests





class CartAPIView(ListAPIView):
    queryset = Cart.objects.all() 
    serializer_class = serializers.CartSerializer
    
            
            

# Create your views here.

class AvtoAPIView(ListAPIView, RetrieveAPIView, UpdateAPIView):
    queryset = Avto.objects.all()
    serializer_class = serializers.AvtoSerializer




class CategoryAPIView(ListAPIView, RetrieveAPIView, UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer



#filter(parent=None)
class SizeCategoryAPIView(ListAPIView, RetrieveAPIView, UpdateAPIView):
    queryset = SizeCategory.objects.all()
    serializer_class = serializers.SizeCategorySerializer



class FuraKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Fura -- Фура', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class FuraOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Fura -- Фура', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class FuraKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Fura -- Фура', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    




class LexkavoyKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Lexkavoy -- Лехкавой', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class 	LexkavoyOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Lexkavoy -- Лехкавой', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class 	LexkavoyKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Lexkavoy -- Лехкавой', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    



class   SelxoztexnikaKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Selxoz texnika -- Сельхозтехника', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class 	SelxoztexnikaOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Selxoz texnika -- Сельхозтехника', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class 	SelxoztexnikaKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Selxoz texnika -- Сельхозтехника', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class   KamazzilKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Kamaz/zil -- Камаз/Зил', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class 	KamazzilOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Kamaz/zil -- Камаз/Зил', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class 	KamazzilKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Kamaz/zil -- Камаз/Зил', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    





class   IsizutralKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Isizu/tral -- Исузу/трал', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class 	IsizutralOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Isizu/tral -- Исузу/трал', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class 	IsizutralKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Isizu/tral -- Исузу/трал', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    





class   KaraKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Kara -- Кара', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class 	KaraOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Kara -- Кара', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class 	KaraKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Kara -- Кара', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


#avtopagruschik
    







class   AvtopagruschikKattaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Avto pagruzchik -- Авто пагрузчик', sizes__differens="Katta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)



class 	AvtopagruschikOrtaCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Avto pagruzchik -- Авто пагрузчик', sizes__differens="O'rta")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class 	AvtopagruschikKichikCategoryAPIView(APIView):
    def get(self, request):
        queryset = Avto.objects.filter(category__name='Avto pagruzchik -- Авто пагрузчик', sizes__differens="Kichik")
        serializer_class = serializers.AvtoSerializer(queryset, many=True)
        return Response(serializer_class.data)
    


class ProductCartAPIView(APIView):
    def post(self, request):
        serializer = serializers.CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        telegram_id = serializer.validated_data['telegram_id']
        product = serializer.validated_data['product']
        plus = serializer.validated_data['telegram_id']
        user = User.objects.filter(telegram_id=telegram_id).first()
        if user:
            cart = Cart.objects.filter(user=user, status='new').first()
            if cart:
                user_product = cart.user_products.filter(product=product)
                if user_product:
                    if plus:
                        user_product.count += 1
                    else:
                        user_product.count -= 1
                    user_product.save()
                else:
                    UserProduct.objects.create(cart=cart, product=product)
            else:
                cart = Cart.objects.create(user=user)
                UserProduct.objects.create(cart=cart, product=product)

            return Response(status=200)
        return Response(status=403)




class ConferensAPIView(ListAPIView, RetrieveAPIView, UpdateAPIView):

    queryset = Conferens.objects.all()
    serializer_class = serializers.ConferensSerializer
    

        