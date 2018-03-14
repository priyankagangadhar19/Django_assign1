from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user  = models.OneToOneField(User)
	about = models.CharField(max_length=200)
	karma = models.IntegerField(default=0)

	def __unicode__(self):
		return u"%s" % self.user


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)