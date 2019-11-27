import os
#如果需要在一个单独的PY脚本文件中导入Django模块，下面是固定代码 booksystem1 是你的项目名，bookAPP是你的settings.py所在文件夹名
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksystem1.settings")
    import django
    django.setup()
    from bookAPP import models  #此处导入，必须在django.setup()后，因为只有启动Django才能执行，否则会报错


#查询的用法
    # print('⬇ ️all()取所有️')
    # print(models.publishinfo.objects.all())  #查询打印所有的出版社
    # print('⬇ filter()取数据️')
    # print(models.publishinfo.objects.filter(pid=1)) #用filter查询如果没有，则返回空
    # print('⬇ ️filter()[0]取数据，取第一个元素')
    # print(models.publishinfo.objects.filter(pid=1)[0]) #用filter查询如果没有，则返回空,0是去第一个元素，去到的是具体对象内容
    # print('⬇ get()取数据')
    # print(models.publishinfo.objects.get(pid=1)) #用get查询如果没有，则报错 #matching query does not exist.
    # print('⬇ exclude()取数据')
    # print(models.publishinfo.objects.exclude(pid=1)[0]) # 排除赛选的值，取其他的值[0]第一个元素
    # print('values取指定列字段'.center(30,'⬇'))
    # print(models.publishinfo.objects.values('pname')) #返回指定列的一个字典
    # print('values取所有字段'.center(30, '⬇'))
    # print(models.publishinfo.objects.values()) #返回全部列的字段
    # print('values_list 取所有字段'.center(30, '⬇'))
    # print(models.publishinfo.objects.values_list()) # 返回一个元祖
    # print('values_list 取指定字段'.center(30, '⬇'))
    # print(models.publishinfo.objects.values_list('pname'))  # 返回一个元祖
    # print('order_by 排序取数据'.center(30, '⬇'))
    # print(models.publishinfo.objects.order_by('pname')) #根据指定字段排序 # 如果不给字段，则按照Model定义的Meta原则排序
    # print('reverse 反向排序取数据'.center(30, '⬇'))
    # print(models.publishinfo.objects.order_by('pname').reverse()) #reverse 只能对有序排序的结果排序，例如Meta定义好的，或者是想这样先order_by在reverse排序的
    # print('count 计算返回值的数量'.center(30, '⬇'))
    # print(models.publishinfo.objects.count()) # 返回这个数据的个数，可以理解表数据的行数
    # print('first 取首个数据'.center(30, '⬇'))
    # print(models.publishinfo.objects.first()) #返回第一条记录
    # print('last 取尾个数据'.center(30, '⬇'))
    # print(models.publishinfo.objects.last()) #返回最后一条记录
    # print('exists 判断是否为空表'.center(30, '⬇'))
    # print(models.publishinfo.objects.exists()) #判断是否为空表，返回一个Ture或False的布尔值
    # print('pid__gt 大于，pid__lt小于'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pid__gt=1,pid__lt=6)) #查询id 大于1小于6的数据
    # print('pid__in 取指定内容的值'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pid__in=[1,3,5,7,9])) # 取出ID为 1，3，5，7，9的值
    # print('pname__contains 模糊查询区分大小写'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pname__contains='A')) # 模糊查询区分大小写
    # print('pname__icontains 模糊查询不区分大小写'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pname__icontains='A')) #模糊查询不区分大小写
    # print('pid__range 范围区间取值'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pid__range=[1,8])) #取ID范围是1-8之间的值
    # print('pname__startswith和istartswith 匹配开始取值'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pname__startswith='a')) #取a开头的数据，区分大小写
    # print(models.publishinfo.objects.filter(pname__istartswith='a')) #取a开头的数据，不区分大小写
    # print('pname__endswith和iendswith 匹配末尾取值'.center(30, '⬇'))
    # print(models.publishinfo.objects.filter(pname__endswith='R')) #取R结尾的数据，区分大小写
    # print(models.publishinfo.objects.filter(pname__iendswith='R')) #取R结尾的数据，不区分大小写
    # date字段还可以：
    # models.Class.objects.filter(first_day__year=2017) #还有字段__year
    #print('*'*100)
    print('查询的用法')

#外键表的查询,主键到外键教做正向查询，外检表到主键表叫反向查询 #基于对象查询
    # res = models.bookinfo.objects.first()
    # re = res.book_pubish
    # r = res.book_pubish.pname
    # print(res,type(res))
    # print(re,type(re))
    # print(r,type(r))
    print('外键表的查询,主键到外键教做正向查询，外检表到主键表叫反向查询 #基于对象查询')

