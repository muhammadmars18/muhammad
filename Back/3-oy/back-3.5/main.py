'''Product klasini yarating
uning mahsulot nomi va uning narxi, miqdori bo'lsin
va shuningdek uning process_order nomli metodi ham bo'lsin

process_order metodining vazifasi mahsulotga buyurtma 
berilganda u uchun hisob kitob qilib ma'lumot chiqazib 
berish

masalan: 
Cola uchun buyurtmangiz tayyorlanmoqda
Umumiy narxi: 200000 so'm
'''


# class Product:
#     def __init__(self,nomi,narxi,miqdori) :
#         self.nomi = nomi
#         self.narxi = narxi
#         self.miqdori = miqdori
#     def process_order(self):
#         nimadur = self.miqdori * self.narxi         
#         print('Pepsi uchun buyurtmangiz tayyorlanmoqda')
#         return f"Miqdori {self.miqdori} | 1 donasining narxi {self.narxi} | Umumiy narxi: {nimadur}"
    


# pepsi = Product(nomi = 'Pepsi',narxi = 8000, miqdori = 20)
# print(pepsi.process_order())  




# '''va quyida Meva, Ichimlik, Shirinlik kabi childklasslar
# hosil qiling va super clasning process_order metodini 
# har bir childklas uchun alohida yozing'''


# class Fruits(Product):
#     def __init__(self, nomi,narxi, miqdori):
#         super().__init__(nomi, narxi, miqdori)
#     def process_order(self):
#         nimadur = self.miqdori * self.narxi         
#         print('Olma uchun buyurtmangiz tayyorlanmoqda')
#         return f"Yashigi {self.miqdori} | 1 kg narxi {self.narxi} | Umumiy narxi: {nimadur}"
    


# olma = Product(nomi = 'Olma',narxi = 55000, miqdori = 10)
# print(olma.process_order())  



# class sweets(Product):
#     def __init__(self, nomi,narxi, miqdori):
#         super().__init__(nomi, narxi, miqdori)
#     def process_order(self):
#         nimadur = self.miqdori * self.narxi         
#         print('Skolad uchun buyurtmangiz tayyorlanmoqda')
#         return f"Miqdori {self.miqdori} | 1 donasining narxi {self.narxi} | Umumiy narxi: {nimadur}"
    


# shkalad = Product(nomi = 'Shikolad',narxi = 15000, miqdori = 10)
# print(shkalad.process_order())


class Belgilar:
    def __init__(self, ism, daraja, salomatlik, hujum_kuchi):
        self.ism = ism
        self.daraja = daraja
        self.salomatlik = salomatlik
        self.hujum_kuchi = hujum_kuchi

    def hujum(self):
        print(f"{self.ism} hujum qiladi.")

    def salomatlantirish(self):
        print(f"{self.ism} salomatlanadi.")

    def darajani_oshirish(self):
        self.daraja += 1
        print(f"{self.ism}ning darajasi {self.daraja} ga oshirildi.")


class Jangchi(Belgilar):
    def __init__(self, ism, daraja, salomatlik, hujum_kuchi, qalqon_soni):
        super().__init__(ism, daraja, salomatlik, hujum_kuchi)
        self.qalqon_soni = qalqon_soni

    def hujum(self):
        print(f"{self.ism} {self.qalqon_soni} ta qalqon bilan hujum qiladi.")


class Mage(Belgilar):
    def __init__(self, ism, daraja, salomatlik, hujum_kuchi, max_maqsadlar):
        super().__init__(ism, daraja, salomatlik, hujum_kuchi)
        self.max_maqsadlar = max_maqsadlar

    def use_magic(self):
        print(f"{self.ism} max maqsadlarga zarb beradi.")


class Archer(Belgilar):
    def __init__(self, ism, daraja, salomatlik, hujum_kuchi, tirish):
        super().__init__(ism, daraja, salomatlik, hujum_kuchi)
        self.tirish = tirish

    def hujum(self):
        print(f"{self.ism} yaydan {self.tirish} martalik tir qiladi.")


print("Turli xil belgilarni yaratish va ular bilan muloqot:")
jangchi = Jangchi("Bahrom", 5, 100, 8, 2)
mage = Mage("Gandalf", 8, 80, 10, 3)
archer = Archer("Legolas", 6, 90, 7, 5)

jangchi.hujum()
jangchi.darajani_oshirish()
jangchi.salomatlantirish()

mage.use_magic()
mage.darajani_oshirish()

archer.hujum()
archer.hujum("qalin")  