from django.conf import settings
from django.db import models
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status="P")

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

class BlogPost(models.Model): 
    POST_STATUS = (('D', 'Draft'),('P', 'Publised'))
    user    = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title  = models.CharField(unique = True, max_length=120, blank=False, null = False)
    slug   = models.SlugField(null=False, unique=True)
    content  = models.TextField(null=True, blank=False)
    timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=POST_STATUS, blank=False)

    objects = BlogPostManager()
    
    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f"/posts/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)