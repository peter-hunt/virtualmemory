from __init__ import *

print(true)
print(false)

a = ByteUnit(false, true, false, true, false, false, false, false)
b = ByteUnit(80)
print(a)
print(b.copy())
print(a == b)

print(null)

c = Bytes((80, 101, 116, 101, 114))
print(c.copy())

d = Bytes((80, 101, 116, 101, 114, 72, 117, 110, 116))
print(d.copy())

print(a in c)
print(80 in d)
print(c in d)
print(Bytes((72, 117, 110, 116)) in d)
