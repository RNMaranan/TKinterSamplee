# The code below is importing the necessary libraries for the
from tkinter import*
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# Creating GUI window with a title
gui = Tk()
gui.title("SCARA_V3 Design Calculator")
gui.resizable(True,False)
gui.config(bg="pink")

def reset():
    a1_E.delete(0, END)
    a2_E.delete(0, END)
    a3_E.delete(0, END)
    a4_E.delete(0, END)

    d1_E.delete(0, END)
    t2_E.delete(0, END)
    t3_E.delete(0, END)

    X_E.delete(0, END)
    Y_E.delete(0, END)
    Z_E.delete(0, END)

def f_k():
    # link lengths in mm
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())
    a4 = float(a4_E.get())

    # joint variables: is mm if f, is degrees if theta
    d1 = float(d1_E.get())
    T2 = float(t2_E.get())
    T3 = float(t3_E.get())

    # degree to radian
    T2 = (T2/180.0)*np.pi
    T3 = (T3/180.0)*np.pi

    # Parametic Table (theta, alpha, r, d)
    PT = [[(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a1+d1],
      [T2,(0.0/180.0)*np.pi,a2,0],
      [T3,(0.0/180.0)*np.pi,a4,a3]]


    # HTM formulae
    i = 0
    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

    i = 1
    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

    i = 2
    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

    H0_1 = np.array(H0_1)
    H1_2 = np.array(H1_2)
    H2_3 = np.array(H2_3)

    H0_2 = np.dot(H0_1,H1_2)
    H0_3 = np.dot(H0_2,H2_3)

    X0_3 = H0_3[0,3]
    X_E.delete(0, END)
    X_E.insert(0,np.around(X0_3,3))

    Y0_3 = H0_3[1,3]
    Y_E.delete(0, END)
    Y_E.insert(0,np.around(Y0_3,3))

    Z0_3 = H0_3[2,3]
    Z_E.delete(0, END)
    Z_E.insert(0,np.around(Z0_3,3))

## Frame
FI = LabelFrame(gui,text="Link Lengths and Joint Variables",font=("Comic Sans MS",20))
FI.grid(row=0,column=0)

#Link Lengths
a1 = Label(FI,text=("a1 = "),font=(10))
a1_E = Entry(FI,width=5,font=(10))
cm1 = Label(FI,text=("cm"),font=(10))

a1.grid(row=0,column=0)
a1_E.grid(row=0,column=1)
cm1.grid(row=0,column=2)

a2 = Label(FI,text=("a2 = "),font=(10))
a2_E = Entry(FI,width=5,font=(10))
cm2 = Label(FI,text=("cm"),font=(10))

a2.grid(row=1,column=0)
a2_E.grid(row=1,column=1)
cm2.grid(row=1,column=2)

a3 = Label(FI,text=("a3 = "),font=(10))
a3_E = Entry(FI,width=5,font=(10))
cm3 = Label(FI,text=("cm"),font=(10))

a3.grid(row=2,column=0)
a3_E.grid(row=2,column=1)
cm3.grid(row=2,column=2)

a4 = Label(FI,text=("a4 = "),font=(10))
a4_E = Entry(FI,width=5,font=(10))
cm4 = Label(FI,text=("cm"),font=(10))

a4.grid(row=3,column=0)
a4_E.grid(row=3,column=1)
cm4.grid(row=3,column=2)

d1 = Label(FI,text=("d1 = "),font=(10))
d1_E = Entry(FI,width=5,font=(10))
cm5 = Label(FI,text=("cm"),font=(10))

d1.grid(row=0,column=3)
d1_E.grid(row=0,column=4)
cm5.grid(row=0,column=5)

t2 = Label(FI,text=("t2 = "),font=(10))
t2_E = Entry(FI,width=5,font=(10))
deg2 = Label(FI,text=("deg"),font=(10))

t2.grid(row=1,column=3)
t2_E.grid(row=1,column=4)
deg2.grid(row=1,column=5)

t3 = Label(FI,text=("t3 = "),font=(10))
t3_E = Entry(FI,width=5,font=(10))
deg3 = Label(FI,text=("deg"),font=(10))

t3.grid(row=2,column=3)
t3_E.grid(row=2,column=4)
deg3.grid(row=2,column=5)

#Button Frames
BF = LabelFrame(gui,text="Forward and Inverse Kinematics",font=("Comic Sans MS",20))
BF.grid(row=1,column=0)

#Buttons
FK = Button(BF,text="Forward",font=(10),bg="black", fg="white",command=f_k)
rst = Button(BF,text="RESET",font=(10),bg="white", fg="black",command=reset)
IK = Button(BF,text="Inverse",font=(10),bg="hot pink", fg="white")

FK.grid(row=0,column=0)
rst.grid(row=0,column=1)
IK.grid(row=0,column=2)

##Position Vector
PV = LabelFrame(gui,text="Position Vector",font=("Comic Sans MS",20))
PV.grid(row=2,column=0)

X = Label(PV,text=("X = "),font=(10))
X_E = Entry(PV,width=5,font=(10))
cm8 = Label(PV,text=("cm"),font=(10))

X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm8.grid(row=0,column=2)

Y = Label(PV,text=("Y = "),font=(10))
Y_E = Entry(PV,width=5,font=(10))
cm9 = Label(PV,text=("cm"),font=(10))

Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cm9.grid(row=1,column=2)

Z = Label(PV,text=("Z = "),font=(10))
Z_E = Entry(PV,width=5,font=(10))
cm10 = Label(PV,text=("cm"),font=(10))

Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cm10.grid(row=2,column=2)

gui.mainloop()
