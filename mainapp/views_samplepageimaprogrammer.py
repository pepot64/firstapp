from django.shortcuts import render
from django.http import HttpResponse


def indeximaprogrammer(request):
	return HttpResponse('<h1>Hello Im A Programmer</h1>')
