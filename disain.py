from cProfile import label
from re import T
from tkinter import *
k=0
def valjuta():
    global k
    k+=1
    nupp.configure(text=k)
def valjuta_(event):
    global k
    k-=1
    nupp.configure(text=k)
def tst_psse(event):
    t=textbox.get()
    pealkiri.configure(text=t,widht=len(t))
    textbox.delete(0,END)
def valik():
    arv=var.get()
    textbox.insert(0,arv)

aken=Tk()
aken.geometry("400x600")
aken.iconbitmap('icon.ico')
aken.title("Tkinteri kasutamine")
tekst="Pealkiri"


pealkiri=Label(aken, 
               text=tekst, 
               bg="#C6E2FF", 
               fg="#668F25", 
               font="Algeria 20", 
               height=3, width=len(tekst),
               cursor="man")
textbox=Entry(aken,
             bg="#C6E2FF",
             fg="#668F25",
             font="Algeria 20", 
             width=20,
             justify=CENTER ) #show="*"
nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3, width=len(tekst),
            relief=RAISED,
            command=valjuta()) #SUNKEN, GROOVE
f=Frame(aken)
var=IntVar() #StringVar
e=Radiobutton(f,text="Esimine",variable=var,value=1,font="Arial 20",command=valik)
t=Radiobutton(f,text="Teine",variable=var,value=2,font="Arial 20",command=valik)
k_=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Arial 20",command=valik)
nupp.bind("<Button-3>", valjuta_) #PKM
textbox.bind("<Return>",tst_psse) #SUNKEN, GROOVE

obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()
obj2=[e,t,k_]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=1)
aken.mainloop()