from django.db import models
import random
import string

# Create your models here.
class State(models.Model):
     name=models.CharField(max_length=50)
     def __str__(self):
          return self.name
class Gender(models.Model):
     name=models.CharField(max_length=10)
     def __str__(self):
          return self.name

class Aadhar(models.Model):
     first_name=models.CharField(max_length=32)
     last_name=models.CharField(max_length=32)
     father_name=models.CharField(max_length=40)
     mother_name=models.CharField(max_length=40)
     DOB=models.DateField()
     address=models.TextField()
     state=models.ForeignKey(State,on_delete=models.CASCADE)
     pin_code=models.PositiveIntegerField()
     phone=models.PositiveBigIntegerField(unique=True)
     email=models.EmailField()
     aadhar_number=models.BigAutoField(primary_key=True)
     gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
     photo=models.ImageField(upload_to='profiles')
     pan=models.CharField(max_length=10)

     def save(self,*args,**kwargs):
          letter=string.ascii_uppercase
          first=''.join(random.choices(letter,k=5))
          num=''.join(random.choices(string.digits,k=4))
          last=''.join(random.choices(letter,k=1))

          self.pan =first+num+last

          super().save(*args,**kwargs)