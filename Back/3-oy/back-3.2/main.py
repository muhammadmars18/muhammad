# class Laptop:
#     brand = 'Apple Mac'
#     def __init__(self, name, color, chip_type) -> None:
#         self.name = name
#         self.color = color
#         self.chip_type = chip_type

#     def info(self):
#         return f"{self.name} | {self.chip_type}"

# mac1 = Laptop(name="Macbook Pro 16", color='Black', chip_type="M3 max")

# print(
#     Laptop.info(mac1)
# )
# print(mac1.info())

# print(
#     mac1.info()
# )
# def info(nimadur):
#     print(nimadur)


# info('kajsdlkfjaslkfdslkjskdl')

# task 2
'''
Person nomli class yarating
uning name atributi bo'lsin
va foydalanuvchidan ma'lumot kiritishini so'rang va 
va u asosida obyekt yarating
va uning name atributi ma'lumotini konsolga chiqaring
'''
# nimadur  = input('Ismingizni kiriting: ')
# nimadur1  = input('Familyangizni kiriting: ')

# class Person:
#     name = ''
#     def __init__(self, name, lastname) -> None:
#         self.name = name
#         self.lastname = lastname

#     def info(self):
#         return f"{self.name} | {self.lastname}"

# user = Person(name=nimadur, lastname=nimadur1)
# print(user.info())



# task 1.2
'''
Talaba classini yarating, uning ism, yosh, va guruh nomli attributlariga ega bo'lsin
va uning info nomli metodi bo'lsin
'''

# class Talaba:
#     def __init__(self, name, lastname, age, group) -> None:
#         self.name = name
#         self.lastname = lastname
#         self.age = age  
#         self.group = group
#     def info(self):
#         return f"{self.name} | {self.lastname} | {self.age} | {self.group}"


class Kitob:
    def __init__(self, nomi, muallifi, janri, nusxalar=1):
        self.nomi = nomi
        self.muallifi = muallifi
        self.janri = janri
        self.nusxalar = nusxalar
    
    def get_copy(self):
        self.nusxalar += 1
    
    def qaytarib_nusxa(self):
        if self.nusxalar > 0:
            self.nusxalar -= 1
        else:
            print("Uzr, bu kitob hozirda mavjud emas.")

class Kutubxona:
    def __init__(self):
        self.kitoblar = []
    
    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)
    
    def kitoblar_soni(self):
        return len(self.kitoblar)

kitob1 = Kitob("Sherlock Holmes", "Sir Arthur Conan Doyle", "Detektiv", 5)
kitob2 = Kitob("To'qimachilik", "Oybek O'tqulov", "Romantika")
kitob3 = Kitob("Tin Oy", "J.K. Rowling", "Fantastika", 3)

kutubxona = Kutubxona()

kutubxona.kitob_qoshish(kitob1)
kutubxona.kitob_qoshish(kitob2)
kutubxona.kitob_qoshish(kitob3)

print("Kitoblar soni avval: ", kutubxona.kitoblar_soni())

kitob1.get_copy()

kitob1.qaytarib_nusxa()

print("Kitoblar soni keyin: ", kutubxona.kitoblar_soni())
