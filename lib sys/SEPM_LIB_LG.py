from tkinter import*
from Lib_manag_sys_SEPM import *
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='name_of_the_database',user='root',password='add_password')
cursor=conn.cursor()
conn.commit()
class login:
        
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Login Page"),height=700,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n=Label(text='Welcome to ABC Library',bg='dodgerblue3',font=('Calibri',22))
        self.n1=Label(text='Lib ID:',bg='dodgerblue3',font=('Calibri',14))
        self.n2=Label(text='Password:',bg='dodgerblue3',font=('Calibri',14))

        self.b1=Button(text='Login',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))

        
        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))

        self.n.place(x=100,y=50)
        self.n1.place(x=50,y=150)
        self.e1.place(x=150,y=150)
        self.n2.place(x=50,y=200)
        self.e2.place(x=150,y=200)

        self.b1.place(x=150,y=250)


    def buttonclick(self,num):
        a=self.e1.get()
        b=self.e2.get()
        flag=0
        if(num==0):
            rows="select * from info where libID=%s and pswd=%s"
            cursor.execute(rows,(a,b))
            rows=cursor.fetchall()
            print(rows)
            if (rows):
                self.root.destroy()
                mp()
            
            else:
                self.n4=Label(text='invalid Username or Password',font=('Calibri',14))
                print('invalid Username or Password')
                self.n4.place(x=100,y=300)
                self.root.destroy()
                SEPM_LIB_LG()
            cursor.close()
            conn.close()
        else:
            self.root.destroy()
               

def SEPM_LIB_LG():
    root=Tk()

    mb=login(root)

    root.mainloop()


        
        











            
            
