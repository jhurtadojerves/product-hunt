# Core imports
from django.db import models

# Third party imports
from markdownx.models import MarkdownxField

# Local imports
from profiles.models import Profile


class Comment(models.Model):
    content = MarkdownxField()
    owner = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
