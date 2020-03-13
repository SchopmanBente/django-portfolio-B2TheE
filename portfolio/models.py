
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import subprocess
from django_portfolio.settings import *
import requests
from django_portfolio.settings.base import get_secret

# Create your models here.
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Graphic(models.Model):
    name = models.CharField(max_length=500,default="", editable=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
class Article(models.Model):
    title = models.CharField(max_length=500)
    head_image = models.ForeignKey(Graphic, on_delete=models.CASCADE, related_name="head_image")
    text = models.TextField(max_length=100000)
    images = models.ManyToManyField(Graphic,verbose_name="list of images", related_name="images")

class GitHubAccount(object):

    def __init__(self):


    def get_authentication(self):
        OAUTH_TOKEN = get_secret(setting="OAUTH_TOKEN")
        print(OAUTH_TOKEN)
        command = 'curl -H "Authorization: token {0}" https://api.github.com'.format(OAUTH_TOKEN)
        response = subprocess.run(command)
        return response




class GitHubPortfolioItem(models.Model):
    pass










