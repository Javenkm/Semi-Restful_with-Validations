from django.db import models


class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title must be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description must be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()