class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self,name):
		self.__name = name

	def set_score(self,score):
		if(0 <= score <= 100):
			self.__score = score
		else:
			return ValueError('bad score')

	def print_score(self):
		print 'name is ',self.__name,'score is ',self.__score

	def get_grade(self):
		if self.__score > 60:
			return 'ok'
		else:
			return 'no'

class MidStudent(Student):
	def play_computer(self):
		print self.get_name(),'age 18 paly_computer'


stu = Student('zhangsan','85')
stu.print_score()
print stu.get_grade()
print stu.get_name()

mid_stu = MidStudent('lisi',56)
mid_stu.play_computer()
print mid_stu.get_grade()

#type  isinstance  dir

print isinstance(stu,Student)
print isinstance(stu,MidStudent)

print dir(stu)