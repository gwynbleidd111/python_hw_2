#Задача №2_____________________________________________________

def Truth_table():
    print('X\tY\tZ\tX∧Y\t¬(X∧Y)\t¬(X∧Y)∨Z')
    print('------------------------------------------------')
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                res_1 = x and y
                res_2 = not(x and y)
                res_3 = not(x and y) or z
                print(f'{x}\t{y}\t{z}\t {int(res_1)}'+
                f'\t  {int(res_2)}\t    {int(res_3)}')

Truth_table()
