# class SimCard:
#     def __init__(self, nomi, modeli, telraqami, kodi, beelinekodi ) -> None:
#         self.nomi = nomi
#         self.modeli = modeli
#         self.telraqami = telraqami
#         self.kodi = kodi
#         self.beelinekodi = beelinekodi
#     def info(self):
#         return f"{self.nomi} | {self.modeli} | {self.telraqami} | {self.kodi} | {self.beelinekodi}"
        
# card = SimCard(nomi="beeline",modeli="nano",telraqami=6731266,kodi=998,beelinekodi=90)   
# print(card.info())


# class Inson:
#     def __init__(self, ismi, familiyasi, jinsi):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.jinsi = jinsi
#         self.yoshi = 0
    
#     def info(self):
#         return f"ismi: {self.ismi}, familiyasi: {self.familiyasi}"

# class Mexanik(Inson):
#     def __init__(self, ismi, familiyasi, jinsi, tajriba):
#         super().__init__(ismi, familiyasi, jinsi)
#         self.tajriba = tajriba

#     def info(self):
#         return f"Mexanik: {self.ismi} tajribasi: {self.tajriba} yil"

# ishchi2 = Mexanik()
# ishchi1 = Mexanik('Davron', 'Rajabov', 'erkak', 2)
# print(
#     ishchi1.info()
# ) 

class Meva:
    def __init__(self, nomi, rangi):
        self.nomi = nomi
        self.rangi = rangi

    def eat(self):
        print(f"{self.nomi} ni yeyapman!")

    def check_freshness(self):
        print(f"{self.nomi} ning tazaligi tekshirildi.")


class Olma(Meva):
    def __init__(self, nomi, rangi, xususiyat):
        super().__init__(nomi, rangi)
        self.xususiyat = xususiyat

    def eat(self):
        print(f"{self.nomi}ni hozir yeyaman! {self.xususiyat}")


class Nok(Meva):
    def __init__(self, nomi, rangi, yuzi):
        super().__init__(nomi, rangi)
        self.yuzi = yuzi

    def check_freshness(self):
        print(f"{self.nomi}ning tazaligi yuzi bo'yicha tekshirildi. {self.yuzi}")


class Apelsin(Meva):
    def __init__(self, nomi, rangi, tuzilishi):
        super().__init__(nomi, rangi)
        self.tuzilishi = tuzilishi

    def eat(self):
        print(f"{self.nomi}ni yoqimli yeyaman! {self.tuzilishi}")


# Foydalanuvchi bilan muloqot
print("Turli xil mevalar bilan muloqot:")
olma = Olma("Olma", "qizil", "Sog'lom va vitaminni.")
nok = Nok("Nok", "sabz", "Yuzi yumshoq va shirin.")
apelsin = Apelsin("Apelsin", "to'q sariq", "Yuzi yog'li va qaymoqli.")

print(f"Meva nomi: {olma.nomi}, Rangi: {olma.rangi}, Xususiyati: {olma.xususiyat}")
olma.eat()
olma.check_freshness()

print(f"\nMeva nomi: {nok.nomi}, Rangi: {nok.rangi}, Yuzi: {nok.yuzi}")
nok.eat()
nok.check_freshness()

print(f"\nMeva nomi: {apelsin.nomi}, Rangi: {apelsin.rangi}, Tuzilishi: {apelsin.tuzilishi}")
apelsin.eat()
apelsin.check_freshness()
