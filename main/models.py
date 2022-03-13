from django.db import models
from django.contrib.auth.models import User

class ContractorUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)
    company = models.CharField(max_length=30, null=True)
    #todo: verification document part left 
    quot_doc = models.FileField(max_length=20, null=True)
    amount = models.FloatField(max_length=20, null=True)
    type = models.CharField(max_length=15, null=True)
    contr = models.IntegerField(max_length=10, null=True)
    def _str_(self):
        return self.user.username


class GovernmentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)
    state = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=15, null=True)
    #todo: verification document part left 
    def _str_(self):
        return self.user.username


class Contract(models.Model):
    government = models.ForeignKey(GovernmentUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    budget = models.FloatField(max_length=20, null=True)
    doc = models.FileField(null=True)
    description = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=100)
    creationdate = models.DateField()
    type = models.CharField(max_length=15, null=True)

    def _str_(self):
        return self.title
