import pandas as pd
import psycopg2 as ps
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

class Poslasticarnica:
    def __init__(self):
        self.con = ps.connect(database='poslasticarnica',
                              port='5432',
                              user='postgres',
                              password='gio199491',
                              host='localhost')

        self.radnici = None

    def prikaz_Radnika(self):
        cursor = self.con.cursor()
        cursor.execute('SELECT * FROM RADNICI;')
        z = cursor.fetchall()
        for i in t1.get_children():
            t1.delete(i)
        for i in z:
            t1.insert('', END, values=i)

    def radnici_ex(self):
        self.radnici = pd.read_sql_query('SELECT * FROM RADNICI', self.con)
        self.radnici.to_excel('RADNICI.xlsx', index=False)

    def radnici_csv(self):
        self.radnici = pd.read_sql_query('SELECT * FROM RADNICI', self.con)
        self.radnici.to_csv('RADNICI.csv', index=False)

    def grafik_radnici(self):
        self.radnici = pd.read_sql_query('SELECT * FROM RADNICI', self.con)
        l = self.radnici.pozicija
        plt.pie(l, autopct='%1.2f%%')
        plt.title("Broj Radnika")
        plt.show()


root = Tk()
root.title('POSLASTICARNICA')

meni = Menu(root)
root.configure(menu=meni)

columns = ('ID', 'IME_PREZIME', 'POZICIJA', 'PLATA')
t1 = ttk.Treeview(root, columns=columns, show='headings')
t1.heading('ID', text='ID')
t1.heading('IME_PREZIME', text='IME_PREZIME')
t1.heading('POZICIJA', text='POZICIJA')
t1.heading('PLATA', text='PLATA')
t1.grid(row=0, column=0, rowspan=10, columnspan=4)

b2 = Button(root, text='promeni platu')
b2.grid(row=0, column=5)
b3 = Button(root, text='Promeni poziciju')
b3.grid(row=1, column=5)

P = Poslasticarnica()
P.prikaz_Radnika()

mainloop()
