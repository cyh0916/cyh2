from django.http import HttpResponse
from django.http import HttpResponse
def login(request):
	return redirect('/index')
def index(request):
	return HttpResponse('index')
