import sys
a=[1,2,3]
b=a
print(sys.getrefcount(a))
print(sys.getrefcount(b))