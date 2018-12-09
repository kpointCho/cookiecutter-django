from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_(""), auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

class Comment(TimeStampedModel):

    text = models.TextField()