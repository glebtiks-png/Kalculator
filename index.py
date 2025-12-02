x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))
a = (input("Оберіть операцію: "))
if a == "+":
    print(x + y)
elif a == "/":
    print(x / y)
elif a == "-":
    print(x - y)
elif a == "*":
    print(x * y)
else:
    print("Error")