import functools

numbers = [10, 20, 30, 40, 50, 60, 70]
res = functools.reduce(lambda  a, b: a + b,numbers)
print  (res)
res = functools.reduce(lambda  a, b: a * b,numbers)
print  (res)
res = functools.reduce(lambda  a, b: a / b,numbers)
print  (res)
res = functools.reduce(lambda  a, b: a - b,numbers)
print  (res)