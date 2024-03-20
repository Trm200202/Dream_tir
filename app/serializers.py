from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"


class SizeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SizeCategory
        fields = "__all__"

class AvtoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    sizes = SizeCategorySerializer()

        


    class Meta:
        model = models.Avto
        fields = "__all__"



class CartSerializer(serializers.Serializer):
    telegram_id =serializers.CharField()
    product = serializers.PrimaryKeyRelatedField(queryset=models.Avto.objects.all())
    plus = serializers.BooleanField()


class ConferensSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Conferens
        fields = "__all__"