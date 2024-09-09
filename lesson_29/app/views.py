from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import UserProfile
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .serializers import ProductSerializer
from .models import Product
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def home(request):
    if request.method == 'POST':
        id =request.POST['id_product']
        return redirect(f'api_product/{id}/')
    users=UserProfile.objects.all()
    my_custom_attr_1 = request.my_custom_attr_1
    my_custom_attr_2 = request.my_custom_attr_2

    return render(request, 'home.html', {'users':users,'custom_attr_1':my_custom_attr_1,'custom_attr_2':my_custom_attr_2})



@api_view(['GET', 'POST'])
def api_products (request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','PATCH','DELETE'])
def api_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product,many=False) 
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = ProductSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        


def view(request):
    response = HttpResponse('Hello view')
    if 'counter' in request.COOKIES:
        cnt = 1 + int(request.COOKIES['counter'])
    else:
        cnt = 1
    response.set_cookie('counter', cnt)
    return response


def forgot_password(request):
    user = UserProfile.objects.get(id=2)
    send_mail(
        "Subject here",
        "Here is the message.",
        f"{settings.EMAIL_HOST_USER}",
        ["chil.dima008@gmail.com"],
        fail_silently=False
    )
    return HttpResponseRedirect("/")


class CreateUser(CreateView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'create.html'
    form_class = CreateUserForm

        




