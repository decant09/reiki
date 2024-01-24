from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Requests'

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name="contact")
    name = models.CharField(max_length=254, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField(max_length=1016)
    created_on = models.DateField(auto_now_add=True, null=False, blank=False,)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
