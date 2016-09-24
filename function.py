# function 
def my_fun(x):
	if x > 60:
		return 'ok'
	else:
		return 'no'

print my_fun(55)
print my_fun(80)


def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

print fact(1)
print fact(5)   # 5*fact(4) => 5*(4*fact(3)) => 5*(4*(3*fact(2))) => 5*(4*3*(2*fact(1)))
				# =>5*(4*(3*(2*1)))
print fact(100)

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x, y


