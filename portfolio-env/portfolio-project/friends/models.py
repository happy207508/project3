from django.db import models

class animal2(models.Model):
	image = models.ImageField(upload_to = 'images/')
	character = models.CharField(max_length = 300)