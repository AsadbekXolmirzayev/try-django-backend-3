from django.db import models
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='articles', null=True, blank=True, help_text='2Mb dan oshmasin')
    content = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    modefied_date = models.DateTimeField(auto_now=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.id})"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save()