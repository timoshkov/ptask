
first_number = int(input())
second_number = first_number + 1
third_number = first_number + 2
print (first_number)
print (second_number)
print (third_number)

a = int(input())
b = int(input())
c = int(input())

sum = a + b + c

print(sum)

leight = int(input())
Обьем= leight ** 3
Площадь_поверхности = 6 * (leight ** 2)
print("Обьем куба:", Обьем)
print("Полная площадь поверхности:", Площадь_поверхности)

a = int(input ("Введите первое число: "))
b = int(input("Введите второе число: "))
f = 3*(a + b)**3 + 275*b**2 -127*a - 41
print (f)

a = int(input("Введите число: "))
f = a+1
n = a-1
print(f"Следущее за числом {a} число: {f}")
print(f"Предыдущее для числа {a} число:{n}")

a = int(input ("Стоимость монитора: "))
b = int(input ("Стоимость системного блока: "))
c = int(input ("Стоимость клавиатур: "))
d = int(input ("Стоимость мыши: "))
sum = int(a+b+c+d)*3
print ("Стоимость трех компьютеров =", sum)

a_1 = int(input())
d = int(input())
n = int(input())
a_n = a_1 + d*(n-1)
print (a_n)

x1 = int(input())
x2 = x1 * 2
x3 = x2 + x1
x4 = x3 + x1
x5 = x4 + x1
print(x1,x2,x3,x4,x5, sep='---')

n = int(input("школьники: "))
k = int(input("мандаринки: "))
a = n // k
basket = n % k
print ("Количество мандаринок у каждого школьникa - ",a)
print ("Остаточное оличество мандаринок в корзине - ",basket)

a=int(input())
print(a//2 + a%2)

m = int(input())
h = m // 60
s = m % 60
print(m, "минута это - ", h, "часов", s, "минут.")

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма чисел =", c + b + a)
print(c * b * a)

pinguin = input()
print('    _~_    ' *int(pinguin))
print('   (o o)   ' *int(pinguin))
print('  /  V  \  ' *int(pinguin))
print(' /(  _  )\ ' *int(pinguin))
print('   ^^ ^^   ' *int(pinguin))

abc = int(input())
x = 1
equ = (x // 10 ** k) % 10
print(n)

a = int(input("Первое число уравнения "))
h = a % (60 * 24) // 60
m = a % 60
print(h, m)

a = int(input("Вставьте число"))
print(1 - a)

a = int(input())
print((a//2+1)*2)

v = int(input())
t = int(input())
a = v * t
n = a // 109
print(-(109 * n - a))

a = float(input())
b = float(input())
c = float(input())
print(int(1 + (a - c - 1) / (b - c)))

