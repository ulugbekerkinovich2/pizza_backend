from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basic_app.urls'))
]


schema_view = get_swagger_view(title='Swagger')
urlpatterns += [
    path(r'docs', schema_view)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
