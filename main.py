#1
a = int(input())
b = int(input())
if a < b:
     print(a)
else:
     print(b)
#2
x = int(input(''))
if x>0:
    print('sign(x)=1')
elif x<0:
    print('sign(x)=-1')
else:
    print('sign(x)=0')
#3
x1 = int(input("Введите номер столбца для первой клетки (от 1 до 8): "))
y1 = int(input("Введите номер строки для первой клетки (от 1 до 8): "))
x2 = int(input("Введите номер столбца для второй клетки (от 1 до 8): "))
y2 = int(input("Введите номер строки для второй клетки (от 1 до 8): "))
first = (x1 + y1) % 2
second = (x2 + y2) % 2

