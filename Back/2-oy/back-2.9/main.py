 # 3 ta parametrga ega funksiya yarating
# 3 ta paramtr ham string bo'lsin
# funksiya berilgan 3 argumentdan 
# eng uzun stringni ekranga chiqarsin
# docstring yozishni unutmang



# def f(a:str, b:str, d:str):
#     '''
#     LEN UZUNLIK NI O'LCHASH UCUN KK
#     '''
#     print(
#         len()
#     )

# f('sALOM','EWRT','DESRDTFYGFDGDFBF')



import random

def generate_random_name(erkak_ismlari, ayol_ismlari):
    erkak_ismi = random.choice(erkak_ismlari)
    ayol_ismi = random.choice(ayol_ismlari)
    return erkak_ismi + ' ' + ayol_ismi

# Test qatorlari
erkak_ismlari = ["Ivan", "Aleksey", "Maksim"]
ayol_ismlari = ["Anna", "Ketrin", "Mariya"]

for _ in range(5):
    print(generate_random_name(erkak_ismlari, ayol_ismlari))

