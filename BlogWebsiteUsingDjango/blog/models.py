from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


#CATEGORY

class category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img_url=models.ImageField(null=True,upload_to="posts/images/",blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    @property
    def formatted_img_url(self):
        if not self.img_url:
            return ""  # or a default image URL

        if str(self.img_url).startswith(("http://", "https://")):
            return self.img_url

        return self.img_url.url

    
    def __str__(self):
        return self.title
    

class AboutUs(models.Model):
    content=models.TextField()
