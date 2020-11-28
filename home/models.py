from django.db import models

# Create your models here.


# for uploading projects
class Project(models.Model):
    image=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=50)
    desc=models.TextField()

    def __str__(self):
        return self.title


# for contact form
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    desc=models.TextField()

    def __str__(self):
        return self.name +"-"+ self.phone

 