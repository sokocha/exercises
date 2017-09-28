EXAMPLE 1
def f():
  print(s)
s="Andrew was beautiful"
f()

EXAMPLE 2
def f():
  s="Andrew was beautiful"
  print(s)

s="Andrew was beautiful"
f()
print(s)

EXAMPLE 3
def f():
  global s
  print(s)
  s = "dfsfsdfsfs"

  print(s)
s="andre cleaned this"
f()
print(s)