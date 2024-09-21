import sqlite3 


con = sqlite3.connect('baza.db')
oyna = con.cursor()


oyna.execute('''
CREATE TABLE IF NOT EXISTS Talabalar (
    id INTEGER,
    ismi TEXT,
    guruxi INTEGER,
    coin INTEGER,
    manzil TEXT
                )
''')


oyna.execute('''
INSERT INTO Talabalar
(id, ismi, guruxi, coin, manzil)
VALUES
(8, 'Muhammad', 1145, 764, 'olmazor')
''')

oyna.execute('''
INSERT INTO Talabalar
(id, ismi, guruxi, coin, manzil)
VALUES
(10, 'Aziz', 1145, 555, 'dadil')
''')

oyna.execute('''
INSERT INTO Talabalar
(id, ismi, guruxi, coin, manzil)
VALUES
(12, "Abdug\'ofir", 1145, 753, 'Ibn sino')
''')


# oyna.execute(
#     ''' 
# UPDATE Talabalar
# SET ismi='Olim', guruxi=1146, coin=999 WHERE id=8
# '''
# )

# oyna.execute(
#     ''' 
# UPDATE Talabalar
# SET ismi='Hamidullo', guruxi=1234, coin=888 WHERE id=10
# '''
# )

# oyna.execute(
#     ''' 
# UPDATE Talabalar
# SET ismi='Abduvoris', guruxi=9876, coin=555 WHERE id=12
# '''
# )

# oyna.execute(""" DELETE FROM Talabalar WHERE id=10""")
# oyna.execute(""" DELETE FROM Talabalar WHERE id=12""")

oyna.execute(""" DELETE FROM Talabalar WHERE id=8 """)

con.commit()
con.close()
