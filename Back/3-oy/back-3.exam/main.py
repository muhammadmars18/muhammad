# Nazariy
    # 1. Javob:
    # funksiyani yaratish uchun def yoziladi va funksiyaga nom brilladi va funksiyani yozish boshlanadi keyin unga \
    # parametr beriladi  funksiyani ishlatish uchun fnksiyaning nomi yoziladi va shunday qavs => () qo'yiladi ba qavs 
    # ichiga argument beriladi.

    # Funksiyani ishlatishdan maqsad ber nechta qator kodni boshqa joydayam oldin yozgan kodizni funksiya 
    # qib yossangiz  boshqa joyda yozimaysiz shunchaki funksiyzni chaqirib qoysan giz boldi 



    # 2. Javob:
    # funksiyani yaratish uchun def yoziladi va funksiyaga nom brilladi 

    # 3. Javob  va kod
    # def kopaytirish(a, b):
    #     return a + b
    # kopaytirish2 = kopaytirish(9, 8)
    # print(kopaytirish2)


    # 4. Javob:
    # qizil rangda belgilangallari str yozilgallariga  faqat str korinishida argument berish mumkin 
    # int yozilgallariga faqat int korinishida argument berish mumkin 
    # sariq rangda belgilangallari Dakumentatsiya

    # 5. Javob:
    # sikl bu bir necha qator kodni qayta va qayta ishatish uchun kerak
    # for va while sikl orasidagi farq forda kod qachon tugashi bilamiz 

    # 6. javon:
    # calss bu metod va atributlarni oz ichiga oladigan ma'lumot turi

    # 7. Javob:
    # Metod bu classni ichida yozilga funksiyaga aytiladi  
    # Kod:
    #  class Product:
    #   bu metod  
    #   def __init__(self,nomi,narxi,miqdori) :
    #         self.nomi = nomi
    #         self.narxi = narxi
    #         self.miqdori = miqdori 
    # bu atribut
    #         self.nomi = nomi
    #         self.narxi = narxi
    #         self.miqdori = miqdori 

    # 8. Javob:
    # __init__ bu kanstruktor 
    # __del__ bu delstruktor funksiyani ohirida ishlaydi vazifasi funksiyani ochirish
    # __str__ yozilgan kodni string korinishida ifodalaydi
    # __repr__ yozilgan kodni string korinishida ifodalaydi

    # 9. Javob:
    # 1-enkapsulatsiya-Clasni ichiga kod yozishimiz
    # 2-abstraksiya-yashirish orqali kodni tushunishni i foydalanishni osonlashtirish mumkin. 
    # 3-polimorfizm-biron bir clasdan meros olib va meros olinga clasdagi kodlarni meros ovotkan classga yozish
    # 4-inhertens-meros olish

    # 10. Javobida 
    # kalss metod birinchi argumentga clasni oladi
    # atribut metod birinchi argumentga clasni oladi 
# Amaliy
# 3.Kod
# class Person:
#       def init(self, name, birthday, phone, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.address = address
#       def info(self):
#         return f"Name: {self.name}, Phone: {self.phone}"

# class Student(Person):
#       def init(self, name, birthday, phone, address,group):
#             super().init(self, name, birthday, phone, address )
#             self.group = group
#       def info(self):
#         return f"Student: {self.name} | birthday: {self.birthday} | phone: {self.phone} | address{self.address} | Group:{self.group} | "

# Oquvchi2 = Student()
# Oquvchi1 = Student('Muhammad', '6-mart', '977572012', 'chig\'atoy', 1145)
# print(
#     Oquvchi1.info()
# ).Kod

# 4.Kod
# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def info(self):
#         '''Shakl yuzasini hisoblaydigan funksiya'''
#         pass

# class Rectangle(Shape):
#     def init(self, a, b):
#         self.a = a
#         self.b = b

#     def info(self):
#         '''To'rtburchak yuzini topadigan funksiya 
#                                      '''
#         return self.a * self.b
# class Circle(Shape):
#     def init(self, d):
#         self.d = d

#     def area(self):
#         '''Aylana doira faqat ichi bo'sh bo'ladi shuning yuzini hisoblaydigan funksiya'''
#         return math.pi * self.d * self.d


# tortburchak = Rectangle(91, 32)
# print(f"T Yuzi: {tortburchak.info()}") 

# doira = Circle(8)
# print(f"A Yuzi: {doira.info()}")
