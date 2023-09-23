from django.db import models

# Create your models here.
class Cars(models.Model):
		cname=models.CharField(max_length=50)
		ccompany=models.CharField(max_length=50)
		cmodel=models.CharField(max_length=50)
		cprice=models.IntegerField()
		color=models.CharField(max_length=50)

		def __str__(self):
			return self.cname