from django.db import models

# Create your models here.
#Table name, has to wrap models.Model to get the functionality of Django.
 class todo(models.Model):

 	name = models.CharField(max_length=100, unique=True) #like a VARCHAR field
 	description = models.TextField() #like a TEXT field
 	created = models.DateTimeField() #like a DATETIME field

 	#Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
 	def __unicode__(self):
 		return self.name