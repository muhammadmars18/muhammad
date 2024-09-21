# Online Store System
# │
# ├── Product
# │    ├── Name
# │    ├── Price
# │    └── Category
# │
# ├── Customer
# │    ├── Name
# │    ├── Address
# │    └── Email
# │
# ├── Order
# │    ├── Customer (Reference to Customer)
# │    ├── ShoppingCart (Reference to ShoppingCart)
# │    └── OrderStatus
# │
# ├── ShoppingCart
# │    ├── Customer (Reference to Customer)
# │    ├── Products (Collection of Products)
# │    └── TotalAmount

# class Product:
#     def __init__(self, price, name, category) -> None:
#         self.price = price
#         self.name = name
#         self.category = category
#     def info(self):
#         return f"narxi: {self.price} | nomi: {self.name} | kategoriyasi: {self.category}"

# product1 = Product(price = 1.000, name = "Kepka", category = "Kiyim-kechak")


# class Customer:
#     def __init__(self, name, address, email):
#         self.name = name
#         self.address = address
#         self.email = email

# customer1 = Customer(name = 'muhammad', address = 'Tashkent', email = 'm4407278@gmail.com') 

 



# class Order:
#     def init(self, shoppingcart, orderstatus) -> None:
#         self.shoppingcart = shoppingcart
#         self.orderstatus = orderstatus
#     def info(self):
#         return f"Order: orderstatus: {self.orderstatus} shoppingcart: {self.shoppingcart}"


# class ShoppingCart:
#     def __init__(self, customer: Customer) -> None:
#         self.customer = customer
#         self.products = []
#         self.total = 0
    
#     def add_product(self, product: Product):
#         self.products.append(product)
#         self.total += product.price

#     def get_customer(self):
#         return self.customer







class Talaba:
    def __init__(self, ismi, yoshi):
        self.ismi = ismi
        self.yoshi = yoshi
        self.fanlar = []

    def fan_qoshish(self, fan):
        self.fanlar.append(fan)
    
    def fanlar_royxati(self):
        if not self.fanlar:
            print(f"{self.ismi}ning hech qanday fanlari yo'q.")
        else:
            print(f"{self.ismi} o'rganayotgan fanlar:")
            for fan in self.fanlar:
                print(f"{fan.nomi} - {fan.daraja} daraja")

    def gpa_hisoblash(self):
        if not self.fanlar:
            return 0.0
        umumiy_baho = sum(fan.daraja for fan in self.fanlar)
        return umumiy_baho / len(self.fanlar)

class Fan:
    def __init__(self, nomi, daraja):
        self.nomi = nomi
        self.daraja = daraja

def asosiy():
    matematika = Fan("Matematika", 90)
    tarix = Fan("Tarix", 85)
    adabiyot = Fan("Adabiyot", 92)
    kimyo = Fan("Kimyo", 88)

    talaba1 = Talaba("Ali", 20)
    talaba2 = Talaba("Vali", 22)

    talaba1.fan_qoshish(matematika)
    talaba1.fan_qoshish(tarix)
    talaba1.fan_qoshish(adabiyot)

    talaba2.fan_qoshish(kimyo)
    talaba2.fan_qoshish(tarix)
    talaba2.fan_qoshish(matematika)

    talaba1.fanlar_royxati()
    talaba2.fanlar_royxati()

    print(f"{talaba1.ismi}ning GPA: {talaba1.gpa_hisoblash()}")
    print(f"{talaba2.ismi}ning GPA: {talaba2.gpa_hisoblash()}")

    yuqori_baho = max(talaba1.gpa_hisoblash(), talaba2.gpa_hisoblash())
    past_baho = min(talaba1.gpa_hisoblash(), talaba2.gpa_hisoblash())

    if talaba1.gpa_hisoblash() == yuqori_baho:
        print(f"Yuqori o'rtacha ball olgan talaba: {talaba1.ismi}")
    else:
        print(f"Yuqori o'rtacha ball olgan talaba: {talaba2.ismi}")

    if talaba1.gpa_hisoblash() == past_baho:
        print(f"Past o'rtacha ball olgan talaba: {talaba1.ismi}")
    else:
        print(f"Past o'rtacha ball olgan talaba: {talaba2.ismi}")

if __name__ == "__main__":
    asosiy()
