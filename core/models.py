from django.db import models
from users.models import User
from django.utils.text import slugify

class Snippet(models.Model):
    title = models.CharField(max_length=200)
    user = models.ManyToManyField(User, related_name="user")
    description = models.TextField(max_length=None)
    language = models.CharField(max_length=30)
    code = models.TextField(max_length=None)
    created_at = models.DateField(auto_now=True)
    # tag = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return f'{self.code}'

    class Meta:
        ordering = ['-created_at']

class Tag(models.Model):
    name = models.CharField(max_length=30)
    snippet = models.ManyToManyField(Snippet, related_name="snippet_tag")
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)