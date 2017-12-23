from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
   return HttpResponse('Welcome to transfer team!');

def upload(request):
   return HttpResponse('Upload success!');

def redirect(request):
   return HttpResponseRedirect('/trans/index/');

@csrf_exempt
def iostat(request):
   print request.body; 
   return HttpResponse('posrt iostat success!');
   
