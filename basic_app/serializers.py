from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from basic_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.CustomUser


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(style={'input_type': 'username'})
    password = serializers.CharField(style={'input_type': 'password'})


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = 'id', 'username', 'password', 'is_staff'

    def is_numeric(string):
        return string.is_numeric()

    def create(self, validated_data):
        # print(validated_data)
        if len(validated_data["username"]) < 5:
            raise serializers.ValidationError('Ism 5 ta belgidan kam bo\'lmasligi kerak')
        if len(validated_data["password"]) < 8:
            raise serializers.ValidationError('Parol 8 ta belgidan kam bo\'lmasligi kerak')
        return models.CustomUser.objects.create_user(**validated_data)

    # def validate(self, data):
    #     if len(data['username']) < 5:
    #         raise serializers.ValidationError('Ism 5 ta belgidan kam bo\'lmasligi kerak')
    #     return data
    #
    # def validate(self, data):
    #     if len(data['password']) < 8:
    #         raise serializers.ValidationError('Parol 8 ta belgidan kam bo\'lmasligi kerak')
    #     return data


class UserPasswordSerializer(ModelSerializer):
    username = serializers.CharField(style={'input_type': 'username'})
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = models.CustomUser
        fields = [
            'username',
            'password',
            # "is_superuser",
            "is_staff"
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Home
        fields = '__all__'


class ContactLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactLocation
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'


class AboutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutProduct
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'


class LogoNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LogoName
        fields = '__all__'


class AboutPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutPricing
        fields = '__all__'


class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Award
        fields = '__all__'


class SecondBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SecondBlog
        fields = '__all__'


class AboutProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutProductDetail
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form
        fields = '__all__'
