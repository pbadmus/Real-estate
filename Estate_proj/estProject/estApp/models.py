from django.db import models

# Create your models here.

class ChangePassword(models.Model):
    old_password = models.CharField(max_length=30)
    new_password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    
    
    
    
    
