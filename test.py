from __init__ import *

# bits
print(f'{true = }')
print(f'{false = }')
print('\n')

# byte units
a = ByteUnit(false, true, false, true, false, false, false, false)
b = ByteUnit(80)
print(f'{a = }')
print(f'{b.copy() = }')
print(f'{(a == b) = }')
print()

print(f'{a.to_str() = }')
print(f'{b.to_mem() = }')
print(f'{b.to_int() = }')
print('\n')

# bytes
c = Bytes((80, 101, 116, 101, 114))
print(f'{c = }')

d = Bytes((80, 101, 116, 101, 114, 72, 117, 110, 116))
print(f'{d.copy() = }')
print()

print(f'{c.to_str() = }')
print(f'{d.to_mem() = }')
print()

print(f'{(a in c) = }')
print(f'{(80 in d) = }')
print(f'{(c in d) = }')
print(f'{(Bytes((72, 117, 110, 116)) in d) = }')
print(f"{c.count(ByteUnit(80)) = }")
print(f'{d.count(101) = }')
print('\n')

# character
e = Char(-48)
print(f'{e = }')
print(f'{e.to_str() = }')
print(f'{e.to_mem() = }')
print(f'{e.to_int() = }')
print()

print(f'{null = }')
print()

f = UnsignedChar(80)
print(f'{f = }')
print(f'{f.to_str() = }')
print(f'{f.to_mem() = }')
print(f'{f.to_int() = }')
print()

print(f'{e + f = }')
