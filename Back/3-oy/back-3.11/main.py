# c = 3661
# h = 60
# m = 60
# s = 60

# asd = c // h
# asd1 = c// m
# asd2 = c % s
# print(
#     f'Soat: {asd} | Minut: {asd1} | Sekund: {asd2}'
# )



'''
Time clasini yarating 
o'ziga sekundlarni qabul qilib 
soat, minut, va sekundlarini aniqlab Time 
clasidan obyekt yaratib qaytaradigan metod yarating
'''

# class Time:
#     def __init__(self, hour, minutes, seconds):
#         self.hour = hour
#         self.minutes = minutes
#         self.seconds = seconds

#     @classmethod
#     def from_seconds(cls, total_seconds):
#         remaining_seconds = total_seconds % 3600
#         hours = total_seconds // 3600
#         minutes = remaining_seconds // 60
#         seconds = remaining_seconds % 60
#         return cls(hours, minutes, seconds)
    
#     def __str__(self):
#         return f"{self.hour} soat, {self.minutes} minut, {self.seconds} sekund"



class Mijoz:
    def __init__(self, nom, balans=0):
        self.nom = nom
        self.balans = balans
        self.tranzaksiyalar = []

    def show_account(self):
        print(f"Mijoz: {self.nom}, Hisob balansi: {self.balans} UZS")

    def depozit(self, summa):
        self.balans += summa
        self.tranzaksiyalar.append(f"Depozit: {summa} UZS")
        print(f"{summa} UZS miqdorida depozit kiritildi. Joriy balans: {self.balans} UZS")

    def yechish(self, summa):
        if summa <= self.balans:
            self.balans -= summa
            self.tranzaksiyalar.append(f"Yechish: {summa} UZS")
            print(f"{summa} UZS miqdorida mablag' yechildi. Joriy balans: {self.balans} UZS")
        else:
            print("Yechish uchun balans yetarli emas!")

    def tranzaksiya_tarixi(self):
        print(f"{self.nom}ning tranzaksiyalar tarixi:")
        for tranzaksiya in self.tranzaksiyalar:
            print(tranzaksiya)



class Bank:
    def __init__(self):
        self.mijozlar = []

    def add_customer(self, mijoz):
        self.mijozlar.append(mijoz)
        print(f"Yangi mijoz qo'shildi: {mijoz.nom}")

    def mijozni_topish(self, nom):
        for mijoz in self.mijozlar:
            if mijoz.nom == nom:
                return mijoz
        return None

    def barcha_mijozlar(self):
        if not self.mijozlar:
            print("Bankda mijozlar yo'q.")
        else:
            print("Bankdagi barcha mijozlar:")
            for mijoz in self.mijozlar:
                mijoz.show_account()





def asosiy():
    bank = Bank()

    mijoz1 = Mijoz("Ali", 1000)
    mijoz2 = Mijoz("Vali", 2000)
    mijoz3 = Mijoz("Salim", 1500)

    bank.add_customer(mijoz1)
    bank.add_customer(mijoz2)
    bank.add_customer(mijoz3)

    bank.barcha_mijozlar()

    mijoz = bank.mijozni_topish("Ali")
    if mijoz:
        mijoz.show_account()
        mijoz.depozit(500)
        mijoz.yechish(300)
        mijoz.tranzaksiya_tarixi()

    bank.barcha_mijozlar()

if __name__ == "__main__":
    asosiy()
