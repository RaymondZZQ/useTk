#coding = utf-8

import tkinter as tk
# from tkinter import *
from PIL import Image, ImageTk
import os
import numpy as np
import shutil

top = tk.Tk()
top.geometry("1200x700")


# global pathSrc , pathDst,imList,imNum
# imList = 0
# pathSrc = os.getcwd()
# pathDst = os.getcwd()
# imNum = 0

print("11111")

def callBack1():
    global pathSrc, pathDst, imList,imNum
    imNum = 0
    v1_1 = v1.get()
    pathSrc = v1_1
    try:
        imList = os.listdir(pathSrc)
    except:
        print("WRONG PATH")
    print("click  b1",pathSrc,pathDst,imList)

def callBack1_2():
    global pathSrc, pathDst, imList
    v2_1 = v2.get()
    pathDst = v2_1


def callBack2():
    global pathSrc, pathDst, imList,imNum

    imThis1 = imList[imNum]
    imThis = os.path.join(pathSrc,imThis1)
    img = Image.open(imThis)
    img =img.resize((700,700))
    img = ImageTk.PhotoImage(img)
    text.config(image=img)
    text.image = img
    imNum += 1

    shutil.copyfile(imThis,os.path.join(pathDst,imThis1))


def callBack21():
    global imNum
    imNum += 1

label1 = tk.Label(top,text="源地址",font=24).grid(row=0,column=1)
label2 = tk.Label(top,text="目标地址",font=24).grid(row=1,column=1)

v1 = tk.StringVar()
v2 = tk.StringVar()
e1 = tk.Entry(top,textvariable=v1).grid(row=0,column=2)
e2 = tk.Entry(top,textvariable=v2).grid(row=1,column=2)
B3 = tk.Button(top,text='confirm  源地址',font=24,command=callBack1).grid(row=2,column=1,columnspan=1)
B4 = tk.Button(top,text='confirm  目标地址',font=24,command=callBack1_2).grid(row=2,column=2,columnspan=1)

# img = Image.open("1.png")
# photo2 = ImageTk.PhotoImage(img)
# text = tk.Label(top, image=photo2).grid(row=0, column=0, rowspan=6)


B1 = tk.Button(top,text= "save and Next img",font=24,command=callBack2).grid(row=3,column=1,columnspan=2)
B2 = tk.Button(top,text='skip and Next img',font=24,command=callBack21).grid(row=4,column=1,columnspan=2)

quit = tk.Button(top,text="quit",command=top.quit,font=24,bg='red',fg='blue').grid(row=5,column=1,columnspan=2)


# imP = tk.PhotoImage("start.png")
img = Image.open("start.png")
img =img.resize((700,700))
photo2 = ImageTk.PhotoImage(img)
text1 = tk.Label(top,image=photo2).grid(row=0, column=0, rowspan=6)

text = tk.Label(top)
text.grid(row=0, column=0, rowspan=6)
top.mainloop()