from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
	"""docstring for UserProfileInfo"""

	user = models.OneToOneField(User,on_delete=models.DO_NOTHING)


	#  additional

	portfolio_site = models.URLField(blank=True)

	profile_pic = models.ImageField(upload_to='profilePics',blank=True)

	def __str__(self):
		return self.user.username
		pass