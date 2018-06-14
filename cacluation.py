#实现输入一串公式计算四则运算的计算器
#   2+4*(2+6*5/(5+2)+12/6-3*3)-5*6

import re

#完成字符串的校验，四则的是否合法
def checkOut(expression_string):
    checkOut_flag=True
    #左右括号数量是否相等
    if not expression_string.count('(')==expression_string.count(')'):
        print('inavaild.error!')
        checkOut_flag=False
    #表达式中是否含有字母
    if re.findall('[a-zA-Z]',expression_string):
        print('inavaild.error!')
        checkOut_flag=False
    #表达式中除了数字和加减乘除外含有其他特殊字符？？？或汉字（\u4e00-\u9fa5）的
    if re.findall('[\u4e00-\u9fa5]',expression_string):
        print('inavaild.error!')
        checkOut_flag = False
    return checkOut_flag

#将可简化的字符串进行规范化
def formatStr(s):
    s = s.replace('--','+')
    s = s.replace('-+','-')
    s = s.replace('+-', '-')
    s = s.replace('++', '+')
    s = s.replace('*+', '*')
    s = s.replace('/+', '/')
    s = s.replace(' ', '')
    return s
#完成加减
def calAddDev(s):
    pass
#完成乘除
def calMulDev(s):
    pass

if __name__ == '__main__':
    caclStr = '2*-3.1吗'
    if checkOut(caclStr):
        newStr=formatStr(caclStr)
        print(caclStr)
        print(newStr)