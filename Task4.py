#Задача №4_____________________________________________________

def List_1(number):
    l = []
    for n in range(-number, number+1):
        l.append(n)
    return l

def List_2(a):
    j = 0
    NUMBER_POSITIONS = 2
    while j < NUMBER_POSITIONS:
        length = len(a)
        x = a[length-1]
        for i in range(length-1, -1,-1):
            a[i] = a[i-1]
        a[0] = x
        j += 1
    return a

N = int(input("Введите число: "))

list = List_1(N)
list_2 = List_2(list)
print(list_2)
