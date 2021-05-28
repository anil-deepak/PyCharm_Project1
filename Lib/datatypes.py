print("NUMERIC TYPES")
#int
a=10
print(type(a))

#float
b=2.4
print(type(b))

#complex
c=2+3j
print(type(c))
#end of numeric types

print()
print("TEXT TYPES")
name="Anil Deepak"
print(type(name))

print()
print("SEQUENCE TYPES")
li=[10,20,30]
print(type(li))
tup=(11,22)
print(type(tup))
print(type(range(10)))

print()
print("MAPPING TYPES")
Dict={"name":"Anil","age":24,"status":"Online"}
print(type(Dict))

print()
print("SET TYPES")
s={"anil",24}
print(type(s))
x=frozenset({"apple","banana",10,20})
print(type(x))

print()
print("BOOLEAN")
ins=True
print(type(ins))

print()
print("BINARY TYPES")
x=10
print(type(b"x"))
print(type(bytearray(x)))
print(type(memoryview(bytes(x))))