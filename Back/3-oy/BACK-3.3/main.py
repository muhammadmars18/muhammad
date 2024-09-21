
# class Kalkulyatr:
#     def qoshish(self, a , b ):
#        return a + b
#     def ayirish(self,a , b ,):
#        return a - b
#     def kopaytirish(self,a , b ,):
#        return a * b
#     def bolish(self,a , b ,):
#        return a / b

# calc =  Kalkulyatr()
# print(
#     calc.ayirish(12,12)
# )


# class Animal:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
#     def info(self):
#         return {self.name} | {self.age}

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass
    
# animals = Animal(name = 'bobik', age = 5)
# animals1 = Animal(name = 'gucci', age = 4)
# print(animals.info(),animals1.info())


class Shop:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.mahsulotlar = {}

    def qoshish_mahsulot(self, nom, narx):
        self.mahsulotlar[nom] = narx
        print(f"{nom} nomli mahsulot do'konga qo'shildi. Narxi: {narx} so'm")

    def mahsulotni_ochirish(self, nom):
        if nom in self.mahsulotlar:
            del self.mahsulotlar[nom]
            print(f"{nom} nomli mahsulot do'kondan olib tashlandi.")
        else:
            print("Bunday nomli mahsulot do'konda mavjud emas.")

    def sell_mahsulot(self, nom, miqdor):
        if nom in self.mahsulotlar:
            narx = self.mahsulotlar[nom]
            if miqdor > 0:
                if miqdor <= len(self.mahsulotlar):
                    narx *= miqdor
                    print(f"{nom} nomli mahsulot {miqdor} dona sotildi. Umumiy narxi: {narx} so'm")
                    del self.mahsulotlar[nom]
                else:
                    print("Do'konda yetarli mahsulot mavjud emas.")
            else:
                print("Mahsulot miqdori musbat son bo'lishi kerak.")
        else:
            print("Bunday nomli mahsulot do'konda mavjud emas.")



dokon = Shop("Oziq-ovqat dokoni", "Toshkent sh. Chilonzor tumani")
dokon.qoshish_mahsulot("Banani", 7000)
dokon.qoshish_mahsulot("Olma", 5000)
dokon.qoshish_mahsulot("Gilos", 3000)


dokon.mahsulotni_ochirish("Banani")
dokon.sell_mahsulot("Gilos", 5)
dokon.sell_mahsulot("Olma", 2)

print(f"\n{dokon.nomi} manzili: {dokon.manzili}")
print("Do'konda qolgan mahsulotlar:")
for nom, narx in dokon.mahsulotlar.items():
    print(f"{nom}: {narx} so'm")
