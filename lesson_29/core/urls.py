from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app.views import home, CreateUser, view, forgot_password, APIProductsViewSet, APIReadOnlyUsersViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router=DefaultRouter()
router.register('poducts', APIProductsViewSet)
router.register('users', APIReadOnlyUsersViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('view/', view, name='view'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('create/', CreateUser.as_view(), name='create'),
    path('api/', include(router.urls), name='api_products'),
    path('api/', include(router.urls), name='api_users'),
    # path('api_products/', ApiProducts.as_view(), name='api_products'),
    # path('api_product/<int:pk>/', ApiProductsDetail.as_view(), name='api_product')
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 