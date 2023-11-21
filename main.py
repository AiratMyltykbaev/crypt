surname = 'Мылтыкбаев'
name = 'Айрат'
sec = 'Рустамович'
Tablersa = { 1, 13, 4, 6, 7, 5, 14, 4,
    15, 11, 11, 12, 13, 8, 11, 10,
    13, 4, 10, 7, 10, 1, 4, 9,
    0, 1, 0, 1, 1, 13, 12, 2,
    5, 3, 7, 5, 0, 10, 6, 13,
    7, 15, 2, 15, 8, 3, 13, 8,
    10, 5, 1, 13, 9, 4, 15, 0,
    4, 9, 13, 8, 15, 2, 10, 14,
    9, 0, 3, 4, 14, 14, 2, 6,
    2, 10, 6, 10, 4, 15, 3, 11,
    3, 14, 8, 9, 6, 12, 8, 1,
    14, 7, 5, 14, 12, 7, 1, 12,
    6, 6, 9, 0, 11, 6, 0, 7,
    11, 8, 12, 3, 2, 0, 7, 15,
    8, 2, 15, 11, 5, 9, 5, 5,
    12, 12, 14, 2, 3, 11, 9, 3}

# while True:
#             print("1. Шифрование Гост")
#             print("2. Шифрование RSA")
#             print("3. Хэш")
#             print("4. ЭЦП по методу RSA")
#             print("5. Выход")
#             choice = input("Выберите опцию: ")
#             if choice == '1':
#                 print("Вы выбрали опцию 1")
#             elif choice == '2':
#                 print("Вы выбрали опцию 2")
#             elif choice == '2':
#                 print("Вы выбрали опцию 3")
#             elif choice == '2':
#                 print("Вы выбрали опцию 4")
#             elif choice == '5':
#                 break
#             else:
#                 print("Неправильный выбор. Попробуйте снова")

def gost(sur, secname):
    massur = []
    for i in sur[:8:]:
        massur.append(bin(i)[2::])
    massur = (''.join(map(str, massur)))
    l0 = (massur[:32:]) #первые 32.
    r0 = (massur[32::]) #вторые 32.
    print((l0), (r0))
    massec = []
    for i in secname[:4:]:
        massec.append(bin(i)[2::])
    x0 = (''.join(map(str, massec)))
    print(x0)
#    print((r0 & x0) % (2 ** 32)) # тут якобы сложение по 2^32
    #return mas

print(gost(surname.encode('cp1251'), sec.encode('cp1251')))