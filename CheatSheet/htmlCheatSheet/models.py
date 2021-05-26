from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class HtmlModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    example_html = models.TextField()

    def get_absolute_url(self):
        return reverse("htmlpage")

    def min_text(self):
        x = min(50, len(self.description))
        return self.description[:x]

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    html = models.ForeignKey(
        'htmlCheatSheet.HtmlModel', related_name='comments')
    author = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.text
