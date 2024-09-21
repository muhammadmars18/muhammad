def create_friends_dict():
    friends = {}
    while True:
        ism = input("Do'stingiz ismini kiriting (chiqish uchun 'exit' ni bosing): ")
        if ism.lower() == 'exit':
            break
        yosh = input("Do'stingiz yoshini kiriting: ")
        friends[ism] = yosh
    return friends

dostlar = create_friends_dict()
print(dostlar)




def sum_numbers_in_list():
    raqamlar = input("Raqamlar ro'yxatini kiriting (bo'shliq joy orqali ajratib chiqish uchun): ").split()
    raqamlar = [int(x) for x in raqamlar]
    return sum(raqamlar)

print(sum_numbers_in_list())




def remove_duplicates():
    royxat = input("Ro'yxatni kiriting (raqamlar orasida vergullar bilan ajratilgan): ").split(',')
    royxat = list(set(royxat))
    return royxat

print(remove_duplicates())








