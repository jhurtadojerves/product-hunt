# Core imports
from django.db import models
from django.utils.text import slugify

# Third party imports

# Local imports
from profiles.models import Profile


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    owner = models.ForeignKey(Profile, related_name='product', on_delete=models.CASCADE)
    votes = models.ManyToManyField(Profile, related_name='votes_to')  # Votos puede ser una clase desde la cual se apunta a Productos y a el usuario. Queda mejor con ManyToMany

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)

