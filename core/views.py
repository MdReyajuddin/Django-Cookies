from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
    response = HttpResponse('<h1>Set Cookie</h1>')
    response.set_cookie('Cookie1', 'Reyaj_Cookie', max_age=60 )
    return response


def getcookie(request):
    cook=request.COOKIES["Cookie1"]
    return HttpResponse('<h1>Get Cookie</h1>'+ cook)
