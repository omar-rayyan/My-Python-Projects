# 1
def a():
    return 5

print(a())  # 5

# 2
def a():
    return 5

print(a() + a())  # 10

# 3
def a():
    return 5
    return 10

print(a())  # 5

# 4
def a():
    return 5

print(10) # 10
print(a()) # 5

# 5
def a():
    print(5) # 5

x = a()
print(x)  # None

# 6
def a(b, c):
    print(b + c) # 3, 5

print(a(1, 2) + a(2, 3))  # None

# 7
def a(b, c):
    return str(b) + str(c)

print(a(2, 5))  # 25

# 8
def a():
    b = 100
    print(b) # 100
    if b < 10:
        return 5
    else:
        return 10
    return 7

print(a())  # 10

# 9
def a(b, c):
    if b < c:
        return 7
    else:
        return 14

return 3  # This line will cause an error due to incorrect placement
# Therefore, all code below won't run.
print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3)) 

# 10
def a(b, c):
    return b + c
    return 10

print(a(3, 5))  # 8

# 11
b = 500
print(b) # 500

def a():
    b = 300
    print(b)

print(b) # 500
a()
print(b) # 300 

# 12
b = 500
print(b) # 500

def a():
    b = 300
    print(b)
    return b

print(b) # 500
a()
print(b)  # 300

# 13
b = 500
print(b) # 500

def a():
    b = 300
    print(b)
    return b

print(b) # 500
b = a()
print(b) # 300

# 14
def a():
    print(1) # 1
    b()
    print(2) # 2

def b():
    print(3) # 3

a()  

# 15
def a():
    print(1) # 1
    x = b()
    print(x) # 5
    return 10

def b():
    print(3) # 3
    return 5

y = a()
print(y)  # 10
