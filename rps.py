



def hi(ch):
  global win_user,win_comp,l8
  l7=tk.Label(win,text="              ",font=("Helevetica",22),fg="orange",bg="green",width=50)
  l7.place(x=530,y=275)
  l9=tk.Label(win,text="      ",font=("Helevetica",22),fg="orange",bg="green",width=50)
  l9.place(x=310,y=410)
  l11=tk.Label(win,text="         ",font=("Helevetica",20),fg="yellow",bg="green",width=50)
  l11.place(x=40,y=390)
  ch_upper=ch.upper()
  if ch_upper not in dict_compuser:
    invalid()
    enter()
  else:
    userinp=dict_compuser[ch_upper]
    comp_input=rand()
    if userinp==3 and comp_input==1:
      win_comp+=1
      l8=tk.Label(win,text="Computer won!!",font=("Helevetica",18),fg="orange",bg="green")
      l8.place(x=550,y=330)
    elif userinp==1 and comp_input==3:
      win_user+=1
      l8=tk.Label(win,text="You won!!",font=("Helevetica",18),fg="orange",bg="green")
      l8.place(x=550,y=330)
    elif userinp>comp_input:
      win_user+=1
      l8=tk.Label(win,text="You won!!",font=("Helevetica",18),fg="orange",bg="green")
      l8.place(x=550,y=330)
    elif userinp<comp_input:
      win_comp+=1
      l8=tk.Label(win,text="Computer won!!",font=("Helevetica",18),fg="orange",bg="green")
      l8.place(x=550,y=330)
    elif userinp==comp_input:
      l8=tk.Label(win,text="Draw!!",font=("Helevetica",18),fg="yellow",bg="green")
      l8.place(x=380,y=400)
      
    l6=tk.Label(win,text="Computer's turn!!",font=("Helevetica",25),fg="orange",bg="green",pady=10)
    l6.place(x=500,y=200)
    
    l7=tk.Label(win,text="Computer chose: "+num_dict[comp_input],font=("Helevetica",20),fg="yellow",bg="green")
    l7.place(x=530,y=275)
    l11=tk.Label(win,text="You chose: "+num_dict[userinp],font=("Helevetica",20),fg="yellow",bg="green")
    l11.place(x=40,y=390)
    l10=tk.Label(win,text="USER: "+str(win_user),padx=10,pady=10,font=("Helevetica",18),fg="yellow",bg="lime green")
    l10.place(x=350,y=260)
    l11=tk.Label(win,text="COMP: "+str(win_comp),padx=10,pady=10,font=("Helevetica",18),fg="yellow",bg="lime green")
    l11.place(x=350,y=310)
    #print("user: ",win_user,"computer: ",win_comp)
    #print("computer chose: ",comp_input)
    if win_user==3 or win_comp==3:
      if win_user>win_comp:
        tk.messagebox.showinfo("Game won!", "You won!!! :D")
      else:
        tk.messagebox.showinfo("Game lost", "You lost :(")
      win.destroy()
    #print("user chose: ",ch_upper,userinp)
    win.after(3000, dest2) 
    
def invalid():
  global l5,b2
  l5=tk.Label(win,text="enter valid input")
  l5.place(x=170,y=400)
  b2=tk.Button(win,text="ok",command=dest)
  b2.place(x=170,y=450)

def dest():
  l5.destroy()
  b2.destroy()

def dest2():
  
  l8.destroy()
  l9=tk.Label(win,text="Keep playing!!",font=("Helevetica",22),fg="yellow",bg="green")
  l9.place(x=320,y=410)
def rand():
  
  import random

  #my_list = [1, 2, 3]
  random_element = random.choice(my_list)
  #dict_comp=[1:"R",2:"P",3:"S"]
  return random_element
def main():
  
  global win,l2


  win=tk.Tk()
  win.geometry("900x500")
  win['bg']="green"
  win.title("rock paper scissors")
  l1=tk.Label(win,text="LET'S PLAY!",width="20",height="2",font=("Helvetica", 16),fg="orange",bg="yellow",relief="solid",pady=10)
  l1.place(x=300,y=50)
  l3=tk.Label(win,text="R: Rock  P: Paper  S: Scissors",font=("Helevetica",25),fg="orange",bg="green",pady=10)
  l3.place(x=200,y=140)
  l2=tk.Label(win,text="Your turn!!",font=("Helevetica",25),fg="orange",bg="green",pady=10)
  l2.place(x=150,y=200)
  enter()
def enter():
  l4=tk.Label(win,text="Enter R/P/S",bg="green",font=("Helevetica",15))
  l4.place(x=25,y=275)
  e1=tk.Entry(win)
  e1.place(x=160,y=280)
  b1=tk.Button(win,text="GO!",bd='5',padx='5',pady='5',width=5,command=lambda: hi(e1.get()))
  b1.place(x=170,y=330)
  
import tkinter as tk
import time
import threading
from tkinter import messagebox
dict_compuser={"R":1,"P":2,"S":3}
my_list = [1, 2, 3]
num_dict={1:"Rock",2:"Paper",3:"Scissors"}
  #dict_user=[1:"R",2:"P",3:"S"]
win_user=0
win_comp=0
main()
