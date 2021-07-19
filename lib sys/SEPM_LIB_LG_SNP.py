from tkinter import*
from SEPM_LIB_SNP import *
from SEPM_LIB_LG import *

import mysql.connector
conn=mysql.connector.connect(host='localhost',database='name_of_the_database',user='root',password='add_password')
cursor=conn.cursor()
conn.commit()

class startpg:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Start Page"),height=500,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()

        self.n1=Label(text='ABC Library',bg='dodgerblue3',font=('Bold Calibri',30))
    
        self.b1=Button(text='Login',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(0))
        self.b2=Button(text='Sign Up',fg='white',bg='dark red',width=20,height=2,font=('Calibri',15),command=lambda: self.buttonclick(1))

        self.n1.place(x=200,y=50)
        self.b1.place(x=200,y=150)
        self.b2.place(x=200,y=250)


    def buttonclick(self,num):
        if(num==1):
            self.root.destroy()
            SEPM_LIB_SNP()
            cursor.close()
            conn.close()
            
        elif(num==0):
            self.root.destroy()
            SEPM_LIB_LG()
            cursor.close()
            conn.close()
            
            

root=Tk()

mb=startpg(root)

root.mainloop()
