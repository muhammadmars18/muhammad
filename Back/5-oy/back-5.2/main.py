import sqlite3


aloqa = sqlite3.connect("baza.db")
kursor = aloqa.cursor()

sql_kod = '''
CREATE TABLE IF NOT EXISTS students (
    ism text,
    familiya text,
    guruh text,
):
'''

sql_kod = '''
INSERT INTO students(ism,familya,yosh,guruh)
VALUES
('Abdulvoris', 'Bahtiyorov',  '1145')
('Aziz', 'Anvarov',  '1145')
('Umar', 'Bahtiyorov',  '1145')
('Abdug\'ofur', 'Anvarov',  '1145')
('Hamidullo', 'Isroiljonov',  '1145')
('Ibrohim', 'Rahimjonov',  '1145')
('Abdulaziz', 'Ilhomov',  '1145')
('Muhammad', 'Doniyorov',  '1145')
('Amirxon', 'Miraliyev',  '1145')
('Abduhalilov', 'Shaxzod',  '1145')
'''