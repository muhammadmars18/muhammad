'''
bir nechta kitoblarni saqlaydigan library nomli dict yarating
har bir kitob nomiga uning avtori mos kelsin 
foydalanuvchidan kitob nomini kiritishini so'rang va agar u so'ragan kitob
kutubxona dictida bo'lsa ushbu kitobni avtori shu deb chiqaring
agar bo'lmasa bunday kitob mavjud emas deb chiqaring
'''

# user = input('kitob nomini kiriting: ')

# library = {
#     'Python for Beginners': 'Jane Doe', 
#     'Data Science Essentials': 'John Smith',
#     'Programming': 'Will Smith',
#     'Fire and Ice': 'Van Pirs'
# }
# if user in library:
#     print(library[user])
# else:
#     print('Bunday kitob mavjud emas')



'''
foydalanuvchidan ism so'rang agar u ism quyidagi lug'atda bo'lsa
ha bu ism lug'atda bor deb chiqaring va raqamni ham chiqaring
agar bo'lmasa yo'q yozuvini chiqaring

va so'ngida phonebook dagi dict kalitlarini tartiblangan ko'rinishda
chiqaring.
'''
# phonebook = {
#     'Sardor': '+998-88-4132698',
#     'Olimjon': '+998-90-5985721', 
#     'Xushnudbek': '+998-93-9288803', 
#     'Sarvar': '+998-98-1391176',
#     'Jurabek': '+998-98-6690812', 
#     'Maqsud': '+998-88-5326899', 
#     'Muso': '+998-93-3211653', 
#     'Uygul': '+998-90-4985641'
# }

# user = input('Ism kiriting: ')

# if user in phonebook:
#     print('Ism lug\'atda bor')
#     print('Telefon no\'meri: ', phonebook[user])
# else:
#     print('yo\'q')




'''
vending machine - sotuv mashinasini 
lug'at ko'rinishida ifodalang
kamida 20 ta mahsulotdan iborat bo'lsin
'''

# products = {
#     '1': {'name': 'Snickers', 'price': 12000,},
#     '2': {'name': 'Baunty', 'price': 12000,},
#     '3': {'name': 'Twix', 'price': 12000,},
#     '4': {'name': 'KitKat', 'price': 12000,},
#     '5': {'name': 'Alpengold', 'price': 12000,},
#     '6': {'name': 'Max-fan', 'price': 12000,},
#     '7': {'name': 'Maxito', 'price': 12000,},
#     '8': {'name': 'Limefresh', 'price': 12000,},
#     '9': {'name': 'Coca-Cola', 'price': 12000,},
#     '10': {'name': 'Fanta', 'price': 12000,},
#     '11': {'name': 'Sprite', 'price': 12000,},
#     '12': {'name': 'Pulpy', 'price': 12000,},
#     '13': {'name': 'Flavis', 'price': 12000,},
#     '14': {'name': 'Royal', 'price': 12000,},
#     '15': {'name': 'Lays', 'price': 12000,},
#     '16': {'name': 'Chears', 'price': 12000,},
#     '17': {'name': 'Flint', 'price': 12000,},
#     '18': {'name': 'Grenki', 'price': 12000,},
#     '19': {'name': 'Xrustoff', 'price': 12000,},
#     '20': {'name': 'Xrus Team', 'price': 12000,},
    
# }

mevalar = {"olma": 5, "banan": 3, "nok": 7, "shaftoli": 4}

meva_nomlari = mevalar.keys()

meva_miqdori = mevalar.values()

print("Meva nomlari:", list(meva_nomlari))
print("Meva miqdori:", list(meva_miqdori))













davlatlar_poytaxtlar = {"O'zbekiston": "Toshkent", "Fransiya": "Parij", "AQSh": "Washington, D.C."}

davlatlar_va_poytaxtlar = davlatlar_poytaxtlar.items()

print("Davlatlar va poytaxtlar:", list(davlatlar_va_poytaxtlar))

shahar_aholi = {"Toshkent": 2_000_000, "Parij": 2_100_000, "Moskva": 12_500_000}

uchirish_shahri = input("O'chirmoqchi bo'lgan shahar nomini kiriting: ")

aholi_soni = shahar_aholi.pop(uchirish_shahri, "Bunday shahar mavjud emas")

print("O'zgartirilgan lug'at:", shahar_aholi)

davlatlar_aholisi = {"Rossiya": 144_000_000, "Fransiya": 67_000_000, "O'zbekiston": 34_000_000}

for davlat, aholi in davlatlar_aholisi.items():
    print(f"{davlat}ning aholisi {aholi} kishi")

umumiy_aholi = sum(davlatlar_aholisi.values())
print("Umumiy aholi:", umumiy_aholi)













film_reyting = {"Forrest Gump": 8.8, "Yulduzli urushlar": 8.7, "Interstellar": 8.6}

while film_reyting:
    print("Mavjud filmlar:", list(film_reyting.keys()))
    ochirish_film = input("O'chirmoqchi bo'lgan film nomini kiriting: ")
    film_reyting.pop(ochirish_film, "Bunday film mavjud emas")

print("Barcha filmlar o'chirildi.")

