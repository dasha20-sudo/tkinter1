from tkinter import *
from tkinter import messagebox
root = Tk()
def show():
    global photo
    photo = PhotoImage(file="img.png")
    label6.configure(image=photo)
def inf():
    s = edit4.get()
    if s == "11М":
         messagebox.showinfo("Про спеціальність", s + "\nСпеціальність 111 Математика\nОсвітня програма Комп'ютерна математика")
    elif s == "СОМ":
         messagebox.showinfo("Про спеціальність" , edit4.get() + '''\nСпеціальність 014 Середня освіта\n Освітня програма Середня освіта.  Математика , Інформатика''')
    else:
         messagebox.showinfo("Про спеціальність" , edit4.get() + "\nТакої спеціальності на факультеті немає")
root.title("Анкета")
root["bg"]="pink"
root.geometry("300x550+500+100")

label1 = Label(root, text="Прізвище:")
label1.grid(row=0,column=0)
edit1=Entry(root, width=25)
edit1.grid(row=0,column=1)

label2 = Label(root, text="Ім'я:")
label2.grid(row=1,column=0)
edit2=Entry(root, width=25)
edit2.grid(row=1,column=1)

label3 = Label(root, text="По батькові:")
label3.grid(row=2,column=0)
edit3=Entry(root, width=25)
edit3.grid(row=2,column=1)

checkbutton1 = Checkbutton(root, text="ч")
checkbutton1.grid(row=3,column=1)

checkbutton2 = Checkbutton(root, text="ж")
checkbutton2.grid(row=4,column=1)

label4=Label(root, text="Виберіть курс:")
label4.grid(row=5,column=1)

result1=IntVar()
result1.set(1)
Radiobutton1=Radiobutton(root, text=1, variable=result1, value=1).grid(row=6,column=1)
Radiobutton2=Radiobutton(root, text=2, variable=result1, value=2).grid(row=7,column=1)
Radiobutton3=Radiobutton(root, text=3, variable=result1, value=3).grid(row=8,column=1)
Radiobutton4=Radiobutton(root, text=4, variable=result1, value=4).grid(row=9,column=1)

label5=Label(root, text="Спеціальність:")
label5.grid(row=10,column=0)
edit4=Entry(root, width=25)
edit4.grid(row=10,column=1)

button1=Button(root, text="Про спеціальність", width=20, command=inf)
button1.grid(row=11,column=1)

label6=Label()
label6.grid(row=0,column=3,rowspan=3)

button2=Button(root, text="Фото", width=20, command=show)
button2.grid(row=12,column=1)

root.mainloop()