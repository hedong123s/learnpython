#!/usr/bin/python

print 'hello, world.'
print 'hello world'
print 'hello','what is you'
print '100+200=',100+200
name = raw_input('please enter your name')
print 'hello,',name

#---------u'华丽分割线'--------------------#
a = 100 
if a>60:
	print 'ok'
else:
	print 'no'

print ord('A')
print chr(65)
print u'中文测试'


# ------------ list ------------- #
classmates = ['zhangsan','lisi','wangwu']
print classmates
c_len = len(classmates)
print c_len

print classmates[0]
print classmates[1]
print classmates[-1]  #last

print classmates.append('zhaoliu')
print classmates

classmates.insert(1,'jack')
print classmates 

classmates.pop()  #delete lase
classmates.pop(1) #delete 1

classmates[1] = 'tihuan'
print classmates

for name in classmates:
	print name

s = ['ipod','iphone',['iphoen6','iphoen8','iphoen9']]
for i in s:
	print i

print s
print len(s)

# ------------ tuple -----------------#  no change
t = (666,777,888)
t_one = (1,)


#------------------u'遍历'----------------#

total = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	total = total + x
print total

print range(101)

total = 0
for y in range(101):
	total = total + y
	#print y
print total   #5050

total = 0
n = 100
while n>0:
	total = total + n
	n = n -1
print total    #5050


birth = raw_input()
birth = int(raw_input())