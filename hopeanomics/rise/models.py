from django.db import models

class State(models.Model):
    name = models.CharField(max_length=2, blank=False, null=False, primary_key=True)


class Campaign(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    state = models.ForeignKey("State", models.DO_NOTHING, blank=False, null=False)


class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=300, blank=True, null=True)
    district = models.IntegerField(blank=True, null=False)
    party = models.CharField(max_length=3, blank=False, null=False)
    first_elected = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey("State", models.DO_NOTHING, blank=False, null=False)
    campaign = models.ForeignKey("Campaign", models.DO_NOTHING, blank=False, null=False)
    branch = models.CharField(max_length=15, null=False)
    number = models.BigIntegerField(null=True)


class Deadline(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, primary_key=True)
    date = models.DateField(blank=False, null=False)
    state = models.ForeignKey("State", models.DO_NOTHING, blank=False, null=False)
