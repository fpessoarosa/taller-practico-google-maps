from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Ubicacion(models.Model):
	# author = models.ForeignKey('auth.User')
	nombre = models.CharField(max_length=200)
	latI = models.CharField(max_length=50)
	lngI = models.CharField(max_length=50)
	fechaI = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.nombre