# is v.s ==
# 'is' is for reference equality. Use it when you would like to know if two references refer to the same object.
# '==' is  for value equality. Use it when you would like to know if two objects have the same value.

'''
(1)
>>> a = 500
>>> b = 500
>>> a == b
True
>>> a is b
False

(2)
>>> c = 200
>>> d = 200
>>> c == d
True
>>> c is d
True

Python caches integer objects in the range -5~256 as singleton instances for performance reasons.
'''

# return an inner function with an outer function
'''
def add(n1):
    def func(n2):
        return n1 + n2
    return func

print(add(1)(2))  # output 3
'''

# lamda (anonymous function)
'''
max = lambda m, n: m if m > n else n
print(max(10, 3))  # output 10
'''
