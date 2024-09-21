import sqlite3 


con = sqlite3.connect('baza.db')
oyna = con.cursor()


oyna.execute('''
CREATE TABLE IF NOT EXISTS Contacts (
    First_name TEXT,
    Last_name Text,
    Age INTEGER,
    Profession VARCHAR(120),
    Phone_number VARCHAR(20),
    Interersts VARCHAR(255)
                ):
''')

oyna.execute = '''
INSERT INTO Contacts(First_name,Last_name, Age,Profession,Phone_number,Interersts) '''
VALUES
