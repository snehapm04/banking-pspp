from tkinter import *
from tkinter import messagebox
import os
w=Tk()
w.geometry("600x400")
w.title("Banking")
bg = PhotoImage(file = "pic2.png")
Label( w, image = bg).place(x = 0, y = 0)
l=Label(w,text="XYZ Banking Services",bg="#B8E2F2",font=("Arial Bold", 25))
l.place(x=50,y=0)
def w2():
    def submit2():
        acc=os.listdir()
        name=f1.get()    
        if name=="" or f2.get()=="" or f3.get()=="" or f4.get()=="" or f5.get()=="" or f6.get()=="":
            l1=Label(w2,text="All fields are required",fg="red",bg="#B8E2F2",font=("Arial Bold", 15))
            l1.place(x=300,y=270)
        else:
            for i in acc:
                if name==i:
                    l2=Label(w2,text="Account already exists",fg="red",bg="#B8E2F2",font=("Arial Bold", 15))
                    l2.place(x=300,y=270)               
                else:
                    t2file= open(name, "w")
                    t2file.write(f1.get()+"\n")
                    t2file.write(f2.get()+"\n")
                    t2file.write(f3.get()+"\n")
                    t2file.write(f4.get()+"\n")
                    t2file.write(f5.get()+"\n")
                    t2file.write(f6.get()+"\n")
                    t2file.write("0"+"\n")
                    t2file.close()
                
    w2=Tk()
    w2.title("Sign up Page")
    w2.geometry("600x450")
    w2.configure(bg="#B8E2F2")
    Label(w2,text="Welcome to our bank",bg="#B8E2F2",font=("Arial Bold", 25)).place(x=120,y=0)
    Label(w2,text="Name:",bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=50)
    f1=Entry(w2)
    f1.place(x=50,y=100)
    Label(w2,text="Phone Number:",bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=150)
    f2=Entry(w2)
    f2.place(x=50,y=200)
    Label(w2,text="Address:",bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=250)
    f3=Entry(w2)
    f3.place(x=50,y=300)
    Label(w2,text="Age:",bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=350)
    f4=Entry(w2)
    f4.place(x=50,y=400)
    Label(w2,text="Email:",bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=250,y=50)
    f5=Entry(w2)
    f5.place(x=250,y=100)
    Label(w2,text="Password:",bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=250,y=150)
    f6=Entry(w2)
    f6.place(x=250,y=200)
    Button(w2,text="Submit",font=("Arial Bold", 15),command=submit2).place(x=300,y=300)
    w2.mainloop()

