from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=254, blank=False, null=False)
    answer = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.question
