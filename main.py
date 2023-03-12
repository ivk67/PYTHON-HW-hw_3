
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
# s = (m + (n - 1)) // n
# print(s)


# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# class_1 = int(input('1--> '))
# class_2 = int(input('2--> '))
# class_3 = int(input('3--> '))
# class_1 += 1
# class_2 += 1
# class_3 += 1
# print(f'Нам нужно парт: {(class_1//2) + (class_2//2) + (class_3//2)}')


# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии 
# с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, 
# а также если он кратен 400.
# Input: 2016
# Output: YES

# year = int(input())
# if ((year%4==0 and year%100!=0) or year%400==0):
#     print("YES")
# else:
#     print("NO")

# # or

# year = int(input())
# print('YES') if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) else print("NO")


# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * 
# N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int(input('n неотрицательное число '))
# fact = 1
# while n > 1:
#     fact *= n
#     n -= 1
# print(fact)


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно 
# является, то есть выведите такое число n, что φ(n)=A. Если А не является числом
# Фибоначчи, выведите число -1.
# Input:   5
# Output:  6

# A=int(input('Enter A: '))
# x=x1=1
# s=0
# while x1<A+2:
#   b=x
#   x=x1
#   x1+=b
#   s+=1
# if s < A:
#     print(s)
# else : print(-1)

# a = int(input('Enter A: '))
# if a == 0:
#     print(0)
# else:
#     fib_prev, fib_next = 0, 1
#     n = 1
#     while fib_next <= a:
#         if fib_next == a:
#             print(n)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(-1)

# OR

# A = int(input())
# num_1, num_2, n = 0, 1, 2

# while num_2 < A:
#     num_1, num_2 = num_2, num_1 + num_2
#     n += 1

# print(n) if num_2 == A else print(-1)


# days_count = int(input())
# len_plus_days = 0
# max_len_plus_days = 0
# days = []

# for i in range(days_count):
#     day = int(input(f'day_{i}--> '))
#     days.append(day)

# print(days)

# for day in days:
#     if day > 0:
#         len_plus_days += 1
#     else:
#         if len_plus_days > max_len_plus_days:
#             max_len_plus_days = len_plus_days
#         len_plus_days = 0
    
# print(max_len_plus_days)

N = int(input('Введите количество монет: '))
orel = reshka = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print(f'Переверните {reshka} монет с решки на орла, их меньше всего')