# import random
# import time


# class Character:
#     def __init__(self, name, strength) -> None:
#         self.name = name
#         self.strength = strength
#         self.health = 100
    
#     def attack(self):
#         return random.randint(1, self.strength)



# class Game:
#     def __init__(self, player1: Character, player2: Character):
#         self.player1 = player1
#         self.player2 = player2

#     def start(self):
#         while True:
#             attack = random.choice(['player1', 'player2'])
#             if attack == 'player1':
#                 self.player2.health -= self.player1.attack()


class Mahsulot:
    def __init__(self, nomi, tannarxi, miqdori):
        self.nomi = nomi
        self.tannarxi = tannarxi
        self.miqdori = miqdori
    
    def mahsulot_malumoti(self):
        return f"Mahsulot: {self.nomi}, Narxi: {self.tannarxi} UZS, Miqdori: {self.miqdori}"

    def yangilash_miqdori(self, miqdor):
        self.miqdori += miqdor
        return self.miqdori


class Elektronika(Mahsulot):
    def __init__(self, nomi, tannarxi, miqdori, kafolat):
        super().__init__(nomi, tannarxi, miqdori)
        self.kafolat = kafolat
    
    def moslikni_tekshirish(self):
        return f"{self.nomi} moslik sertifikatiga ega."

class Kiyim(Mahsulot):
    def __init__(self, nomi, tannarxi, miqdori, olcham):
        super().__init__(nomi, tannarxi, miqdori)
        self.olcham = olcham
    
    def olchamini_ozgartirish(self, yangi_olcham):
        self.olcham = yangi_olcham
        return f"{self.nomi} yangi o'lchami: {self.olcham}"

class Kitob(Mahsulot):
    def __init__(self, nomi, tannarxi, miqdori, muallif):
        super().__init__(nomi, tannarxi, miqdori)
        self.muallif = muallif
    
    def kitob_muallifi(self):
        return f"{self.nomi} 'muallifi': {self.muallif}"
