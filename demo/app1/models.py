from django.db import models

null_args = dict(null=True, blank=True)


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    alias = models.CharField(max_length=100)
    website = models.URLField(**null_args)
    area = models.CharField(max_length=8, choices=(
        ('CN', 'China'),
        ('US', 'America'),
    ), **null_args)
