# while True:
#     son1 = int(input('son1 = '))
#     son2 = int(input('son2 = '))

#     ishora = input("Ishorani kiriting (-,+,/,*):  ").strip()

#     if ishora == '-':
#         javob = son1-son2
#         break
        
#     elif ishora == '+':
#         javob = son1+son2
#         break
#     elif ishora == '/':
#         javob = son1/son2
#         print(javob)
#         break
#     elif ishora == '*':
#         javob = son1*son2
#         print(javob)
#         break
#     elif ishora =='**':
#         javob =son1**son2
#         print(javob)
#         break
#     elif ishora =='-+':
#         javob = 'notog\'ri ishora kiritting'
#         print(javob)
#         break
#     elif ishora =='-+/':
#         javob = 'notog\'ri ishora kiritting'
#         print(javob)
#         break
#     elif ishora =='-+/*':
#         javob = 'notog\'ri ishora kiritting'
#         print(javob)
#         break

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


    
import random


bot_soni = random.randint(1, 10)
user_soni = 0

while True:
    user_soni += 1
    kiritilgan_son = int(input("Son kiriting (1 dan 10 gacha): "))
    
    if kiritilgan_son < bot_soni:
        print("Noto'g'ri, kattaroq son kiritib ko'ring.")
    elif kiritilgan_son > bot_soni:
        print("Noto'g'ri, kichikroq son kiritib ko'ring.")
    else:
        print(f"Tabriklaymiz! Siz {user_soni} urinishda topdingiz.")
        break  







    password = "MD18"

while True:
    parol = input("Parolni kiriting: ")
    if parol == password:
        print("Parol to'g'ri!")
        break
    else:
        print("Parol noto'g'ri, qayta urinib ko'ring.")
