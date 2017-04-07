from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Comment(models.Model):

	name = models.CharField(max_length=100)
	age = models.DecimalField(max_digits=20, decimal_places=2)
	says = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
