from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import home, CreateUser, view, forgot_password, api_products, api_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('view/', view, name='view'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('create/', CreateUser.as_view(), name='create'),
    path('api_products/', api_products, name='api_products'),
    path('api_product/<int:id>/', api_product, name='api_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 