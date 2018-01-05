from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from trans_context import Page, TransContext
from mysite.settings import BASE_DIR
import os

# Create your views here.
def get_header():
  c = TransContext('Trans team')
  header_pages = list()
  fns = os.listdir(os.path.join(BASE_DIR, 'trans/templates/header'))
  for fn in fns:
    (sn, ext) = os.path.splitext(fn);
    header_pages.append(Page(sn.capitalize(), sn))
  c.setHeaderPages(header_pages)
  return c   

def index(request):
    c = get_header();
    return render(request, 'default.html', {'site':c}) 

def upload(request):
   return HttpResponse('Upload success!');

def redirect(request):
   return HttpResponseRedirect('/trans/index/');

@csrf_exempt
def iostat(request):
   print request.body; 
   return HttpResponse('posrt iostat success!');
   
def about(request):
  c = get_header();
  return render(request, 'header/about.html',{'site':c})

