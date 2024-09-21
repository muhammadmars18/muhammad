# students = {
#    ' oqishjoyi':'Mars It school',
#     1:'O\'quvchi',
#     'name':'Muhammad',
#     'lastname':'Doniyorov',
#     'id':546416,

#     ' oqishjoyi':'Mars It school',
#     2:'O\'quvchi',
#     'name':'Aziz',
#     'lastname':'Anvarov',
#     'id':546417,

#     ' oqishjoyi':'Mars It school',
#     3:'O\'quvchi',
#     'name':'Ibrohim',
#     'lastname':'Rahimjoniv',
#     'id':546418,    
# }

mahsulotlar = {"olma": 5, "banan": 3, "uzum": 8, "shaftoli": 2}

mahsulot_nom = input("Qaysi mahsulotni qidirmoqdasiz? ")

if mahsulot_nom in mahsulotlar:
    print(f"{mahsulot_nom.capitalize()} {mahsulotlar[mahsulot_nom]} kg bor")
else:
    print(f"{mahsulot_nom.capitalize()} yo'q")

davlatlar_aholi = {"O'zbekiston": 34, "Rossiya": 144, "AQSh": 328, "Kanada": 37}

davlat_nom = input("Qaysi davlatning aholisini bilmoqchisiz? ")

if davlat_nom in davlatlar_aholi:
    if davlatlar_aholi[davlat_nom] < 50:
        print("Kichik aholi")
    elif davlatlar_aholi[davlat_nom] < 100:
        print("O'rta aholi")
    else:
        print("Katta aholi")
else:
    print("Bunday davlat mavjud emas")

davlatlar_poytaxtlar = {"O'zbekiston": "Toshkent", "Rossiya": "Moskva", "AQSh": "Washington", "Fransiya": "Parij"}

davlat_nom = input("Qaysi davlatning poytaxtini bilmoqchisiz? ")

if davlat_nom in davlatlar_poytaxtlar:
    print(f"{davlat_nom}ning poytaxti: {davlatlar_poytaxtlar[davlat_nom]}")
else:
    print("Bunday davlat mavjud emas")

meva_ranglar = {"olma": "qizil", "banan": "sariq", "anor": "yashil", "shaftoli": "sariq"}

meva_nom = input("Qaysi mevani rangini bilmoqchisiz? ")

if meva_nom in meva_ranglar:
    if meva_ranglar[meva_nom] == "":
        print("Bu meva nomalum rangda")
    else:
        print(f"Bu {meva_ranglar[meva_nom]} {meva_nom}")
else:
    print("Bunday meva mavjud emas")

filmlar_reytinglar = {"Titanik": 7.8, "Interstellar": 8.6, "Inception": 8.8, "Forrest Gump": 8.9}

for film, reyting in filmlar_reytinglar.items():
    if reyting > 8.5:
        print(f"{film}ning yuqori reytingi: {reyting}")
    else:
        print(f"{film}ning normal reytingi: {reyting}")


