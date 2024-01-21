from django.db import models

from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="reviews")
    created_on = models.DateField(auto_now_add=True,
        blank=False, null=False)
    content = models.TextField(max_length=5080)
    is_approved = models.BooleanField(default=False)
    homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.user
