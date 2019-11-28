from django.db import models
import datetime
# Create your models here.
class publishinfo(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=32, null=False)
    def __str__(self):
        return self.pname
    # class Meta:
    #     ordering = 'pname'

class bookinfo(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=32,null=False)
    bprice = models.DecimalField(max_digits=6,decimal_places=2,default=16.99) # max_digits=6,decimal_places=2这两个参数是必填项
    binventory = models.IntegerField(default=100)
    bsalesvolume = models.IntegerField(default=0)
    bpublishdata = models.DateField(default=datetime.date.today())
    book_pubish = models.ForeignKey(to=publishinfo,on_delete=models.CASCADE)
    #book_pubish = models.ForeignKey(to=publishinfo,on_delete=models.CASCADE,related_name='books')
    #book_pubish = models.ForeignKey(to=publishinfo,on_delete=models.CASCADE,related_query_name='xxoo')
    def __str__(self):
        return self.bname

class authorinfo(models.Model):
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=32,null=False)
    aage = models.IntegerField(default=20,null=True)
    aphone = models.CharField(max_length=32,null=True)
    author_book_publish = models.ManyToManyField(bookinfo)
    adetails = models.OneToOneField(to="authordetails",on_delete=models.CASCADE)
    def __str__(self):
        return self.aname

class authordetails(models.Model):
    ahobby = models.CharField(max_length=32,default='dog',null=True)
    alocation = models.CharField(max_length=32,default='Canada',null=True)
