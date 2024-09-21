3
print('''
Kontaktlar bo'limiga xush kelibsiz
add - kontakt qo'shish
delete - kontaktni olib tashlash
show - barcha kontaktlarni ko'rsatish
exit - chiqish uchun 'exit' ni kiriting
''')

contacts = {}
# while True:
#     user = input("|||||: ")
#     if user == 'add':
#         name = input("Ismingizni kiriting: ")
#         phone = input("Telefon raqamingizni kiriting: ")
#         email = input('Elektron pochtangizni kiriting: ')
#         contacts[name] = phone
#         print(f"{name} kontaktlarga qo'shildi.")

#     elif user == 'delete':
#         name = input("O'chiriladigan kontakt nomini kiriting: ")
#         if name in contacts:
#             del contacts[name]
#             print(f"{name} kontaktlardan o'chirildi.")
#         else:
#             print(f"{name} nomli kontakt topilmadi.")

#     elif user == 'show':
#         if contacts:
#             print("Kontaktlar:")
#             for name, phone in contacts.items():
#                 print(f"{name}: {phone}")
#         else:
#             print("Hozircha hech qanday kontakt mavjud emas.")
    
#     elif user == 'exit':
#         print('bye! :(')
#         break

#     else:
#         print('siz boshqa buyruqni kiritdingiz qaytadan urinib ko\'ring')

# print(contacts)


# Restoran menyusi
# Lug'at yaratish, unda kalitlar idishlarning nomlari va qiymatlari ularning narxidir
menu = {
    "osh": 20,
    "lag'mon": 18,
    "somsa": 3,
    "shashlik": 25,
    "mastava": 15
}

print("Menyuda mavjud taomlar:")
print("Taomlar:", list(menu.keys()))
print("Narxlar:", list(menu.values()))

taom_nom = input("Iltimos, menyudan taom nomini kiriting: ")

if taom_nom in menu:
    narx = menu[taom_nom]
    print(f"{taom_nom} {narx} so'm.")
    buyurtma = input("Ushbu taomni buyurtma berishni istaysizmi? (yes/no): ")
    if buyurtma.lower() == "yes":
        print("Buyurtmangiz qabul qilindi, tez orada sizga xizmat qilamiz!")
    else:
        print("Rahmat! Boshqa taom tanlashingiz mumkin yoki restoranni tark etingiz.")
else:
    print("Ushbu taom menyuda mavjud emas.")
    print("Iltimos, boshqa taom tanlang yoki restoranni tark eting.")
