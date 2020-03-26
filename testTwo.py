a = "Hello, World!"
x = "el" in a
y = 4+6j
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(a[2]+a[5])
print(a[2:6])
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("W","J"))
print(a.split(","))
print(x)
print(y)
print(type(y))
print(fruits[2])
print(fruits[0:2])

for x in fruits:
    print(x)

if "apples" in fruits:
  print("\nYes, 'apple' is in the fruits list") 

print(fruits[2:5])
