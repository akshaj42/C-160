from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root=Tk()
root.minsize(650,630)
root.maxsize(650,650)

image1=ImageTk.PhotoImage(Image.open("open.png"))
image2=ImageTk.PhotoImage(Image.open("save.png"))
image3=ImageTk.PhotoImage(Image.open("exit.jpg"))

label_filename=Label(root,text="File Name: ")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

label_inputtextbox=Entry(root)
label_inputtextbox.place(relx=0.46,rely=0.03,anchor=CENTER)

text_area=Text(root,height=30,width=80)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""
def function_open():
    global name
    label_inputtextbox.delete(0,END)
    text_area.delete(1.0,END)
    textfile=filedialog.askopenfilename(title="Open text file", filetypes=(("Text Files","*.txt"),))
    print(textfile)
    name=os.path.basename(textfile)
    formatedname=name.split(".")[0]
    label_inputtextbox.insert(END,formatedname)
    root.title(formatedname)
    textfile=open(name,"r")
    paragraph=textfile.read()
    text_area.insert(END,paragraph)
    textfile.close()
    
def save():
    file_name=label_inputtextbox.get()
    file=open(file_name+".txt","w")
    data=text_area.get("1.0",END)
    print(data)
    file.write(data)
    label_inputtextbox.delete(0,END)
    text_area.delete(1.0,END)
    messagebox.showinfo("Succes","File Saved Succesfully!")
    
def close():
    root.destroy()
    
btn_open=Button(root,image=image1,command=function_open)
btn_open.place(relx=0.05,rely=0.03,anchor=CENTER)

btn_save=Button(root,image=image2,command=save)
btn_save.place(relx=0.11,rely=0.03,anchor=CENTER)

btn_close=Button(root,image=image3,command=close)
btn_close.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()