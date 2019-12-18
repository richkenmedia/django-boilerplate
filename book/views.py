from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book

def index(request):
    result = Book.objects.all().translate('zh')
    return HttpResponse(result)

@csrf_exempt
def create(request):
    book = Book(name =  request.POST.get('name'), description =  request.POST.get('description'))
    book.save()
    return HttpResponse('Index')

def show(request):
    return HttpResponse('Index')

def edit(request):
    return HttpResponse('Index')

def delete(request):
    return HttpResponse('Index')
