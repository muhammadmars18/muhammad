# task1.1 
# ikta son qabul qiladigan va ularning yig'indisini 
# konsolga chiqaradigan funksiya yarating
# funksiyaga tushunarli va qilayotgan vazifasiga qarab
# qulayroq nom bering


# def hisob(njs, mjs):
#     print(njs + mjs)

# njs = 2
# mjs = 5

# hisob(njs, mjs)







# task1.2
# to'rburchak yuzini hisoblaydigan va uni konsolga
# chiqaradigan funksiya yarating


# def hisob(son1, son2):
#     print(son1 * son2)

# son1 = 2
# son2 = 5

# hisob(son1, son2)

def say_salom(name):
    print(f"Salom, {name}!")

say_salom("Ali")   
say_salom("Bobur") 
say_salom("Diana") 





def hisoblash_sum(a, b):
    return a + b

print(hisoblash_sum(5, 3))   # 8
print(hisoblash_sum(10, -2)) # 8
print(hisoblash_sum(0, 0))   # 0





def chop_etish_royxati_raqamlar(raqamlar):
    for raqam in raqamlar:
        print(raqam)

raqamlar = [3, 7, 12, -5]
chop_etish_royxati_raqamlar(raqamlar)




def juft(raqam):
    if raqam % 2 == 0:
        return "true"
    else:
        return "false"

print(juft(6))  
print(juft(3))  
print(juft(0))  




def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

print_numbers(1, 5)   
print_numbers(-3, 2)  
print_numbers(0, 10)  
