from django.db import models

# Create your models here.

class dept(models.Model):
    Dno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=50)
    D_loc=models.CharField(max_length=50)
    def __str__(self):
        return self.Dname
        
  
class emp(models.Model):
    Eno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    Hiredate=models.DateField(auto_now=True)
    Dno=models.ForeignKey(dept,on_delete=models.CASCADE)
    Mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.Ename
