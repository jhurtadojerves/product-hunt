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
    votes = models.ManyToManyField(Profile, related_name='votes_to')
    url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if Product.objects.filter(slug=slug).exists():
            slug = slug + '-' + self.id
        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('products.Product', related_name='images', on_delete=models.CASCADE)


class Vote(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['product', 'owner', ]
