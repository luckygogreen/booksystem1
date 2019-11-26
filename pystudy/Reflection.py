import sys
resys = sys.modules[__name__]  #系统里面的一个modulesde包，[__name__] 表示当前文件

class Person(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('{}在吃{}'.format(self.name,food))

    def dream(self):
        print('{}在做好梦'.format(self.name))



str = 'person'
s = str.capitalize() # 首字母大写函数
print(s)
print(locals())
#反射的重要使用
if hasattr(resys,s):  #判断本地声明的类，函数和变量中是否有s
    strclass = getattr(resys,s) #如果有s这个变量对应的值，把它反色成对应的函数，类或变量
    #obj = strclass(name = 'Kevin') #调用类，并且把Name传给类    这种方法和下面的给类传参数的方法同等作，
    obj = strclass('Kevin') #调用类，并且把Name传给类   这种方法和上面的给类传参数的方法同等作，

    obj.eat('Pizza') #调用类里的方法，这里打点事出不来方法的，
    obj.dream()  #此处调用方法即使没有参数也要有括号，否则不会作为方法被调用
    print('-'*100)
    print(s,type(s))
    print(strclass,type(strclass))
    print(resys,type(resys))

#用来展示Locals函数的作用，列出所有声明的变量，函数和类
def num():
    a = 1
    b = 2
    c = 3
    print(a,b,c)
    print(locals())  #答应该方法下的所有变量，函数和类，并且生产字典
num()