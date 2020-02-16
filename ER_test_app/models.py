from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from random import randint


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	website = models.URLField(blank=True)
	avatar = models.ImageField(upload_to='profile_images', default="avatar.png")
	visits = models.IntegerField(default=0)
	
	def __unicode__(self):
		return str(self.user.username) + " - " + str(self.packet_name)
	def __str__(self):
		return str(self.user)

class NumberPacket(models.Model):
	packet_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	packet_name = models.CharField(max_length=100, blank=True)
	packet_content = models.TextField()
	
	def __unicode__(self):
		return str(self.user.username) + " - " + str(self.packet_name)
	def __str__(self):
		return str(self.user.username) + " - " + str(self.packet_name)

class DataAboutSending(models.Model):
	sending_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	packet_id = models.ForeignKey(NumberPacket, on_delete=models.PROTECT)
	message = models.FileField(upload_to="messages/", default="somefile.mp3")
	
	def __unicode__(self):
		return self.user.username + " - " + self.sending_id
	def __str__(self):
		return str(self.user) + " - " + str(self.sending_id)


