#Задача №1_____________________________________________________

N = int(input("Введите число: "))

def Get_factorial(n):
    f = 1
    list = []
    for i in range(1, n+1):
        f = f*i
        list.append(f)
    return list 

print(Get_factorial(N))
