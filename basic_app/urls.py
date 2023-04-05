from django.urls import path, include
from rest_framework import routers

from basic_app import views
from .views import ChatRoomViewSet, ChatMessageViewSet

urlpatterns = [
    path('users/', views.ListUsers.as_view()),
    path('users/<int:pk>', views.DetailUsers.as_view()),
    path('home/', views.ListHome.as_view()),
    path('home/<int:pk>', views.DetailHome.as_view()),
    path('contact_location/', views.ListContactLocation.as_view()),
    path('contact_location/<int:pk>', views.DetailContactLocation.as_view()),
    path('about/', views.ListAbout.as_view()),
    path('about/<int:pk>', views.DetailAbout.as_view()),
    path('about_product/', views.ListAboutProduct.as_view()),
    path('about/<int:pk>', views.DetailAboutProduct.as_view()),
    path('product/', views.ListProduct.as_view()),
    path('product/<int:pk>', views.DetailProduct.as_view()),
    path('blog/', views.ListBlog.as_view()),
    path('blog/<int:pk>', views.DetailBlog.as_view()),
    path('blog/', views.ListBlog.as_view()),
    path('blog/<int:pk>', views.DetailBlog.as_view()),
    path('about_pricing/', views.ListAboutPricing.as_view()),
    path('about_pricing/<int:pk>', views.DetailAboutPricing.as_view()),
    path('award/', views.ListAward.as_view()),
    path('award/<int:pk>', views.DetailAward.as_view()),
    path('second_blog/', views.ListSecondBlog.as_view()),
    path('award/<int:pk>', views.DetailSecondBlog.as_view()),
    path('about_product_detail/', views.ListAboutProductDetail.as_view()),
    path('about_product_detail/<int:pk>', views.DetailAboutProductDetail.as_view()),
    path('form/', views.ListForm.as_view()),
    path('form/<int:pk>', views.DetailForm.as_view()),
]

router = routers.DefaultRouter()
router.register('chatrooms/', ChatRoomViewSet)
router.register('chatmessages/', ChatMessageViewSet)

urlpatterns += [
    path('', include(router.urls)),
    # path('v1/', views.usd_to_eur)
]
