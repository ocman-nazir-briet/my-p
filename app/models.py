import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=32)
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