from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=100)
    ipaddress = models.GenericIPAddressField()
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.hostname + "(%s) " % self.ipaddress


class HostGroup(models.Model):
    group = models.CharField(max_length=100)
    host = models.ManyToManyField(Host)

    def __str__(self):
        return self.group


class Script(models.Model):
    script_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.script_name


class User(models.Model):
    name = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    privilege = models.ManyToManyField(Host, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
