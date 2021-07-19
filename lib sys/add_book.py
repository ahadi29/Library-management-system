from tkinter import*
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='name_of_the_database',user='root',password='add_password')
cursor=conn.cursor()

class add_book:
    def __init__(self,root):
        self.f=Frame(root.title("Add Book Page"),height=500,width=800,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n=Label(text='ADD BOOK',fg="black",bg="dodgerblue3",font=('Calibri Bold',26))
        self.n1=Label(text='Title:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n2=Label(text='Author:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='Publication:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n4=Label(text='Category:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n7=Label(text='Book ID Number :',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n8=Label(text='Price:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='ADD BOOK',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))
 
        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e3=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e4=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e5=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e6=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))    

        self.n.place(x=300,y=25)    
        self.n1.place(x=50,y=100)
        self.e1.place(x=250,y=100)
        self.n2.place(x=50,y=150)
        self.e2.place(x=250,y=150)
        self.n3.place(x=50,y=200)
        self.e3.place(x=250,y=200)
        self.n4.place(x=50,y=250)
        self.e4.place(x=250,y=250)
        self.n7.place(x=50,y=300)
        self.e5.place(x=250,y=300)
        self.n8.place(x=50,y=350)
        self.e6.place(x=250,y=350)
        self.b1.place(x=300,y=450)

    def buttonclick(self,num):
        a=self.e1.get()
        b=self.e2.get()
        c=self.e3.get()
        d=self.e4.get()
        e=self.e5.get()
        f=self.e6.get()
        
        if(num==0):
            print(1)
            sql_insert_book = " insert into books VALUES (%s,%s,%s,%s,%s,%s)"
            print(2)
            insert_tuple_1 = (a, b, c, d, e, f)

            cursor.execute(sql_insert_book, insert_tuple_1)
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return 

def ad_bk():   
    root=Tk()

    mb=add_book(root)

    root.mainloop()

