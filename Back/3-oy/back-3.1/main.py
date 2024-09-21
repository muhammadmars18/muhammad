# class Moshina():
#     moshina_nomi = 'Mers'
#     rangi = 'Qora'
#     modelli = 'AMG GT'
#     moshina_dvigitili = ' M178 V8'
    

# class Moshina():
#     def __init__(self, rangi, modelli):
#         self.modelli = modelli
#         self.rangi = rangi


# car1 = Moshina(rangi='qora',modelli='AMG GT')
# car2 = Moshina(rangi='oq',modelli='amg gt')
# print(car1.rangi)
# print(car2.rangi)


class Hayvon:
    def __init__(self, ism, yosh, turi):
        self.ism = ism
        self.yosh = yosh
        self.turi = turi
    
    def malumot(self):
        return f"Mening ismim {self.ism}, men {self.yosh} yoshdaman va men {self.turi}"

# Animal sinfimizning bir nechta obyektlarini yaratish
quyon = Hayvon("Quyon", 5, "ittifoq")
it = Hayvon("It", 3, "sirt")
mushuk = Hayvon("Mushuk", 2, "qush")

# Obyektlarni ekranga chiqarish
print(quyon.malumot())
print(it.malumot())
print(mushuk.malumot())
