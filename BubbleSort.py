def inputMas(num):
    return [int(input("Введите число №"+str(i)+" массива: ")) for i in range(num)]

def inputType():
    flag = True
    while flag:
        type = input("Введите тип сортировки.\n"+
                     "По возрастанию - 1\n"+
                     "По убыванию - 2\n"
                     "Ваш выбор: ")
        if type.isdigit():
            if int(type) == 1 or int(type) == 2:
                flag = False
    return int(type)

def bubleSort(mas, type):
    for j in range(len(mas)):
        for i in range(j, len(mas) - 1):
            if mas[i] >= mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    if type == 1:
        print(mas)
    else:
        print(mas[::-1])

bubleSort(inputMas(5),inputType())