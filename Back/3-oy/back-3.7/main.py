# import time


# class A:
#     def __init__(self):
#         print("A Obyekti yaratildi :)")
#     def __del__(self):
#         print("A obyekti o'chirildi :(")


# # a = A()
# # for i in range(4):
# #     print(i)
# #     time.sleep(1)
# # print('deleting objet')
# # del a

# # time.sleep(2)

# class B:
#     def __init__(self, oby):
#         self.obj = oby
#         print('B obyekti yaratildi') # birinchi print


# class C:
#     def __init__(self):
#         self.b = B(self)
#         print('C obyekt yaratildi ::)') # 2nchi print
#     def __del__(self):
#         print("C obyekti O'chirildi!") # 3nchi print
# c = C()
# del c
# print('salom') # 4nchi print


class Mushuk:
    def __init__(self, ism, yoshi, rangi):
        self.ism = ism
        self.yoshi = yoshi
        self.rangi = rangi
    
    def tanishtirmoq(self):
        print(f"Salom, mening ismim {self.ism}. Men {self.yoshi} yoshdaman va mening palto rangim {self.rangi}.")
    
    def miyov(self):
        print("Miyav!")
    
    def set_yosh(self, yangi_yosh):
        self.yoshi = yangi_yosh
    
    def set_rangi(self, yangi_rangi):
        self.rangi = yangi_rangi
    
    def oziqlantirmoq(self):
        print(f"{self.ism} oziqlandi va endi u kuchliroq!")

mening_mushugim = Mushuk("Tom", 3, "kulrang")

mening_mushugim.tanishtirmoq()

mening_mushugim.miyov()

mening_mushugim.set_yosh(4)
print(f"Yangi yosh: {mening_mushugim.yoshi}")

mening_mushugim.set_rangi("oq")
print(f"Yangi palto rangi: {mening_mushugim.rangi}")

mening_mushugim.oziqlantirmoq()

