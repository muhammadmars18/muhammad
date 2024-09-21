'''
vazifalar
1 - fruits nomli tuple yarating va unga sevimli 3 ta mevangizni 
qo'shing
2 - fruits ning ikkinchi elementini konsolga chiqaring
3 - fruits bilan ushbu tuple ni birlashtiring -> ('orange', 'grape') 
va combined_fruits ga saqlang
4 - 'banana' mevasi combined_fruitsda mavjudligini tekshiring
5 - empty_tuple nomi bilan bo'sh tuple yarating va 
uni konsolga chiqaring
'''


# fruits = ('apelsin','mandarin','banan')
# print(fruits[1])
# fruits2 = ('orange', 'grape')
# combined_fruits = fruits + fruits2
# print(combined_fruits.count('banan'))
# empty_tuple = ()


'''
1 - count va index
    - 'apple', 1, 'banana', 2, 'orange' larni o'z ichiga
      olgan mixed_tuple nomli tuple yarating
    - 2 raqami nechtaligini hisoblang
    - 'banana' ning indeksini aniqlang

2 - birlashtirish va takrorlash
    - 1,2,3 ni o'z ichiga olgan tuple1 va
      'a', 'b', 'c' ni o'z ichiga olgan tuple2 ni yarating
    - ikta tuple ni combined_tuple ga birlashtiring
    - combined_tuple ni 3 marta takrorlang
    m-n: combined_tuple = [1,2,3] -> [1,2,3,1,2,3,1,2,3]

3 - qo'shish va ko'paytirish
    - bir nechta elementni o'z ichiga olgan first_tuple ni 
      yarating
    - turli elementni o'z ichiga olgan different_tuple ni 
      yarating
    - ikta tuple ni final_tuple ga birlashtiring
    - final_tuple ni 2 marta takrorlang

'''
# 1
# mixed_tuple = ('apple', 1, 'banana', 2, 'orange')
# # print(mixed_tuple.count(2))
# print(mixed_tuple.index('banana'))


# 2
# tuple1 = (1,2,3)
# tuple2 = ('a','b','c')
# combined_tuple = tuple1 + tuple2 
# combined_tuple = combined_tuple * 3
# print(combined_tuple)


# 3
# first_tuple = ('orange','strawberry','banana','kiwi')
# different_tuple = ('apple','melon','watermelon','pineapple')
# final_tuple  = first_tuple + different_tuple
# final_tuple = final_tuple * 2
# print(final_tuple)


raqamlar = [1, 2, 3, 4, 5]

for raqam in raqamlar:
    print(raqam)

nomlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]

indeks = 0
while indeks < len(nomlar):
    print(nomlar[indeks])
    indeks += 1

raqamlar = [10, 20, 30, 40, 50]

jami = 0
for raqam in raqamlar:
    jami += raqam

print("Ro'yxatdagi raqamlar yig'indisi:", jami)

royxat = [3, 6, 9, 2, 5, 8]

indeks = 0
while indeks < len(royxat):
    if royxat[indeks] % 2 == 0:
        print("Birinchi juft son:", royxat[indeks])
        break
    indeks += 1

raqamlar = [7, 12, 4, 9, 3]

yangi_raqamlar = []
for raqam in raqamlar:
    if raqam < 5:
        yangi_raqamlar.append(raqam)

print("O'zgartirilgan ro'yxat:", yangi_raqamlar)

royxat = []

raqam = int(input("Raqam kiriting (0 dan tashqari): "))
while raqam != 0:
    royxat.append(raqam)
    raqam = int(input("Raqam kiriting (0 dan tashqari): "))

print("Olingan ro'yxat:", royxat)

elementlar = [5, "salom", True, 3.14, [1, 2, 3]]

for indeks, element in enumerate(elementlar):
    print("Indeks", indeks, ":", element)

    
