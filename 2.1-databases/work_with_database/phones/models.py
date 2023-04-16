from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(Phone, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }
        return reverse('products:product_detail', kwargs=kwargs)




















#
# from django.utils.text import slugify

# class Phone(models.Model):
#     id = models.IntegerField(primary_key=True, unique=True)
#     name = models.CharField(max_length = 30)
#     image = models.TextField()
#     price = models.IntegerField()
#     release_date = models.DateField()
#     lte_exists = models.BooleanField()
#     slug = models.SlugField(blank=True, unique=True, verbose_name='URL')
#
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.slug)
    #     super(Phone, self).save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     kwargs = {
    #         'slug': self.slug,
    #     }
    #     return reverse('products:product_detail', kwargs=kwargs)

