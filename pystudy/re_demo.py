import re

r_str = re.compile(r'^([a-zA-Z]+)/(\d+)/$') #编译一个正则表达式 ，r'^为正则表达式的开头,/$为表达式的结尾，([a-zA-Z]+) 字母组合，(\d+)数字组合，括号表示分组
ret = r_str.match("delete/11/") #判断一个字符串是否满足r'^([a-zA-Z]+)/(\d+)/$'的要求，返回None或者<re.Match object; span=(0, 10), match='delete/11/'>
print(ret)
print(ret.groups())  #返回一个数组，('delete', '11')
print(ret.group())   #返回一个路径  delete/11/
print(ret.group(1))   #返回路径的第N个元素，1代表第一个元素