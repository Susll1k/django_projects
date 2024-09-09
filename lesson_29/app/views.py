from django.shortcuts import render
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

def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return JsonResponse(serializer.data, safe=False)




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
def home(request):
    users=UserProfile.objects.all()
    my_custom_attr_1 = request.my_custom_attr_1
    my_custom_attr_2 = request.my_custom_attr_2


    return render(request, 'home.html', {'users':users,'custom_attr_1':my_custom_attr_1,'custom_attr_2':my_custom_attr_2})

class CreateUser(CreateView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'create.html'
    form_class = CreateUserForm

        




