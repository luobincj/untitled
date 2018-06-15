#正则表达式，正则，对字符串的操作
#元字符 ?  *  $  ^ + { }  [ ]  ( )  \

import re
#！！！！！[ ]内不需要使用逗号隔开
# ret=re.split('[j,s]','ajksal')
# print(ret)  #['a', 'k', 'al']

# ret=re.split('[s,j]','ajksal')
# print(ret) #['a', 'k', 'al']

# ret=re.split('[sj]','ajksal')
# print(ret) #['a', 'k', 'al']

# ret=re.split('[s,j]','ajksa,l')
# print(ret) #['a', 'k', 'a', 'l']

# ret=re.split('[sj]','ajksa,l')
# print(ret) #['a', 'k', 'a,l']

# q1=re.compile('a..x')     #将规则a..x定义为一个对象，后面可以调用
# ret=q1.sub('b.....x','dfjeowjfoewalexfjweofkwne')
# print(ret)

# ret=re.search('(?P<name>\w{3})/(?P<age>\d{2})','sdnfdnen/32fnenfa.c.eifnwal')     #给规则\w{3}命名为name,给规则\d{2}命名为age
# print(ret.group())      #nen/32
# print(ret.group('name'))    #nen
# print(ret.group('age'))     #nen

# ret1=re.findall('www.(\w+).com','www.baidu.com')        #findall在提取时，如果有元组的规则(),则在返回结果时只返回元组规则内容
# print(ret1)     #['baidu']
# ret2=re.findall('www.(?:\w+).com','www.sohu.com')       # 括号内?: 取消了()的优先
# print(ret2)     #['www.sohu.com']

# ret=re.finditer('\d','dfew2jkgn4kljgn5452ngjew23')      #去出所有结果，将其封装成一个迭代器
# ret2=re.findall('\d','dfew2jkgn4kljgn5452ngjew23')      #去出所有结果，将结果封装成一个列表
# print(ret)      #<callable_iterator object at 0x000001EE77E9C6D8>
# print(next(ret))        #<_sre.SRE_Match object; span=(4, 5), match='2'>
# print(next(ret).group())        #4
# print(ret2)     #['2', '4', '5', '4', '5', '2', '2', '3']

# regular='\-?\d+\.?\d*[*/]\-?\d+\.?\d*'
# string='3+4.2*3-4.4/2'
# while re.search(regular,string):
#     expression = re.search(regular,string).group()
#     print(expression)
# # expressions = re.findall(regular,string)
# # print(expressions)
# # for i in re.findall(regular,string):
# #     exprssion = re.search(regular,i).group()
# #     print(exprssion)

aclStr = '2+5*-3.1*(10+5/(17-(8+9)))'
ret = re.search('\([^()]*\)',aclStr).group()
print(ret)