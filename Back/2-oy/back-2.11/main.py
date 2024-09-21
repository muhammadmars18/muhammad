


import random

def guess_number_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Raqamni toping (1-100 oraliqda): "))
        attempts += 1

        if guess < target_number:
            print("Kichikroq!")
        elif guess > target_number:
            print("Ko'proq!")
        else:
            print(f"Tabriklaymiz, siz {attempts} ta urinishda raqamni topdingiz!")
            return attempts

print("Men 1 dan 100 gacha bo'lgan bir son o'yladim. Uni topasizmi?")
urinishlar_soni = guess_number_game()
print(f"Siz {urinishlar_soni} ta urinishda topdingiz!")


 