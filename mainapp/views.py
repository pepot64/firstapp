from django.shortcuts import render
from .models import Comment

def index(request):
	comments = Comment.objects.all()
	return render(request, 'index.html', {'comments' : comments})
