import os
#如果需要在一个单独的PY脚本文件中导入Django模块，下面是固定代码 booksystem1 是你的项目名，bookAPP是你的settings.py所在文件夹名
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksystem1.settings")
    import django
    django.setup()
    from bookAPP import models  #此处导入，必须在判断体内，如果在判断体外会报错
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


















