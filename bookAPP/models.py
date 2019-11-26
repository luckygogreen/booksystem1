from django.db import models

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
    book_pubish = models.ForeignKey(to=publishinfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.bname

class authorinfo(models.Model):
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=32,null=False)
    author_book_publish = models.ManyToManyField(bookinfo)
    def __str__(self):
        return self.aname
