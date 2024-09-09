from app.views import home, BookCreate, update, delete
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')

]
