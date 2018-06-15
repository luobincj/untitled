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
    #表达式中汉字（\u4e00-\u9fa5）的
    if re.findall('[\u4e00-\u9fa5]',expression_string):
        print('inavaild.error!')
        checkOut_flag = False
    #如果除数为0
    if re.findall('(/0)+',expression_string):
        print('Error dev number 0!, No result!')
        checkOut_flag = False
    #除了数字和加减乘除外含有其他特殊字符？？？的
    #if re.findall('',expression_string)：
    # print('inavaild.error!')
    # checkOut_flag = False
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
def calAddSub(s):
    #设计规则，加法匹配规则，减法匹配规则
    add_regular = '\-?\d+\.?\d*[+]\-?\d+\.?\d*'
    sub_regular = '\-?\d+\.?\d*\-\-?\d+\.?\d*'
    #获取表达式，该式子中已经不存在乘除，仅有加减运算
    #开始加法运算
    while re.findall(add_regular,s):
        #获取所有加法运算
        add_list = re.findall(add_regular,s)
        for add_str in add_list:
            x,y = add_str.split('+')
            add_result = '+'+str(float(x)+float(y))
            s = s.replace(add_str,add_result)
            s=formatStr(s)
    #开始减法
    while re.findall(sub_regular,s):
        #获取所有减法运算
        sub_list = re.findall(sub_regular,s)
        for sub_str in sub_list:
            #按照 - 符号分解元式
            special_sub = sub_str.split('-')
            # 如果出现  -3-6
            if len(special_sub) == 3:
                for i in special_sub:
                    result = 0
                    if i:
                        result -= float(i)
            else:
                x,y = special_sub
                result = float(x)-float(y)
            s = s.replace(sub_str,'+'+str(result))      #*****!!!!
            s = formatStr(s)
    return s

#完成乘除
def calMulDev(formated_string):
    #设计规则,按照乘除符号匹配两边的数字，包括小数数字
    regular='\-?\d+\.?\d*[*/]\-?\d+\.?\d*'
    #如果是多个乘除又加减符号链接的表达式，则需要循环迭代出所有的无括号的乘除项
    while re.search(regular,formated_string):       #第一次2*-3.1  第二次-6.2*10/4    第三次-62/4
        #获取表达式
        expression = re.search(regular,formated_string).group()     #第一次2*-3.1  （*10/4      第二次-6.2*10   （/4
        if formatStr(expression) :
            if expression.count('*')==1:
                x,y = expression.split('*')     #   2    -3.1    #-6.2  10
                mul_result = str(float(x)*float(y))     #-6.2
                formated_string = formated_string.replace(expression,mul_result)    #-6.2*10/4  #-62/4
                formated_string = formatStr(formated_string)    #-6.2*10/4  #-62/4
            if expression.count('/')==1 and not re.findall('[/0]+',expression):    #第三次 -62/4
                x,y = expression.split('/')     #-62  4
                mul_result = str(float(x)/float(y))      #-62
                formated_string = formated_string.replace(expression,mul_result)         #-15.5
                formated_string = formatStr(formated_string)        #-15.5
            else:
                break
    return formated_string

if __name__ == '__main__':
    caclStr = '2+5*-3.1*(10+5/(2+(8-5+4-9)))'
    if checkOut(caclStr):
        while caclStr.count('(')>0:
            strs = re.search('\([^()]*\)',caclStr).group()        #(8+9)
            newstrs = calMulDev(strs)
            newstrs = calAddSub(newstrs)
            caclStr = formatStr(caclStr.replace(strs,newstrs[1:-1]))
        else:
            newStr = formatStr(caclStr)
            newStr = calMulDev(newStr)
            newStr = calAddSub(newStr)
        print(caclStr)
        print(newStr)