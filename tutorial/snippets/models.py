from django.db import models
from io import BytesIO  # for resizing images
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    # slugs are generally used in urls
    slug =  models.SlugField()

    class Meta:
        ordering  = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
# it returns a URL for displaying individual model records on the website
    def get_absolute_url(self):
        return f'/{self.slug}/'     

class Customer(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE,blank=True, related_name='customers')
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, null=True, blank=False, help_text='product name')
    slug = models.SlugField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    #import Pillow to use images
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='uploads/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    # this helps to avoid an error if a product that desnt have an image
    @property
    def get_imageUrl(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
        # try:
        #     url = self.image.url
        # except:
        #     url = ''
        # return url
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else: 
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
           

    def make_thumbnail(self, image, size = (300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG' , quality = 85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

