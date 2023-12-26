from tkinter import *
import ast



i=0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1

def get_opertion(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def calculate():
    entire_string=display.get()
    try:
        node=ast.parse(entire_string,mode="eval")
        r=eval(compile(node,"<string>",'eval'))
        clear_all()
        display.insert(0,r)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"")

root=Tk()


display=Entry(root)
display.grid(row=1,columnspan=6)

numbers=[1,2,3,4,5,6,7,8,9]
counter=0
for x in range(3):
    for y in range(3):
        b_t=numbers[counter]
        b=Button(root,text=b_t,width=2,height=2,command=lambda text=b_t:get_number(text))
        b.grid(row=x+2,column=y)
        counter+=1

b=Button(root,text="0",width=2,height=2,command=lambda :get_number(0))
b.grid(row=5,column=1)

count=0
operations=['+',"-","*","/","*3.14","%","(","**",")","**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            b=Button(root,text=operations[count],width=2,height=2,command=lambda text=operations[count]:get_opertion(text))
            count+=1
            b.grid(row=x + 2, column=y+3)

Button(root,text="AC",height=2,width=2,command=clear_all).grid(row=5,column=0)
Button(root,text="=",height=2,width=2,command=calculate).grid(row=5,column=2)
Button(root,text="<-",width=2,height=2,command=lambda  :undo()).grid(row=5,column=4)

root.mainloop()