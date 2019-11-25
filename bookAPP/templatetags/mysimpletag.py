from django import template
register = template.Library()  #  注意导入的Libraryi一定是首字母大写的
@register.simple_tag(name = 'getsum')
def first_simpletag(arg1,arg2,agr3):
    sum = arg1+arg2+agr3
    return sum


