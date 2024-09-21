import sqlite3 


con = sqlite3.connect('baza.db')
oyna = con.cursor()



def create_table():
    oyna.execute = '''
CREATE TABLE IF NOT EXISTS Talabalar (
    ism TEXT,
    familiya TEXT,
    guruh INTEGER,
    grade INTEGER
):
'''

oyna.execute = '''
INSERT INTO students(ism,familya,guruh,grade)
VALUES
('Abdulvoris', 'Bahtiyorov',  1145, 45),
('Aziz', 'Anvarov',  1145, 70),
('Umar', 'Bahtiyorov',  1145, 60),
('Abdug\'ofur', 'Toxirov',  1145, 80),
('Hamidullo', 'Isroiljonov',  1145, 90),
('Ibrohim', 'Rahimjonov',  1145, 30),
('Abdulaziz', 'Ilhomov',  1145,75 ),
('Muhammad', 'Doniyorov',  1145e, 85),

            

'''

con.commit()
con.close()
