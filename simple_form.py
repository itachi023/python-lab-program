# button label  entry
from tkinter import *
from tkinter import messagebox
root = Tk()

var=StringVar()
var1=StringVar()
var2=StringVar()
var3=StringVar()

def submit():
    # var.set(var1.get())
    messagebox.showinfo("your details","\nname:- "+var.get()+"\nUSN:- "+var1.get()+"\nDOB:- "+var2.get()+"\nPassword:- "+var3.get()+"\n\t\t\t\t")
user_name=Label(root,text="Name:- ").place(x=40,y=30)
user_usn=Label(root,text="USN:- ").place(x=40,y=50)
user_dob=Label(root,text="DOB(dd/mm/yyyy):- ").place(x=40,y=70)
user_password=Label(root,text="password:- ").place(x=40,y=90)
user_name_input_area = Entry(root,textvariable= var ,width = 30).place(x = 200, y = 30)
user_usn_input_area = Entry(root,textvariable= var1,width = 30).place(x = 200, y = 50)
user_dob_input_area = Entry(root,textvariable= var2,width = 30).place(x = 200, y = 70)
user_password_input_area = Entry(root, textvariable= var3,width = 30).place(x = 200, y = 90)
submit = Button(root, text ="Submit",bd=5, command=submit).place(x=40,y=130)
exit = Button(root, text ="\t\t\tExit\t\t\t",bd=5,command=root.destroy )
exit.pack(side = "bottom")
root.geometry("800x400")
root.mainloop()