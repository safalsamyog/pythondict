from tkinter import *
from bs4 import BeautifulSoup
import requests
root=Tk()
root.title("safal dictionary")
root.geometry("540x620")
root.config(bg="black")
safal=StringVar()
def sad():
   
    a=safal.get()
    contents=requests.get("https://www.englishnepalidictionary.com/?q=%s"%a).content
    soup=BeautifulSoup(contents,"lxml")

    dd=soup.find('div',class_="search-result")
    result=dd.h3.text
    t.config(text=result)
 

    

L= Label(root, text="welcome to our english to nepali dicitonary",fg="white",bg="black",font="arial 8 bold underline")
L.pack( side =TOP)

L1 = Label(root, text="enter any words you want",fg="red",bg="black")
L1.pack( side =TOP)
e1=Entry(root,bg="gray",bd=5,width=40,textvariable=safal,fg="white",relief=SUNKEN,borderwidth=7)
e1.pack()
dd=Button(root,text="click",command=sad,bd=4,width=20,bg="yellow",fg="green",relief=SUNKEN)
dd.pack()
t=Label(root,bg="black",fg="white",width=20)
t.pack()
_l=Label(root, text="Note:there is no virus and required internet connection by safal..",fg="white",bg="black",font="arial 8 bold")
_l.pack(side=BOTTOM)
__but=Button(root,text="quit",command=root.quit,bg="blue",bd=5,fg="white",width=25)
__but.pack(side=BOTTOM)
if __name__=='__main__':
	root.mainloop()

