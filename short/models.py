from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from hashlib import md5

class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=False)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile')
    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs,):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)