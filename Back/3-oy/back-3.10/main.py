class Robot:
    def __init__(self, nomi, x=0, y=0, yonalish="yuqoriga"):
        self.nomi = nomi
        self.x = x
        self.y = y
        self.yonalish = yonalish
    
    def holatni_korsatish(self):
        print(f"Robot: {self.nomi}, Pozitsiya: ({self.x}, {self.y}), Yo'nalish: {self.yonalish}")
    
    def harakat(self, qadamlar):
        if self.yonalish == "yuqoriga":
            self.y += qadamlar
        elif self.yonalish == "pastga":
            self.y -= qadamlar
        elif self.yonalish == "chapga":
            self.x -= qadamlar
        elif self.yonalish == "o'ngga":
            self.x += qadamlar
        self.holatni_korsatish()
    
    def yonalishni_ozgartirish(self, yangi_yonalish):
        yonalishlar = ["yuqoriga", "pastga", "chapga", "o\'ngga"]
        if yangi_yonalish in yonalishlar:
            self.yonalish = yangi_yonalish
            print(f"Yo'nalish {yangi_yonalish}ga o'zgartirildi.")
        else:
            print("Noto'g'ri yo'nalish! Yo'nalishlar: yuqoriga, pastga, chapga, o'ngga")
        self.holatni_korsatish()

def asosiy():
    robot = Robot("Mars Rover")
    
    while True:
        print("\n1. Robot holatini ko'rsatish")
        print("2. Robotni harakatlantirish")
        print("3. Robot yo'nalishini o'zgartirish")
        print("4. Chiqish")
        
        tanlov = input("Tanlovni kiriting: ")
        
        if tanlov == '1':
            robot.holatni_korsatish()
        elif tanlov == '2':
            qadamlar = int(input("Qadamlar sonini kiriting: "))
            robot.harakat(qadamlar)
        elif tanlov == '3':
            yangi_yonalish = input("Yangi yo'nalishni kiriting (yuqoriga, pastga, chapga, o'ngga): ")
            robot.yonalishni_ozgartirish(yangi_yonalish)
        elif tanlov == '4':
            break
        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")

if __name__ == "__main__":
    asosiy()
