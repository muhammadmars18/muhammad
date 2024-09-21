# '''
# kontaktlar bo'sh lug'ati (dict) ini yarating
# va foydalanuvchi quyidagi xususiyatlarga ega
# bo'lishi kerak
# 1. foydalanuvchi kontakt kirita olishi
# (ya'ni kontakt qo'sha olishi)
# 2. kontaktdan ma'lum odam kontaktini olib tashlay
# olishi (ya'ni o'chirib tashlay olishi)
# 3. va barcha kontaktlarni ko'ra olishi kerak
# '''


# print('''
# Kontaktlar bo'limiga xush kelibsiz
# add - kontakt qo'shish
# delete - kontaktni olib tashlash
# show - barcha kontaktlarni ko'rsatish
# exit - chiqish uchun 'exit' ni kiriting
# soni - kontaktlar sonini ko'rish
# ''')

# contacts = {}
# while True:
#     user = input("|||||: ")
#     if user == 'add':
#         name = input("Ismingizni kiriting: ")
#         raqam = input("Raqamingizni kiriting: ")
#         email = input("elektron pochtangizni kiriting: ")
#         contacts[name] = {'raqam': raqam, 'email': email}
#         # contacts.update(
#         #     {name: {'raqam': raqam, 'email': email}}
#         # )
#         # contacts.setdefault(
#         #     name,
#         #     {'raqam': raqam, 'email': email}
#         # )

#     elif user == 'delete':
#         name = input('o\'chirmoqchi bo\'lgan kontaktingizni kiriting ')
#         if name in contacts:
#             del contacts[name]

#     elif user == 'show':
#         for name in contacts.keys():
#             print(
#                 f"ismi: {name} | raqami: {contacts[name]['raqam']} | pochtasi: {contacts[name]['email']}"
#             )

#     elif user == 'soni':
#         print(
#             f"sizda {len(contacts)} ta kontakt bor"
#         )

#     elif user == 'exit':
#         print('bye! :(')
#         break

#     else:
#         print('siz boshqa buyruqni kiritdingiz qaytadan urinib ko\'ring')


# print(contacts)




def calc_string_length():
    string = input("Iltimos, satrni kiriting: ")
    length = len(string)
    print(f"Satr uzunligi: {length}")

calc_string_length()  





def vaqt_mashinasi(yil):
    faktlar = {
        2022: "Koreya bo'ylab Olimpiya o'yinlari bo'lib o'tdi.",
        2019: "Birinchi siyosiy rivojlanish miqdorini kiritish uchun HUV qaror qilindi.",
        2016: "Donald Trump AQSh prezidenti bo'ldi.",
        2012: "Endi moslamalik ham davom ettirilmoqda."
    }

    if yil in faktlar:
        return faktlar[yil]
    else:
        return "Bu yil haqida hech qanday ma'lumot yo'q"

# Test qatorlari
print(vaqt_mashinasi(2022))  # Koreya bo'ylab Olimpiya o'yinlari bo'lib o'tdi.
print(vaqt_mashinasi(2017))  # Bu yil haqida hech qanday ma'lumot yo'q

