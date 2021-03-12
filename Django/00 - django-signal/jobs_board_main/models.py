from django.db import models


class Job(models.Model):
    company = models.CharField(blank=False, max_length=255)
    company_email = models.CharField(blank=False, max_length=255)
    title = models.CharField(blank=False, max_length=255)
    details = models.CharField(blank=True, max_length=100)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Subscriber(models.Model):
    email = models.CharField(blank=False, max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    email = models.CharField(blank=False, max_length=255, unique=True)
    user = models.ForeignKey(Subscriber, related_name="subscriptions", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="jobs", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