def check():
    acc=os.listdir()
    name=e1.get()
    pw=e2.get()
    def deposit():
        def finish():
            if g1.get()=="":
                Label(depositscreen,text="Amount required",font=("Trebuchet MS", 20)).pack()
            elif float(g1.get())<=0:
                l3=Label(depositscreen,text="Negative amount not allowed",font=("Trebuchet MS", 20))
                l3.pack()
            file=open(name,"r+")
            filedata=file.read()
            filedatas=filedata.split("\n")
            
            cbal=filedatas[6]
            ubal=cbal
            ubal=float(ubal)+float(g1.get())
            filedata=filedata.replace(cbal,str(ubal))
            file.seek(0)
            file.truncate(0)
            file.write(filedata)
            file.close()
            Label(depositscreen,text="Current Balance: Rs"+str(ubal),font=("Trebuchet MS", 20)).pack()
            Label(depositscreen,text="Balance updated",font=("Trebuchet MS", 20)).pack()                               
        file=open(name,"r")
        filedata=file.read()
        filedata=filedata.split("\n")
        bal=filedata[6]
        depositscreen=Tk()
        depositscreen.title("Deposit")
        Label(depositscreen,text="Deposit",font=("Trebuchet MS", 20)).pack()
        Label(depositscreen,text="Current balance: Rs"+bal,font=("Trebuchet MS", 20)).pack()
        Label(depositscreen,text="Amount",font=("Trebuchet MS", 20)).pack()
        g1=Entry(depositscreen)
        g1.pack()
        Button(depositscreen,text="Finish",command=finish,font=("Arial Bold", 20)).pack()

    def withdraw():
        def finish1():
            if g2.get()=="":
                Label(withscreen,text="Amount required",font=("Trebuchet MS", 20)).pack()
            elif float(g2.get())<=0:
                Label(withscreen,text="Negative amount not allowed",font=("Trebuchet MS", 20)).pack()
            file=open(name,"r+")
            filedata=file.read()
            filedatas=filedata.split("\n")
            
            cbal=filedatas[6]
            if float(g2.get())>float(cbal):
                Label(withscreen,text="Insufficient Fund",font=("Trebuchet MS", 20)).pack()
            else:
                
                ubal=cbal
                ubal=float(ubal)-float(g2.get())
                filedata=filedata.replace(cbal,str(ubal))
                file.seek(0)
                file.truncate(0)
                file.write(filedata)
                file.close()
                Label(withscreen,text="Current Balance: Rs"+str(ubal),font=("Trebuchet MS", 20)).pack()
                Label(withscreen,text="Balance updated",font=("Trebuchet MS", 20)).pack()               
            

        file=open(name,"r")
        filedata=file.read()
        filedata=filedata.split("\n")
        bal=filedata[6]
        withscreen=Tk()
        withscreen.title("Withdraw")
        Label(withscreen,text="Withdrawal",font=("Trebuchet MS", 20)).pack()
        Label(withscreen,text="Current balance: Rs"+bal,font=("Trebuchet MS", 20)).pack()
        Label(withscreen,text="Amount to be withdrawn",font=("Trebuchet MS", 20)).pack()
        g2=Entry(withscreen)
        g2.pack()
        Button(withscreen,text="Finish",font=("Arial Bold", 20),command=finish1).pack()            
    for i in acc:
        if i ==name:
            file=open(name,"r")
            filedata=file.read()
            filedata=filedata.split("\n")
            password=filedata[5]
            if pw==password:
                w3=Tk()
                w3.title("Banking")
                w3.geometry("600x500")
                w3.configure(bg="#B8E2F2")
                Label(w3,text="Account details",bg="#B8E2F2",font=("Trebuchet MS", 25)).place(x=150,y=0)
                Label(w3,text="Welcome "+name+" ! ",bg="#B8E2F2",font=("Trebuchet MS", 20)).place(x=100,y=50)
                file=open(name,"r")
                Label(w3,text="Name : "+filedata[0],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=100)
                Label(w3,text="Phone Num :  "+filedata[1],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=150)
                Label(w3,text="Address : "+filedata[2],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=200)
                Label(w3,text="Age : "+filedata[3],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=250)
                Label(w3,text="Email ID : "+filedata[4],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=300)
                Label(w3,text="Password : "+filedata[5],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=350)
                Label(w3,text="Balance : Rs "+filedata[6],bg="#B8E2F2",font=("Trebuchet MS", 15)).place(x=50,y=400)
                
                Button(w3,text="Deposit",font=("Arial Bold", 15),command=deposit).place(x=370,y=200)
                Button(w3,text="Withdraw",font=("Arial Bold", 15),command=withdraw).place(x=370,y=300)
            else:
                messagebox.showerror("Error","Password incorrect")
                file.close()    
Label(w,text="Name",bg="#B8E2F2",font=("Arial Bold", 15)).place(x=50,y=100)
e1=Entry(w)
e1.place(x=150,y=100)
Label(w,text="Password",bg="#B8E2F2",font=("Arial Bold", 15)).place(x=40,y=150)
e2=Entry(w,show="*")
e2.place(x=150,y=150)
Button(w,text="Submit",font=("Arial Bold", 15),command=check).place(x=120,y=230)
Button(w,text="Create a new account",font=("Arial Bold", 15),command=w2).place(x=300,y=250)
w.mainloop()
