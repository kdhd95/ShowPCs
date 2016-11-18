'''
def num (num1):
    if num1.isdigit():
        if int(num1)<100000 and int(num1)>=10000:
            print num1
            for i in num1:
                print i,
            print
            aa=0
            for i in num1:
                aa+=int(i)
            print aa
        else:
            num(raw_input('please enter a 5 digit number'))
    else:
        num(raw_input('please enter a 5 digit number'))       
num(raw_input('please enter a 5 digit number'))
'''
'''
def digit (b):
    aa=0
    for i in b:
        aa+=int(i)
    print aa    
def lisum (a):
    if a.isdigit():
        digit(a)
    elif a.isalpha():
        print a
    else:
        lisum(raw_input())    
lisum(raw_input('a'))
'''
import sys
def last (b):
    return b[-1]

a=sys.args
b=a[1:]
print sorted(b,key=last)
