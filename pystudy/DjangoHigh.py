import os
#如果需要在一个单独的PY脚本文件中导入Django模块，下面是固定代码 booksystem1 是你的项目名，bookAPP是你的settings.py所在文件夹名

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksystem.settings")
    import django
    django.setup()
    from django.db.models import F,Q
    # 此处导入，必须在django.setup()后，因为只有启动Django才能执行，否则会报错


    # ORM多对多查询的三种方法 # 例如第一个作者有那些书
    # 第一种，查询原始表 直接用 manytomany 建立好的表，查询
    # 如果第三张关联表，没有额外的字段时，使用该种方法建表
    from bookAPP import models
    rs = models.authorinfo.objects.get(aid=1).author_book_publish.all()
    print('第一种方法:',*rs)
    # 如果需要删除第一本书
    # models.authorinfo.objects.get(aid=1).author_book_publish.remove(1) # 1 是书的id值

    # 第二种，查询app02中的表 ,没有 manytomany 关系的原始查询方式,自己创建第三章关联表 # app02/models.py
    from app02 import models
    rs = models.authors_books.objects.filter(authorsid=1).values_list('booksid')
    # print(rs) #<QuerySet [(1,), (2,), (3,)]>
    rs = [i[0] for i in rs]
    # print(rs) #[1, 2, 3]
    rs = models.bookinfo.objects.filter(bid__in=rs)
    print('第二种方法:',*rs) #科技指南 生物指南 化学指南

    # 第三种，查询app03中的表 ,自己创建 manytomany 关系 用于查询 # app03/models.py
    # 如果第三张关联表，有额外的其他字段，就使用该方法
    # 例如关联表 字段为ID，bookid,authorid   date(此处date就是额外字段)
    # 第三种没有Django封装的ORM操作方法了，例如，add,remove等，只能用python发放
    from app03 import models
    rs = models.authorinfo.objects.get(aid=1).boos.all()
    print('第三种方法:', *rs)
    #删除第一个作者的第一本书
    # models.authors_books.objects.get(authorsid=1,booksid=1).delete()