#基于双下划线查找方法
    # result = models.bookinfo.objects.filter(bid=3).values('book_pubish__pname')
    # print(result,type(result))
    print('基于双下划线查找方法')

#外键表的查询,主键到外键教做反向查询，外检表到主键表叫反向查询 #基于对象查询
#     publish_object = models.publishinfo.objects.first()
#     reverse_result = publish_object.bookinfo_set.all() #如果Class model中没有定义related_name ,则需要这样查找
    #reverse_result = publish_object.books.all() ##如果Class model中定义了related_name ,就可以直接用定义的名字查
    # print('*'*100)
    # print(reverse_result)
    # print(reverse_result[0])
    print('外键表的查询,主键到外键教做反向查询，外检表到主键表叫反向查询 #基于对象查询')

#双下划线查找方法 #基于双下划线查询
    # reverse_result = models.publishinfo.objects.filter(pid=1).values_list('bookinfo__bname')
    #reverse_result = models.publishinfo.objects.filter(pid=1).values_list('books__bname') #如果Class model中定义了related_query_name='xxoo'
    #reverse_result = models.publishinfo.objects.filter(pid=1).values_list('xxoo__bname') #如果Class model中定义了related_query_name='xxoo'
    # print(reverse_result[0])
    print('双下划线查找方法 #基于双下划线查询')

#多对多查询
#create() 创建新数据
    # print('*'*100)
    #查询第一个作者
    # author_obj = models.authorinfo.objects.get(aid=7) # 用get取得到的是一个authorinfo的对象
    # print(author_obj,type(author_obj)) # Mini <class 'bookAPP.models.authorinfo'>

    #下面的代码其实做了两部操作，第一在Book表里面创建一本书，第二个操作是对对联的表创建一条关联数据（就是 bookAPP_authorinfo_author_book_publish 这个表）
    # author_obj.author_book_publish.create(bname='第二次世界大战图解',book_pubish_id=9) # author_obj这个对象是 authorinfo 表，对authorinfo表的author_book_publish字段（因为是对应的bookinfo表manytomany关系），所以还需要给bookinfo表的book_pubish_id 一个值，这个字段，只有数据库有，modelclass对应的是book_pubish，后面的_id是自动生成的

    # author_first = models.authorinfo.objects.last() #返回的同样是一个对象，只有filter返回的是一个数据集合
    # print(author_first,type(author_first))
    # author_queryset = models.authorinfo.objects.filter(aid=8) # 用filter得到的是一个QuerySet（从数据库中查询出来的一个结果，理解为集合）
    # print(author_queryset,type(author_queryset)) # <QuerySet [<authorinfo: Mini>]> <class 'django.db.models.query.QuerySet'>

    # #查询该作者的所有书
    # authors_books = author_obj.author_book_publish.all()# 取出来的也是一个queryset的集合
    # print(authors_books,type(authors_books)) # <QuerySet [<bookinfo: mini自传>, <bookinfo: mini高级攻略>]> <class 'django.db.models.query.QuerySet'>
    # # #给该作者添加一本书
    # #create（）方法
#add 关联已有数据
    # getbooks_obj = models.bookinfo.objects.filter(bid__gt=9)
    # print(getbooks_obj)  # 返回的是Queryset集合的数据 <QuerySet [<bookinfo: mini自传>, <bookinfo: mini高级攻略>, <bookinfo: 第二次世界大战图解>]>
    # print(*getbooks_obj) # 加*代表把Queryset集合的数据，全部打散成对象，这里是字符串  mini自传 mini高级攻略 第二次世界大战图解
    # models.authorinfo.objects.get(aid=7).author_book_publish.add(*getbooks_obj)
    # models.authorinfo.objects.get(aid=8).author_book_publish.add(3)
    # models.authorinfo.objects.get(aid=8).author_book_publish.add(*getbooks_obj2)
    print('create() 创建新数据')

#remove（）删除已有数据
    # getbooks_obj2 = models.bookinfo.objects.get(bname='Python 300') # get 返回数据集对象，不需要打散
    # getbooks_obj2 = models.bookinfo.objects.filter(bname='Python 300') # filter返回数据集，添加时候需要打散
    # models.authorinfo.objects.get(aid=8).author_book_publish.remove(*getbooks_obj2)
    print('remove（）删除已有数据')

#clear（）清空指定数据
    # getauthorid = models.authorinfo.objects.get(aid=7)  #取出要清空的作者ID
    # getauthorid.author_book_publish.clear()  #清空该作者的所有书
    print('clear（）清空指定数据')


#ORM聚合和分组





