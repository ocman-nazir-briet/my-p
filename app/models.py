import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=32, unique=True)
    created = models.DateTimeField(blank=True)
    
    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    @property
    def fullName(self, *args, **kwargs):
        return str(self.fname + self.lname)
    
    def fullNameRev(self, *args, **kwargs):
        return str(self.lname + self.fname)
    
    fullNameReverse = fullNameRev

    def __str__(self):
        return self.fname
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'List of Authors'


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    des = models.TextField()
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Blogs'

class School(models.Model):
    blog = models.ManyToManyField(Blog)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=32,help_text='must contain 11 digits')
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Schools'

class TesttAbstract(models.Model):
    des = models.TextField()

    class Meta:
        abstract = True

class Testt(TesttAbstract):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name