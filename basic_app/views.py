from django.shortcuts import render
from rest_framework import generics

from basic_app import models, serializers


# Create your views here.
class ListUsers(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer1


class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserPasswordSerializer


class ListHome(generics.ListCreateAPIView):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer


class DetailHome(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer


class ListContactLocation(generics.ListCreateAPIView):
    queryset = models.ContactLocation.objects.all()
    serializer_class = serializers.ContactLocationSerializer


class DetailContactLocation(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ContactLocation.objects.all()
    serializer_class = serializers.ContactLocationSerializer


class ListAbout(generics.ListCreateAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class DetailAbout(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer


class ListAboutProduct(generics.ListCreateAPIView):
    queryset = models.AboutProduct.objects.all()
    serializer_class = serializers.AboutProductSerializer


class DetailAboutProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AboutProduct.objects.all()
    serializer_class = serializers.AboutProductSerializer


class ListProduct(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ListBlog(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class ListLogoName(generics.ListCreateAPIView):
    queryset = models.LogoName.objects.all()
    serializer_class = serializers.LogoNameSerializer


class DetailLogoName(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LogoName.objects.all()
    serializer_class = serializers.LogoNameSerializer


class ListAboutPricing(generics.ListCreateAPIView):
    queryset = models.AboutPricing.objects.all()
    serializer_class = serializers.AboutPricingSerializer


class DetailAboutPricing(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AboutPricing.objects.all()
    serializer_class = serializers.AboutPricingSerializer


class ListAward(generics.ListCreateAPIView):
    queryset = models.Award.objects.all()
    serializer_class = serializers.AwardsSerializer


class DetailAward(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Award.objects.all()
    serializer_class = serializers.AwardsSerializer


class ListSecondBlog(generics.ListCreateAPIView):
    queryset = models.SecondBlog.objects.all()
    serializer_class = serializers.SecondBlogSerializer


class DetailSecondBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SecondBlog.objects.all()
    serializer_class = serializers.SecondBlogSerializer


class ListAboutProductDetail(generics.ListCreateAPIView):
    queryset = models.AboutProductDetail.objects.all()
    serializer_class = serializers.AboutProductDetailSerializer


class DetailAboutProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AboutProductDetail.objects.all()
    serializer_class = serializers.AboutProductDetailSerializer


class ListForm(generics.ListCreateAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer


class DetailForm(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer
