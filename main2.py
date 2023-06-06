from tkinter import *
from klase import *

root=Tk()

def confirmation(odabir,searched):
    t=Toplevel(root)
    t_l=Label(t,text="Odaberite tip fajla").pack()
    t_b=Button(t,text='CSV')
    t_b.pack()
    t_b1=Button(t,text="Excel")
    t_b1.pack()
    t_l1=Label(t,text="")
    t_l1.pack()
    if odabir=='all':
        t_b.configure(command=lambda:t_l1.configure(text=A.export_all('csv')))
        t_b1.configure(command=lambda:t_l1.configure(text=A.export_all('excel')))
    else:
        t_b.configure(command=lambda:t_l1.configure(text=A.export_searched(int(searched),'csv')))
        t_b.configure(command=lambda:t_l1.configure(text=A.export_searched(int(searched),'excel')))


e=Entry(root)
e.pack()
b=Button(root,text="Search and export",command=lambda:confirmation('s',e.get())).pack()
b1=Button(root,text="Export all",command=lambda:confirmation('all',None)).pack()

mainloop()