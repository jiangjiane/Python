#!usr/bin/env python3
#_*_coding:utf-8_*__

name=input('please enter your name:')
h=int(input('please enter your grade Height(cm):'))
w=int(input('please enter your grade Weight(kg):'))
h1=h/100
b1=h1*h1
b2=w/b1
print('bmi=%.2f'%b2)
if b2<18.5:
	print('hello,%s,your Height is:%s,your Weight is:%s,BMI:%.2f,so light'%(name,h,w,b2))_
	elif b2<25:
		print('hello,%s,your Height is:%s,your Weight is:%s,BMI:%.2f,so nomal'%(name,h,w,b2))_
	elif b2<28:
		print('hello,%s,your Height is:%s,your Weight is:%s,BMI:%.2f,so strong'%(name,h,w,b2))_
	elif b2<32:
		print('hello,%s,your Height is:%s,your Weight is:%s,BMI:%.2f,so obesity'%(name,h,w,b2))_
	else:
		print('hello,%s,your Height is:%s,your Weight is:%s,BMI:%.2f,so obesitiest'%(name,h,w,b2))_
