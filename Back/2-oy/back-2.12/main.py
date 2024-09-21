# task 1.1
# istalgancha sonlarni qabul qilib ularning
# ko'paytmasi hisoblab qaytaradigan funksiya yarating


# def kupaytr(*args):
#     hammasi = 1
#     for i in args:
#         hammasi = hammasi * i
#     print(hammasi)

# kupaytr(1,2,3,4,5)
# print(
#     kupaytr(1,2,-3,-12, 23, 123123123)
# )


# task 1.2
# istalgancha son qabul qiladigan funksiya
# yarating , funksiyaga  berilgan ko'p argumentlar
# tuple sifatida qabul qilinadi, 
# vazifa shuki shu berilgan tupledagi eng katta
# sonning indeksini qaytarib bering

def find_max_index(*args):
    find_max_index(21, 122, 0, 987, 13, 12312312321,1)
    max(find_max_index)

    print(max(find_max_index).index)

find_max_index










import random

def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    return random_numbers

tasodifiy_raqamlar = generate_random_numbers()

print("Tasodifiy raqamlar:")
print(tasodifiy_raqamlar)


import random

def guess_number_game():
    target_number = random.randint(1, 50)
    attempts = 0

    print("Men 1 dan 50 gacha bo'lgan bir son o'yladim. Uni topasizmi?")

    while attempts < 5:
        guess = int(input("Raqamni toping (1-50 oraliqda): "))
        attempts += 1

        if guess < target_number:
            print("Kichikroq!")
        elif guess > target_number:
            print("Ko'proq!")
        else:
            print(f"Tabriklaymiz, siz {attempts} ta urinishda raqamni topdingiz!")
            return attempts

    print("Siz belgilangan urinishlar sonida raqamni topa olmadingiz!")
    return attempts

urinishlar_soni = guess_number_game()
print(f"Siz {urinishlar_soni} ta urinishda topdingiz!")


