#Задача №3_____________________________________________________

def Repetition_check(a): # Проверка на наличие повторяющихся символов
    string = a           # в одной строке и объединение их
    seen = ""
    list =[]
    for i in string:
        if i not in seen:
            list.append(i)
            seen += i
    return list
            
def Repetition_count(b, c):
    for i in range(len(b)):
        count = c.count(b[i])
        print(f"{b[i]} - {count}")


string_1 = input("Введите первую строку: ")
string_2 = input("Введите вторую строку: ")

string = Repetition_check(string_1)
Repetition_count(string, string_2)
