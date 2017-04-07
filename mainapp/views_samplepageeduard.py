from django.shortcuts import render
from django.http import HttpResponse


def indexhelloeduard(request):
	return HttpResponse('<h1>Hello Eduard</h1>')
