
# Imtihon qoidalari, aldamang, atrofga qaramang!
# Savollarga javob yozing va namuna kodini taqdim eting


# 1-savol: print() bu...

#Javob:
# print bu malumotni terminalga chiqaradi

# Kod namunasi:

print('MMMMMM')

# 2-savol: input() bu...

#Javob:

# input foydalanuvchidan malumot so'rash uchun kerak bo'ladi

# Kod namunasi:

a = input('Ismingizni kiriting: ')

# 3-savol: O'zgaruvchi nima?

#Javob:o'zgaruvchiga qiymat beriladi
# Kod namunasi:
# a = 1   a bu o'zgaruvchi 1 bu qiymat



# 4-savol: 4 ta maʼlumot turini sanab oʻting va misol keltiring:

#Javob:
# Kod namunasi:
int()
str()
float()
bool()


# 5-savol: String formatlash nima va Pythonda ikkita formatlash usuliga misol keltiring:

#Javob:
# Kod namunasi:
# name = 'm'
# lastname = '4407278'

# print(
#     f"{name}{lastname}@gmail.com"
# )



# 6-savol: If, elif, else for nima va ular bilan misol ko'ring:

#Javob:
# Kod namunasi:

# for i in range(8):
#      print()
# yegindi = 0
# for i in range(1, 100,2):
#     yegindi = yegindi + i
#     print(f"yigindi = {yegindi}")

# ball = input('balni kiriting: ')
# ball = int(ball)

# if ball >= 90:
#     print("Juda Ajoyib")
# elif ball >= 80:
#     print("Yaxshi")
# elif ball >= 70:
#     print("O'rtacha")
# elif ball >= 60:
#     print(":(")
# else:
#     print("O'tolmadiz :><)")

# 7-savol: Taqqoslash operatorlarini sanab bering va ularga misol keltiring:

#Javob: < >  ==  !=  
# Kod namunasi:
# a = input('1-chi sonni kiriting: ')
# b = input('2-chi sonni kiriting: ')
# c = input('3-chi sonni kiriting: ')
# a, b, c = int(a), int(b), int(c)

# if a > c and a > b:
#     print(a, 'eng katta son!')
# elif c > a and c > b:
#     print(c, "eng katta son!")
# elif b > a and b > c:
#     print(b, "eng katta son!")
# elif a == c and c == b and a == b:
#  print("Hamma sonlar teng!")
# elif a == b > c:
#  print("1-son va 2-son sonlari teng 3-son kichik")
# elif a == b < c:
#  print("1-son va 2-son sonlari teng 3-son katta")
# elif a > b == c:
#    print("2-son va 3-son sonlari teng 1-son katta")
# elif a < b == c:
#    print("2-son va 3-son sonlari teng 1-son kichik")


# 8-savol: Mantiqiy operatorlar and, or, not bularning vazifasi nima va unga misol keltiring:

#Javob: not bu emas ; and bu va ; or bu  yoki degani
# Kod namunasi:
# a = input('1-chi sonni kiriting: ')
# b = input('2-chi sonni kiriting: ')
# c = input('3-chi sonni kiriting: ')
# a, b, c = int(a), int(b), int(c)

# if a > c and a > b:
#     print(a, 'eng katta son!')



# 9-savol: Loop(sikl) nima va while sikli qanday ishlaydi:

#Javob: sikl bu kod qayta va qayta ishlatish uchun kerak bo'ladi
# Kod namunasi:

# son = int(input("Iltimos, son kiriting: "))
# summa = 0

# for i in range(1, son + 1):
#     summa += i

# print(f"Input: {son}. Output: {summa}")

# 10-savol: For va while o'rtasidagi farq nima va misol keltiring:

#Javob:

# for da qachon tugashini bilamiz while da bilmaymiz

# Kod namunasi:

# parol = 'banana'
# user = input('maxfiy so\'zni kiriting: ')

# while user != parol:
#     user = input('maxfiy so\'zni kiriting: ')

# print('topdiz')


# for i in range(8):
#      print()
# yegindi = 0
# for i in range(1, 100,2):
#     yegindi = yegindi + i
#     print(f"yigindi = {yegindi}")

# 11-chi: Endi siz o'yin qilishingiz kerak: tosh, qog'oz, qaychi.
# Ya'ni, bu o'yinni ikkita o'yinchi o'ynashiga ishonch hosil qilishingiz kerak, omad tilaymiz!
# import random
# computer = random.choice(
#     ('tosh', 'qogoz', 'qaychi')
# )
# print(('tosh', 'qogoz', 'qaychi'))
# user = input("tanlovizni kiriting: ").strip().lower()

# if user == 'tosh':
#     if computer == 'qaychi':
#         print('siz yutdingiz!')
#     elif computer == 'qogoz':
#         print('yutqazdiz!')
#     else:
#         print('durang!')
# if user == 'qaychi':
#     if computer == 'qogoz': 
#         print('siz yutdingiz!')
#     elif computer == 'tosh':
#         print('yutqazdiz!')
#     else:
#         print('durang!')
# if user == 'qogoz':
#     if computer == 'qaychi':
#         print('siz yutdingiz!')
#     elif computer == 'tosh':
#         print('yutqazdiz!')
#     else:
#         print('durang!')
