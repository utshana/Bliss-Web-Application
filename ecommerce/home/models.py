from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=30)
    email= models.CharField(max_length=30,unique=True)
    contact = models.CharField(max_length=11)
    address = models.CharField(max_length=40)
    password = models.CharField(max_length=20)


    def __str__(self) :
        return self.name
    
    class Meta:
        db_table = 'Member'