from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=250, null=True)
	description = models.TextField(null=True, blank=True)
	posted_on = models.DateTimeField()
	posted_by = models.ForeignKey(User, null=True)
	slug = models.SlugField(null=True, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('-posted_on',)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)