import os
import datetime
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksystem.settings")
    import django
    django.setup()
    from django.db.models import F,Q
    # 此处导入，必须在django.setup()后，因为只有启动Django才能执行，否则会报错

    # ORM查询练习
    from bookAPP import models
    # 1查找书名里面包含学字的所有
    rs = models.bookinfo.objects.filter(bname__icontains='学')
    print(*rs)
    # 2查询出版时间为2018年的所有书
    rs = models.bookinfo.objects.filter(bpublishdata__year=2018)
    print(*rs)
    # 3查询价格大于50的书
    rs = models.bookinfo.objects.filter(bprice__gt=50)
    print(*rs)
    # 4查询价格大于50的书,列出名字和价格
    rs = models.bookinfo.objects.filter(bprice__gt = 50).values_list('bname','bprice')
    print(*rs)
    # 5所有出过书的出版社  用到distinct去重知识
    rs = models.bookinfo.objects.all().values_list('book_pubish__pname')
    print(*rs.distinct())
    # 6将所有书按照价格倒序排序
    rs = models.bookinfo.objects.all().order_by('bprice').reverse() # 另外一种查询
    rs1 = models.bookinfo.objects.all().order_by('-bprice') #用- 号也同时表示倒序
    print(rs)
    print(rs1)
    # 7查询书名有科技的书的出版社 跨一张表
    rs = models.bookinfo.objects.filter(bname__icontains='化学').values_list('book_pubish__pname')
    print(rs)
    # 8查询书名是科技指南的作者爱好 跨两张表
    rs = models.bookinfo.objects.filter(bname='科技指南').values_list('authorinfo__adetails__ahobby')
    print(rs)



















