




from tkinter import*
#from PIL import Image, ImageTK

app = Tk()

app.title ("โปรแกรม BMI")
app.geometry ('450x500')

Label1=Label(app,Text="Label ข้อความ")
Label1.grid(column=0,row=0)

Label2=Label(app,Text="Label ข้อความ2")
Label2.grid(column=0,row=0)


input1=Entry(app,width=50)
input1.grid(app,column=2,row=0)

def clicked():
    Label2['text']=input1.get()


Button1=Button(app,text="คำนวน BMI",COMMAND=clicked)
Button1.grid(column=0,row=1)

txt=Entry(app,width=90)

app.mainloop()