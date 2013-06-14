#coding:utf8
a = reduce(lambda x, y:x * y, range(1, 10))

print(a)

def factorial(x, y):
    return x * y

print(reduce(factorial, range(1, 20)))#19的阶乘

a = [1, 2, 3]
a.append(a)
print(a)
