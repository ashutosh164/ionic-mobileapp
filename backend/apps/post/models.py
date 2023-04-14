from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=250, blank=True, null=True)
    desc = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.title


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return f'{self.user}--{self.post}--{self.value}'


class Comment(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    body = models.CharField(max_length=250, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

