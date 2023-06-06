from tkinter import*
from tkinter import ttk
import pandas as pd
import psycopg2 as ps
import matplotlib.pyplot as plt


root=Tk()
root.title('POSLASTICARNICA')

meni=Menu(root)
podmeni1=Menu(meni,tearoff=0)
meni.add_cascade(label="Edit",menu=podmeni1)
podmeni1.add_command(label="Dodaj",command=lambda:t3())
podmeni1.add_command(label="Obrisi",command=lambda:t2())


podmeni2=Menu(meni,tearoff=0)
meni.add_cascade(label="Export",menu=podmeni2)
podmeni2.add_command(label="Export to excel", command=lambda:P.radnici_ex())
podmeni2.add_command(label="Export to csv", command=lambda:P.radnici_csv())


podmeni3=Menu(meni,tearoff=0)
meni.add_cascade(label="View",menu=podmeni3)
podmeni3.add_command(label="Barplot")
podmeni3.add_command(label="Piechart",command=lambda:P.grafik_radnici)

podmeni4=Menu(meni,tearoff=0)
meni.add_cascade(label="Option",menu=podmeni4)
podmeni4.add_command(label="Exit", command=root.destroy)

root.configure(menu=meni)

columns=('ID','IME_PREZIME','POZICIJA','PLATA')
t1=ttk.Treeview(root,columns=columns,show='headings')
t1.heading('ID',text='ID')
t1.heading('IME_PREZIME',text='Ime & Prezime')
t1.heading('POZICIJA',text='Pozicije')
t1.heading('PLATA',text='Plata')
t1.grid(row=0,column=0,rowspan=10,columnspan=4)

b2=Button(root,text='Promeni Platu',command=lambda:t4())
b2.grid(row=0,column=5)
b3=Button(root,text='Promeni Poziciju',command=lambda:t5())
b3.grid(row=1,column=5)

def t2():
    t=Toplevel()
    l=Label(t,text='Unesite ime radnika koga zelite da izbrisete')
    l.pack()
    e=Entry(t)
    e.pack()
    B=Button(t,text='Izbrisi radnika',command=lambda:P.ponisti_radnika(e.get()))
    B.pack()

def t3():
    t=Toplevel()
    l=Label(t,text='Unesite ime radnika koga zelite da dodate')
    l.pack()
    e=Entry(t)
    e.pack()
    l1=Label(t,text='Unesite Poziciju radnika koga zelite da dodate')
    l1.pack()
    e2=Entry(t)
    e2.pack()
    l2=Label(t,text="Unesite Platu radnika koga zelite da dodate")
    l2.pack()
    e3=Entry(t)
    e3.pack()
    B=Button(t,text='Dodaj radnika',command=lambda:P.dodaj_radnika(e.get(),e2.get(),e3.get()))
    B.pack()

def t4():
    t=Toplevel()
    l=Label(t,text='Promeni platu radnika')
    l.pack()
    e=Entry(t)
    e.pack()
    l1=Label(t,text='Unesite ID radnika')
    l1.pack()
    e1=Entry(t)
    e1.pack()
    B=Button(t,text='Promeni Platu',command=lambda:P.promeni_platu(e.get(),e1.get()))
    B.pack()

def t5():
    t=Toplevel()
    l=Label(t,text='Promeni poziciju radnika')
    l.pack()
    e=Entry(t)
    e.pack()
    l1=Label(t,text='Unesite ID radnika')
    l1.pack()
    e1=Entry(t)
    e1.pack()
    B=Button(t,text='Promeni poziciju',command=lambda:P.promeni_poziiju(e.get(),e1.get()))
    B.pack()



class Poslasticarnica:
    def __init__(self):
        self.con=ps.connect(database='poslasticarnica',
                           port='5432',
                           user='postgres',
                           password='gio199491',
                           host='localhost')
        
        self.radnici=None

    def prikaz_Radnika(self):
        cursor=self.con.cursor()
        cursor.execute('SELECT*FROM RADNICI;')
        z=cursor.fetchall()
        for i in t1.get_children():
            t1.delete(i)
        for i in z:
            t1.insert('',END,values=i)

    def radnici_ex(self):
        self.radnici=pd.read_sql_query('SELECT*FROM RADNICI',self.con)
        self.radnici.to_excel('RADNICI.xlsx',index=False)

    def radnici_csv(self):
        self.radnici=pd.read_sql_query('SELECT*FROM RADNICI',self.con)
        self.radnici.to_csv('RADNICI.csv',index=False)
    
    
    def grafik_radnici(self):
        self.radnici=pd.read_sql_query('SELECT*FROM RADNICI',self.con)
        l=self.radnici.pozicija
        
        
        plt.pie(l,autopct='%1.2f.%%')
        plt.title="Broj Radnika"
        plt.show()


    def ponisti_radnika(self,IME_PREZIME):
        cursor=self.con.cursor()
        cursor.execute('''DELETE FROM RADNICI WHERE IME_PREZIME='{}';'''.format(IME_PREZIME))
        self.con.commit()
        self.prikaz_Radnika()

    def dodaj_radnika(self,IME_PREZIME,POZICIJA,PLATA):
        cursor=self.con.cursor()
        cursor.execute('''INSERT INTO RADNICI(IME_PREZIME,POZICIJA,PLATA) VALUES ('{}','{}',{})'''.format(IME_PREZIME,POZICIJA,PLATA))
        self.con.commit()
        self.prikaz_Radnika()



    def promeni_platu(self,PLATA,ID):
        cursor=self.con.cursor()
        cursor.execute('''UPDATE RADNICI SET PLATA={} WHERE ID = {}'''.format(PLATA,ID))
        self.con.commit()
        self.prikaz_Radnika()

    def promeni_poziiju(self,POZICIJA,ID):
        cursor=self.con.cursor()
        cursor.execute('''UPDATE RADNICI SET POZICIJA='{}' WHERE ID = {}'''.format(POZICIJA,ID))
        self.con.commit()
        self.prikaz_Radnika()










P=Poslasticarnica()
P.prikaz_Radnika()


mainloop()