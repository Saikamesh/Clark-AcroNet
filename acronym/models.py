from django.db import models

# Create your models here.
class Acronym(models.Model):
     acronym_name = models.CharField(max_length=10)
     full_form = models.CharField(max_length=70)
     description = models.CharField(max_length=300)
     location = models.CharField(max_length=20)
     phone_number = models.IntegerField(max_length=10)
     email = models.EmailField(max_length=50)
     website = models.URLField(max_length=100)
     created_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f"{self.acronym_name} - {self.full_form}"

class Users(models.Model):
     user_name = models.CharField(max_length=50)
     user_type = user_type = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User'), ('su', 'Super_User')])
     email = models.EmailField(max_length=50)
     password = models.CharField(max_length=50)
     
     def __str__(self):
          return f"{self.user_name} - {self.user_type}"

class Suggestions(models.Model):
    acronym_name = models.CharField(max_length=10)
    full_form = models.CharField(max_length=70)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=20)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    suggested_by_name = models.CharField(null=True, max_length=50)
    suggested_by_email = models.EmailField(null=True, max_length=50)
    status = models.CharField(default='pending', max_length=10, choices=[('approved','Approved'),('rejected','Rejected'),('pending','Pending')])

    def __str__(self):
          return f"{self.acronym_name} - {self.full_form}"