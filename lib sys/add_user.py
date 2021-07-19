from tkinter import*
import mysql.connector

conn=mysql.connector.connect(host='localhost',database='name_of_the_database',user='root',password='add_password')
cursor=conn.cursor()

class add_user:
    def __init__(self,root):
        self.f=Frame(root.title("Add User Page"),height=700,width=600,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
        self.n=Label(text='ADD USER',fg="black",bg="dodgerblue3",font=('Calibri Bold',26))
        self.n1=Label(text='Name:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n2=Label(text='Lib ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n3=Label(text='Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n4=Label(text='Confirm Password:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n7=Label(text='Phone no:',fg="black",bg="dodgerblue3",font=('Calibri',14))
        self.n8=Label(text='Email ID:',fg="black",bg="dodgerblue3",font=('Calibri',14))

        self.b1=Button(text='ADD USER',fg='white',bg='dark red',width=20,height=2,command=lambda: self.buttonclick(0))

        
        self.e1=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e2=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e3=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e4=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e5=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))
        self.e6=Entry(self.f,width=25,fg="black",bg="white",font=('Calibri',14))

            

        self.n.place(x=200,y=0)    
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
        
        if(self.e4.get()!=self.e3.get()):
            self.n5=Label(text='Password did not match',font=('Calibri',14),fg='red')
            self.n5.place(x=50,y=400)
            num=1
  
        print(num)    
        a=self.e1.get()
        b=self.e2.get()
        c=self.e3.get()
        d=self.e5.get()
        e=self.e6.get()

        if(num==0):
            sql_insert_query = " insert into info VALUES (%s,%s,%s,%s,%s,%s)"

            insert_tuple_1 = (a, b, c, d, e, 0)


            cursor.execute(sql_insert_query, insert_tuple_1)
            conn.commit()
            cursor.close()
            conn.close()

        else:
            return 

            
def ad_us():
    root=Tk()

    mb=add_user(root)

    root.mainloop()


        
        











            
            
