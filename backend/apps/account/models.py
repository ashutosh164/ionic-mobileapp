from django.db import models
from django.contrib.auth.models import User
from apps.post.models import Posts


class Profiles(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='download.png')
    mob = models.CharField(max_length=10, blank=True)
    post = models.ForeignKey(Posts, on_delete=models.DO_NOTHING, null=True, blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    # def __str__(self):
    #     return self.first_name

    def __int__(self):
        return self.user




