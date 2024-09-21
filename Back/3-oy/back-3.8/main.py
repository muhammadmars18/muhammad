# import time
# from typing import Any 
# # double underscore methods = dunder metodlari

# '''
# __slots__
# '''
# class Car:
#     def __init__(self, name, model, color, narxi) -> None:
#         self.name = name
#         self.model = model
#         self.color = color
#         self.narxi = narxi
    
#     def __del__(self):
#         pass
    
#     def __int__(self):
#         return self.narxi

#     def __str__(self):
#         return f"{self.name} {self.model}"
    
#     def __repr__(self) -> str:
#         return f'{self.name}, {self.model}, {self.color}'

#     def __add__(self, other) -> int:
#         return self.narxi + other.narxi

#     def __len__(self) -> str:
#         return 0

#     def __eq__(self, value: object) -> bool:
#         return self.narxi == value.narxi

#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         return f"bu obyet: {self.__str__()}"

#     # uyga vazifa 🔽
#     def __setattr__(self, name: str, value: Any) -> None:
#         super().__setattr__(name, value)

#     # def __contains__(self, item):
#     #     return item in self.name

#     def __getattribute__(self, name: str) -> Any:
#         return super().__getattribute__(name)
    
#     def __delattr__(self, name: str) -> None:
#         super().__delattr__(name)


# car = Car('Lexus', '570', 'oq', 12)
# car1 = Car('Lexus', '570', 'oq', 12)

# car2 = Car('Bugatti', 'veyron', 'gray', 20)
# car3 = Car("BMW", 'X8', 'black', 18)


# # print(
# #     car == car1
# # )
# print(car())


# class Food:
#     def init(self,nomi,narxi,vazni,kaloriyasi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.vazni = vazni
#         self.kaloryazi = kaloriyasi

#     def info(self):
#             return f"Ovqat nomi: {self.nomi} narxi: {self.narxi}"
#     def info(self):
#             return f"Ovqat vazni: {self.vazni} kaloriyasi: {self.kaloriyasi}"

# oqat = Food('nomi,narxi,vazni,kaloriyasi')
# oqat1 = Food('nomi,narxi,vazni,kaloriyasi')

# print(
#       oqat1.info()
# )

class Mahsulot:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

class Shop:
    def __init__(self):
        self.mahsulotlar = []

    def mahsulot_qoshish(self, nomi, narxi):
        yangi_mahsulot = Mahsulot(nomi, narxi)
        self.mahsulotlar.append(yangi_mahsulot)

    def mavjud_mahsulotlar(self):
        if not self.mahsulotlar:
            print("Do'konda hech qanday mahsulot yo'q.")
        else:
            print("Do'kondagi mavjud mahsulotlar:")
            for idx, mahsulot in enumerate(self.mahsulotlar, start=1):
                print(f"{idx}. {mahsulot.nomi} - {mahsulot.narxi} UZS")

class Savat:
    def __init__(self):
        self.savatdagi_mahsulotlar = []

    def savatga_qoshish(self, mahsulot):
        self.savatdagi_mahsulotlar.append(mahsulot)
        print(f"{mahsulot.nomi} savatga qo'shildi.")

    def umumiy_narx(self):
        return sum(mahsulot.narxi for mahsulot in self.savatdagi_mahsulotlar)

    def savatdagi_mahsulotlar_haqida(self):
        if not self.savatdagi_mahsulotlar:
            print("Savat bo'sh.")
        else:
            print("Savatdagi mahsulotlar:")
            for mahsulot in self.savatdagi_mahsulotlar:
                print(f"{mahsulot.nomi} - {mahsulot.narxi} UZS")
            print(f"Umumiy narx: {self.umumiy_narx()} UZS")

def asosiy():
    dokon = Shop()
    savat = Savat()

    while True:
        print("\n1. Mahsulot qo'shish\n2. Mavjud mahsulotlar\n3. Savatga mahsulot qo'shish\n4. Savatni ko'rish\n5. Chiqish")
        tanlov = input("Tanlovni kiriting: ")

        if tanlov == '1':
            nomi = input("Mahsulot nomini kiriting: ")
            narxi = float(input("Mahsulot narxini kiriting: "))
            dokon.mahsulot_qoshish(nomi, narxi)
        elif tanlov == '2':
            dokon.mavjud_mahsulotlar()
        elif tanlov == '3':
            dokon.mavjud_mahsulotlar()
            idx = int(input("Savatga qo'shmoqchi bo'lgan mahsulot raqamini kiriting: ")) - 1
            if 0 <= idx < len(dokon.mahsulotlar):
                savat.savatga_qoshish(dokon.mahsulotlar[idx])
            else:
                print("Noto'g'ri tanlov.")
        elif tanlov == '4':
            savat.savatdagi_mahsulotlar_haqida()
        elif tanlov == '5':
            break
        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")

if __name__ == "__main__":
    asosiy()
