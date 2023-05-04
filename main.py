import time

time.perf_counter()

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

a = int(input("Введите число: "))
print("Число раскладывается на простые делители: ")
print(primfacs(a))
print("Время работы программы: ")
print(time.process_time())
