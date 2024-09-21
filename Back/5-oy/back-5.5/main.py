import sqlite3


con = sqlite3.connect('baza.db')
oyna = con.cursor()

id_ = 0

def create_table():
    oyna.execute('''
    CREATE TABLE IF NOT EXISTS Talabalar (
        id INTEGER,
        first_name VARCHAR(120),
        last_name TEXT  
    )
    ''')

def insert_data(id_, first_name, last_name):
    oyna.execute(f'''
    INSERT INTO users (id, first_name, last_name)
    VALUES ({id_}, '{first_name}', '{last_name}')
    ''')


def delete_data(id_):
    oyna.execute(f"""DELETE FROM Talabalar WHERE id={id_}""")


def update_data(id_, first_name, last_name):
    oyna.execute(f"""UPDATE Talabalar
 SET 
                 first_name = '{first_name}' 
                 last_name = '{last_name}'
                 WHERE id={id_}x
                  """)

create_table()

print('actionni tanlang')

while True:
    choice = input('add, delete, update, exit: ')
    if choice == 'add':
        first_name = input("ismni kiriting: ")
        last_name = input('familiyani kiriting: ')
        id_ += 1
        insert_data(id_, first_name, last_name)
        
    elif choice == 'delete':
        id_ = int(input('Foydalanuvchi id sini kiriting: '))
        delete_data(id_)
    elif choice == 'update':
        up_data1 = str(input('Familyasini kiriting: '))
        up_data2 = str(input('Ismingizni kiriting: '))
        up_data3 = str(input('O\'zkartirmoqchi bolgan insoningizni id sini kiriting: '))
        
    elif choice == 'exit':
        break






con.commit()
con.close()
