def inputMas(num):
    return [int(input("Введите число №"+str(i)+" массива:")) for i in range(num)]

def bubleSortUP(mas):
    for j in range(len(mas)):
        for i in range(j,len(mas)-1):
            if mas[i] >= mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
    print(mas)

bubleSortUP(inputMas(5))