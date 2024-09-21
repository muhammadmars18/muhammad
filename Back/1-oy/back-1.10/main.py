# i = 10
# while i > -1:
#    print(i)
#    i = i-1

# i = 1
# yegindi = 0
# while i < 100:
#    print(i)
#    yegindi = yegindi + i
#    i += 2
# print(f"yegindi={yegindi}")



import random

maxfiy_raqam = random.randint(1, 10)

tahminlar = 0

for urinish in range(1, 4):
    kiritilgan_raqam = int(input("Raqam kiriting (1 dan 10 gacha): "))

    tahminlar += 1

    if kiritilgan_raqam == maxfiy_raqam:
        print(f"Tabriklaymiz! Siz {tahminlar} urinishdagi raqamni taxmin qildingiz!")
        break
    elif kiritilgan_raqam > maxfiy_raqam:
        print("Yashirin raqam kichikroq")
    else:
        print("Yashirin raqam kattaroq")

print("O'yin tugadi!")
