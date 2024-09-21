# Imtihon qoidalari, aldamang, atrofga qaramang!
# Savollarga javob yozing va namuna kodini taqdim eting.



# 1 savol: Pythonda bo'sh ro'yxatni qanday yaratish mumkin?

#Javob: listga nom qoyiladi keyin borobar qo'yiladi va tort burchak qavs qoyiladi
# Kod namunasi:
# my_list = []



# 2-savol: Python-da ro'yxat uzunligini qanday olish mumkin?

#Javob:ro'yxat uzunligini topish uchun len ishlatiladi
# Kod namunasi:
# fruit = ['apple','watermelon','melon']
# fruit1 = len(fruit)
# print(fruit1)





# 3-savol: Ro'yxat oxiriga elementni qanday qo'shish mumkin?

#Javob: ro'yxatga append orqali qo'shiladi
# Kod namunasi:
# fruit = ['apple','watermelon','melon']
# fruit.append('banana')
# print(fruit)


# 4-savol: Ro'yxatdagi ma'lum bir indeksdagi elementni qanday olish mumkin?

#Javob: pop orqali
# Kod namunasi:
# fruit = ['apple','watermelon','melon']
# fruit.pop(2)
# print(fruit)



# 5-savol: Muayyan indeksdagi ro'yxat elementining qiymatini qanday o'zgartirish mumkin?

#Javob:
# Kod namunasi:
# fruit = ['apple','watermelon','melon']
# fruit1 = fruit
# fruit1[0] = 'banana'
# print(fruit1)



# 6-savol: Pythonda lug'at (dict) nima?

#Javob:dict (Dictionaries) - lug'atlar pythonda ma'lumotolarni kalit va qiymat
# ko'rinishidagi ifodalaydigan juda kuchli va ko'p qirrali
# ma'lumot turi hisoblanadi
# Kod namunasi:
# menu = {
#     "osh": 20,
#     "lag'mon": 18,
#     "somsa": 3,
#     "shashlik": 25,
#     "mastava": 15
# }



# 7-savol: Lug'atga element qanday qo'shiladi?

#Javob: lug'atga update orqaqli qo'shiladi
# Kod namunasi:
# menu = {
#     "osh": 20,
#     "lag'mon": 18,
#     "somsa": 3,
#     "shashlik": 25,
#     "mastava": 15
# }
# menu1 = menu
# menu1.update({'xalim':20})
# print(menu1)


# 8-savol: Lug'atda ma'lum bir kalitning qiymatini qanday olish mumkin?

#Javob:
# Kod namunasi:
# my_dict = {"name": "Muhammad", "age": 12, "city": "Tashkkent"}

# my_value = my_dict["name"]
# print(my_value)




# 9-savol: Lug'atdan elementni qanday olib tashlash mumkin?

#Javob:lug'atdan pop orqali olib tashlanadi
# Kod namunasi:
# menu = {
#     "osh": 20,
#     "lag'mon": 18,
#     "somsa": 3,
#     "shashlik": 25,
#     "mastava": 15
# }
# menu1 = menu.pop("somsa")
# print(menu1)
# print(menu)


# 10-savol: Python-da kortej nima?

# Javob: Python tilida "kortej" degani "tuple" deb ataladi. Kortej bir nechta qiymatlarni o'z ichiga oladi va unga o'zgartirishsiz bo'lgan ro'yxat deb ham aytiladi. Bu ro'yxatni qavs orqali ifodalash mumkin bo'lsa-da, kortej() belgilar orqali ifodalanadi.
# Kod namunasi:
# teachers = ('Ali', 'Muhammad','Munisa')
# oqituvchilar = tuple(teachers)
# print(oqituvchilar)



# 11-savol: Bo'sh kortejni qanday e'lon qilish kerak?

#Javob: tuplega nom beriladi va () <- shunday qavs qo'yiladi
# Kod namunasi:
# teachers = ()



# 12-savol: Tuple yaratilgandan keyin uning elementlari qiymatlarini o'zgartirish mumkinmi?

#Javob: tuple yaratilganidan keyin uning elementlar qiymatlarini o'zgartirib bo'lmaydi
# Kod namunasi:



# №13-savol: Python-da for tsikli nima?

#Javob: for bu kod qayta va qayta ishlatish uchun kerak bo'ladi
# Kod namunasi:
# son = int(input("Iltimos, son kiriting: "))
# summa = 0

# for i in range(1, son + 1):
#     summa += i
# print(f"Input: {son}. Output: {summa}")



# № 14-savol: siklda break operatoridan qanday foydalanish kerak?

#Javob: Agar bir siklda  break operatoridan foydalanish kerak bo'lsa, uni shart bo'lgan holatda siklni to'xtatish uchun ishlatishingiz mumkin
# Kod namunasi:

# my_list = [1, 2, 3, 4, 5]

# for item in my_list:
#     print(item)
#     if item == 3:
#         break


# № 15-savol: Davom iborasidan siklda qanday foydalaniladi?

#Javob: Siklda foydalanish uchun, biz bir dastur qatorini bir necha marta takrorlash uchun ishlatiladi. 
# Kod namunasi:
#     my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item)           