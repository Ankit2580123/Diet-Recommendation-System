from django.db import models

# GENDER_CHOICES = (
#    ('M', 'Male'),
#    ('F', 'Female')
# )
# Diseases = (
#    ('M', 'Male'),
#    ('F', 'Female')
# )
# Create your models here.
class signup(models.Model):
    username=models.CharField(null=False, max_length=50)
    mobile_no=models.IntegerField(null=False)
    email=models.CharField(max_length=15)
    password=models.CharField(max_length=255)


class ContactsInformations(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    message=models.TextField()

class DietForm(models.Model):
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=128)
    age=models.IntegerField(null=False)
    bmi=models.FloatField(null=True)
    diseases=models.CharField(max_length=128)
    foodType=models.CharField(max_length=128)

    

    


