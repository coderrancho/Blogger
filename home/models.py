from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=15,default="")
    content=models.TextField(max_length=1000,default="")
    timestamp=models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.name+'-'+self.email