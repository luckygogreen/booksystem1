import json

kkk = '{"user":"kevin","age":18}' # 定义一个字符串  ，内部必须是双引号，不然json报错
# 把字符串反序列为Python中的数据类型
rs = json.loads(kkk)
print(rs,type(rs))
#把字典类型转化成为Python中的字符串
re = json.dumps(rs)
print(re,type(re))

