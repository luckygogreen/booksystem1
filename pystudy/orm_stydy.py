import os
#如果需要在一个单独的PY脚本文件中导入Django模块，下面是固定代码 booksystem1 是你的项目名，bookAPP是你的settings.py所在文件夹名
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksystem1.settings")
    import django
    django.setup()
    from bookAPP import models  #此处导入，必须在django.setup()后，因为只有启动Django才能执行，否则会报错

    #查询的用法
    print('⬇ ️all()取所有️')
    print(models.publishinfo.objects.all())  #查询打印所有的出版社
    print('⬇ filter()取数据️')
    print(models.publishinfo.objects.filter(pid=1)) #用filter查询如果没有，则返回空
    print('⬇ ️filter()[0]取数据，取第一个元素')
    print(models.publishinfo.objects.filter(pid=1)[0]) #用filter查询如果没有，则返回空,0是去第一个元素，去到的是具体对象内容
    print('⬇ get()取数据')
    print(models.publishinfo.objects.get(pid=1)) #用get查询如果没有，则报错 #matching query does not exist.
    print('⬇ exclude()取数据')
    print(models.publishinfo.objects.exclude(pid=1)[0]) # 排除赛选的值，取其他的值[0]第一个元素
    print('values取指定列字段'.center(30,'⬇'))
    print(models.publishinfo.objects.values('pname')) #返回指定列的一个字典
    print('values取所有字段'.center(30, '⬇'))
    print(models.publishinfo.objects.values()) #返回全部列的字段
    print('values_list 取所有字段'.center(30, '⬇'))
    print(models.publishinfo.objects.values_list()) # 返回一个元祖
    print('values_list 取指定字段'.center(30, '⬇'))
    print(models.publishinfo.objects.values_list('pname'))  # 返回一个元祖
    print('order_by 排序取数据'.center(30, '⬇'))
    print(models.publishinfo.objects.order_by('pname')) #根据指定字段排序 # 如果不给字段，则按照Model定义的Meta原则排序
    print('reverse 反向排序取数据'.center(30, '⬇'))
    print(models.publishinfo.objects.order_by('pname').reverse()) #reverse 只能对有序排序的结果排序，例如Meta定义好的，或者是想这样先order_by在reverse排序的
    print('count 计算返回值的数量'.center(30, '⬇'))
    print(models.publishinfo.objects.count()) # 返回这个数据的个数，可以理解表数据的行数
    print('first 取首个数据'.center(30, '⬇'))
    print(models.publishinfo.objects.first()) #返回第一条记录
    print('last 取尾个数据'.center(30, '⬇'))
    print(models.publishinfo.objects.last()) #返回最后一条记录
    print('exists 判断是否为空表'.center(30, '⬇'))
    print(models.publishinfo.objects.exists()) #判断是否为空表，返回一个Ture或False的布尔值
    print('pid__gt 大于，pid__lt小于'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pid__gt=1,pid__lt=6)) #查询id 大于1小于6的数据
    print('pid__in 取指定内容的值'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pid__in=[1,3,5,7,9])) # 取出ID为 1，3，5，7，9的值
    print('pname__contains 模糊查询区分大小写'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pname__contains='A')) # 模糊查询区分大小写
    print('pname__icontains 模糊查询不区分大小写'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pname__icontains='A')) #模糊查询不区分大小写
    print('pid__range 范围区间取值'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pid__range=[1,8])) #取ID范围是1-8之间的值
    print('pname__startswith和istartswith 匹配开始取值'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pname__startswith='a')) #取a开头的数据，区分大小写
    print(models.publishinfo.objects.filter(pname__istartswith='a')) #取a开头的数据，不区分大小写
    print('pname__endswith和iendswith 匹配末尾取值'.center(30, '⬇'))
    print(models.publishinfo.objects.filter(pname__endswith='R')) #取R结尾的数据，区分大小写
    print(models.publishinfo.objects.filter(pname__iendswith='R')) #取R结尾的数据，不区分大小写
    # date字段还可以：
    # models.Class.objects.filter(first_day__year=2017) #还有字段__year

    print('*'*100)
#  外键表的查询,主键到外键教做正向查询，外检表到主键表叫反向查询 #基于对象查询
    res = models.bookinfo.objects.first()
    re = res.book_pubish
    r = res.book_pubish.pname
    print(res,type(res))
    print(re,type(re))
    print(r,type(r))
#基于双下划线查找方法
    result = models.bookinfo.objects.filter(bid=3).values('book_pubish__pname')
    print(result,type(result))
#end

#  外键表的查询,主键到外键教做反向查询，外检表到主键表叫反向查询 #基于对象查询
    publish_object = models.publishinfo.objects.first()
    reverse_result = publish_object.bookinfo_set.all() #如果Class model中没有定义related_name ,则需要这样查找
    #reverse_result = publish_object.books.all() ##如果Class model中定义了related_name ,就可以直接用定义的名字查
    print('*'*100)
    print(reverse_result)
    print(reverse_result[0])
#双下划线查找方法 #基于双下划线查询
    reverse_result = models.publishinfo.objects.filter(pid=1).values_list('bookinfo__bname')
    #reverse_result = models.publishinfo.objects.filter(pid=1).values_list('books__bname') #如果Class model中定义了related_query_name='xxoo'
    #reverse_result = models.publishinfo.objects.filter(pid=1).values_list('xxoo__bname') #如果Class model中定义了related_query_name='xxoo'
    print(reverse_result[0])


#多对多查询
    #create()
    print('*'*100)
    #查询第一个作者
    author_obj = models.authorinfo.objects.get(aid=8)
    print(author_obj)
    #查询该作者的所有书
    authors_books = author_obj.author_book_publish.all()
    print(authors_books)
    #给该作者添加一本书
    #create（）方法
    author_obj.author_book_publish.create(bname = 'mini高级攻略',book_pubish_id = 9)









