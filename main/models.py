from django.db import models
from django.utils import timezone


class Groups(models.Model):
    groupName =  models.CharField(max_length=50, db_index=True)
    groupDesc = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.groupName + " " + self.groupDesc

class Contacts(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    phoneNumber = models.BigIntegerField()
    email = models.EmailField(max_length=254, blank=True)
    note = models.TextField(max_length=512)
    created_date = models.DateTimeField(
            default=timezone.now)
    last_updated = models.DateTimeField(
            blank=True, null=True)
    group = models.ManyToManyField(Groups)

    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.firstName + " " + self.lastName

