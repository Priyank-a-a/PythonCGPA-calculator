from tkinter import*
from tkinter.font import Font
import string
import tkinter.messagebox



#****************************Database for other***********************************************
import sqlite3
cb=sqlite3.connect("py3.db")
d=cb.cursor()
def table2():
    
    #d.execute("""CREATE TABLE class5(regno TEXT,name TEXT,semester1 TEXT,semester2 TEXT,cgpa TEXT)""")
    d.execute("INSERT INTO class5 VALUES(?,?,?,?,?)",(e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
    cb.commit()
    r=d.execute("SELECT * FROM class5")
    print(r.fetchall())


#***************************function for other***************************************************
def res12():
    if (text7.get()!= "" and text8.get()!= "" and text9.get()!= "" and text10.get()!= "" and text11.get()!= "" and text12.get()!= "" and
        text13.get()!= "" and text14.get()!= "" and text15.get()!= "" and text16.get()!= "" and text17.get()!= "" and text18.get()!= ""):
        num13=str(text7.get())
        num14=str(text8.get())
        num15=str(text9.get())
        num16=str(text10.get())
        num17=str(text11.get())
        num18=str(text12.get())
        num19=int(text13.get())
        num20=int(text14.get())
        num21=int(text15.get())
        num22=int(text16.get())
        num23=int(text17.get())
        num24=int(text18.get())

        
        if num13=='O'or num13=='o':
            sum13=10*num19
        elif num13=='A+'or num13=='a+':
            sum13=9*num19
        elif num13=="A" or num13== "a":
            sum13=8*num19
        elif num13=="B+" or num13== "b+":
            sum13=7*num19
        elif num13=="B" or num13== "b":
            sum13=6*num19
        elif num13=="C+" or num13== "c+":
            sum13=5*num19
        elif num13=="C" or num13== "c":
            sum13=4*num19
        elif num13=="E" or num13== "e":
            sum13=0*num19
        elif num13=="F" or num13== "f":
            sum13=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Enter Alphabets b/w a to f ")

        if num14=='O' or num14=='o' :
            sum14=10*num20
        elif num14=='A+'or num14=='a+':
            sum14=9*num20
        elif num14=="A" or num14== "a":
            sum14=8*num20
        elif num14=="B+" or num14== "b+":
            sum14=7*num20
        elif num14=="B" or num14== "b":
            sum14=6*num20
        elif num14=="C+" or num14== "c+":
            sum14=5*num20
        elif num14=="C" or num14== "c":
            sum14=4*num20
        elif num14=="E" or num14== "e":
            sum14=0*num20
        elif num14=="F" or num14== "f":
            sum14=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Enter Alphabets b/w a to f ")


        if num15=='O'or num15=='o':
            sum15=10*num21
        elif num15=='A+'or num15=='a+':
            sum15=9*num21
        elif num15=="A" or num15== "a":
            sum15=8*num21
        elif num15=="B+" or num15== "b+":
            sum15=7*num21
        elif num15=="B" or num15== "b":
            sum15=6*num21
        elif num15=="C+" or num15== "c+":
            sum15=5*num21
        elif num15=="C" or num15== "c":
            sum15=4*num21
        elif num15=="E" or num15== "e":
            sum15=0*num21
        elif num15=="F" or num15== "f":
            sum15=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Enter Alphabets b/w a to f ")

        if num16=='O'or num16=='o':
            sum16=10*num22
        elif num16=='A+'or num16=='a+':
            sum16=9*num22
        elif num16=="A" or num16== "a":
            sum16=8*num22
        elif num16=="B+" or num16== "b+":
            sum16=7*num22
        elif num16=="B" or num16== "b":
            sum16=6*num22
        elif num16=="C+" or num16== "c+":
            sum16=5*num22
        elif num16=="C" or num16== "c":
            sum16=4*num22
        elif num16=="E" or num16== "e":
            sum16=0*num22
        elif num16=="F" or num16== "f":
            sum16=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Enter Alphabets b/w a to f ")

        if num17=='O'or num17=='o':
            sum17=10*num23
        elif num17=='A+'or num17=='a+':
            sum17=9*num23
        elif num17=="A" or num17== "a":
            sum17=8*num23
        elif num17=="B+" or num17== "b+":
            sum17=7*num23
        elif num17=="B" or num17== "b":
            sum17=6*num23
        elif num17=="C+" or num17== "c+":
            sum17=5*num23
        elif num17=="C" or num17== "c":
            sum17=4*num23
        elif num17=="E" or num17== "e":
            sum17=0*num23
        elif num17=="F" or num17== "f":
            sum17=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Enter Alphabets b/w a to f ")


        if num18=='O'or num18=='o':
            sum18=10*num24
        elif num18=='A+'or num18=='a+':
            sum18=9*num24
        elif num18=="A" or num18== "a":
            sum18=8*num24
        elif num18=="B+" or num18== "b+":
            sum18=7*num24
        elif num18=="B" or num18== "b":
            sum18=6*num24
        elif num18=="C+" or num18== "c+":
            sum18=5*num24
        elif num18=="C" or num18== "c":
            sum18=4*num24
        elif num18=="E" or num18== "e":
            sum18=0*num24
        elif num18=="F" or num18== "f":
            sum18=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Enter Alphabets b/w a to f ")
        root=Tk()
        answer_label=Label(root)
        a=Label(root)
        z=Label(root)
        a.grid(row=1,column=1)
        answer_label.grid(row=2,column=1)
        z.grid(row=3,column=1)    
        a.configure(text="YOUR'S TGPA IS")
        answer_label.configure(text=(sum13+sum14+sum15+sum16+sum17+sum18)/(num19+num20+num21+num22+num23+num24))
        z.configure(text=" O grade point-10 \n A+ grade point-9\n A grade point-8\n B+ grade point-7 \n B grade point-6 \n C+ grade point-5 \n C grade point-4 \n E - Reappear \n F-Fail")
    else:
        tkinter.messagebox.showinfo('ERROR',"FILL ALL THE TEXT BOXES ")

        
    
#*****************************Frame for other************************************************


def clear():
    text7.set('')
    text8.set('')
    text9.set('')
    text10.set('')
    text11.set('')
    text12.set('')
    text13.set('')
    text14.set('')
    text15.set('')
    text16.set('')
    text17.set('')
    text18.set('')
 

def o_sem1():
    top=Toplevel()
    my_font=Font(family="Times New Roman",size=30,weight="bold",slant="italic",underline=1)
    tf=Frame(top,width=250,height=250)
    top.title("CGPA CALCULATOR")
    Head=Label(top,text="MY CGPA CALCULATOR", font=my_font).grid()
    L1=Label(tf,text="SEMESTER 1 & SEMESTER 2",font=('arial',13,'bold','underline'),fg="red")
    L2=Label(tf,text="SUBJECT",font=('arial',13,'bold'),fg="blue")
    L3=Label(tf,text="GRADE",font=('arial',13,'bold'),fg="blue")
    L4=Label(tf,text="CREDIT",font=('arial',13,'bold'),fg="blue")
    L5=Label(tf,text="SUBJECT 1",font=('arial',13,'bold'))
    L6=Label(tf,text="SUBJECT 2",font=('arial',13,'bold'))
    L7=Label(tf,text="SUBJECT 3",font=('arial',13,'bold'))
    L8=Label(tf,text="SUBJECT 4",font=('arial',13,'bold'))
    L9=Label(tf,text="SUBJECT 5",font=('arial',13,'bold'))
    L10=Label(tf,text="SUBJECT 6",font=('arial',13,'bold'))
    global text7
    text7=StringVar()
    E1=Entry(tf,text=text7,font=('arial',13,'bold'),bg="powder blue")
    global text8
    text8=StringVar()
    E2=Entry(tf,text=text8,font=('arial',13,'bold'),bg="powder blue")
    global text9
    text9=StringVar()
    E3=Entry(tf,text=text9,font=('arial',13,'bold'),bg="powder blue")
    global text10
    text10=StringVar()
    E4=Entry(tf,text=text10,font=('arial',13,'bold'),bg="powder blue")
    global text11
    text11=StringVar()
    E5=Entry(tf,text=text11,font=('arial',13,'bold'),bg="powder blue")
    global text12
    text12=StringVar()
    E6=Entry(tf,text=text12,font=('arial',13,'bold'),bg="powder blue")
    global text13
    text13=StringVar()
    E7=Entry(tf,text=text13,font=('arial',13,'bold'),bg="powder blue")
    global text14
    text14=StringVar()
    E8=Entry(tf,text=text14,font=('arial',13,'bold'),bg="powder blue")
    global text15
    text15=StringVar()
    E9=Entry(tf,text=text15,font=('arial',13,'bold'),bg="powder blue")
    global text16
    text16=StringVar()
    E10=Entry(tf,text=text16,font=('arial',13,'bold'),bg="powder blue")
    global text17
    text17=StringVar()
    E11=Entry(tf,text=text17,font=('arial',13,'bold'),bg="powder blue")
    global text18
    text18=StringVar()
    E12=Entry(tf,text=text18,font=('arial',13,'bold'),bg="powder blue")
    L1.grid(row=0,column=0)
    L2.grid(row=1,column=0)
    L3.grid(row=1,column=1)
    L4.grid(row=1,column=2)
    L5.grid(row=2)
    L6.grid(row=3)
    L7.grid(row=4)
    L8.grid(row=5)
    L9.grid(row=6)
    L10.grid(row=7)
    E1.grid(row=2 ,column=1)
    E2.grid(row=3 ,column=1)
    E3.grid(row=4 ,column=1)
    E4.grid(row=5 ,column=1)
    E5.grid(row=6 ,column=1)
    E6.grid(row=7 ,column=1)
    E7.grid(row=2 ,column=2)
    E8.grid(row=3 ,column=2)
    E9.grid(row=4 ,column=2)
    E10.grid(row=5 ,column=2)
    E11.grid(row=6 ,column=2)
    E12.grid(row=7 ,column=2)
    ag=Button(tf,text="Calculate TGPA",command=res12)
    ag.grid(row=4,column=3)
    ac=Button(tf,text="Calculate CGPA",command=final)
    ac.grid(row=6,column=3)
    l23=Label(tf,text="SUBMIT YOUR DETAILS",font=('arial',13,'bold'),fg="blue")
    l23.grid(row=8,column=3)
    l7=Label(tf,text="Enter Registration number",font=('arial',13,'bold'))
    l7.grid(row=9,column=3)
    global e7
    e7=Entry(tf,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e7.grid(row=9,column=4)
    l8=Label(tf,text="Enter your name",font=('arial',13,'bold'))
    l8.grid(row=10,column=3)
    global e8
    e8=Entry(tf,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e8.grid(row=10,column=4)
    l9=Label(tf,text="Semester 1 TGPA",font=('arial',13,'bold'))
    l9.grid(row=11,column=3)
    global e9
    e9=Entry(tf,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e9.grid(row=11,column=4)
    l10=Label(tf,text="Semester 2 TGPA",font=('arial',13,'bold'))
    l10.grid(row=12,column=3)
    global e10
    e10=Entry(tf,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e10.grid(row=12,column=4)
    l11=Label(tf,text="Enter CGPA",font=('arial',13,'bold'))
    l11.grid(row=13,column=3)
    global e11
    e11=Entry(tf,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e11.grid(row=13,column=4)
    b=Button(tf,text="OK",command=table2)
    b.grid(row=14,column=3)
    p=Button(tf,text="CLEAR",command=clear)
    p.grid(row=5,column=3)
    tf.grid()

#***************************Function of cse(SEM1)***************************************************
def addF():
    if (text1.get()!= "" and text2.get()!= "" and text3.get()!= "" and text4.get()!= "" and text5.get()!= "" and text6.get()!= ""):
        num1 =str(text1.get())
        num2 =str(text2.get())
        num3 =str(text3.get())
        num4 =str(text4.get())
        num5 =str(text5.get())
        num6 =str(text6.get())
        if num1=='O'or num1=='o':
            sum1=10*4
        elif num1=='A+'or num1=='a+':
            sum1=9*4
        elif num1=="A" or num1== "a":
            sum1=8*4
        elif num1=="B+" or num1== "b+":
            sum1=7*4
        elif num1=="B" or num1== "b":
            sum1=6*4
        elif num1=="C+" or num1== "c+":
            sum1=5*4
        elif num1=="C" or num1== "c":
            sum1=4*4
        elif num1=="E" or num1== "e":
            sum1=0*4
        elif num1=="F" or num1== "f":
            sum1=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        if num2=='O' or num2=='o' :
            sum2=10*4
        elif num2=='A+'or num2=='a+':
            sum2=9*4
        elif num2=="A" or num2== "a":
            sum2=8*4
        elif num2=="B+" or num2== "b+":
            sum2=7*4
        elif num2=="B" or num2== "b":
            sum2=6*4
        elif num2=="C+" or num2== "c+":
            sum2=5*4
        elif num2=="C" or num2== "c":
            sum2=4*4
        elif num2=="E" or num2== "e":
            sum2=0*4
        elif num2=="F" or num2== "f":
            sum2=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")


        if num3=='O'or num3=='o':
            sum3=10*4
        elif num3=='A+'or num3=='a+':
            sum3=9*4
        elif num3=="A" or num3== "a":
            sum3=8*4
        elif num3=="B+" or num3== "b+":
            sum3=7*4
        elif num3=="B" or num3== "b":
            sum3=6*4
        elif num3=="C+" or num3== "c+":
            sum3=5*4
        elif num3=="C" or num3== "c":
            sum3=4*4
        elif num3=="E" or num3== "e":
            sum3=0*4
        elif num3=="F" or num3== "f":
            sum3=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        if num4=='O'or num4=='o':
            sum4=10*4
        elif num4=='A+'or num4=='a+':
            sum4=9*4
        elif num4=="A" or num4== "a":
            sum4=8*4
        elif num4=="B+" or num4== "b+":
            sum4=7*4
        elif num4=="B" or num4== "b":
            sum4=6*4
        elif num4=="C+" or num4== "c+":
            sum4=5*4
        elif num4=="C" or num4== "c":
            sum4=4*4
        elif num4=="E" or num4== "e":
            sum4=0*4
        elif num4=="F" or num4== "f":
            sum4=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        if num5=='O'or num5=='o':
            sum5=10*4
        elif num5=='A+'or num5=='a+':
            sum5=9*4
        elif num5=="A" or num5== "a":
            sum5=8*4
        elif num5=="B+" or num5== "b+":
            sum5=7*4
        elif num5=="B" or num5== "b":
            sum5=6*4
        elif num5=="C+" or num5== "c+":
            sum5=5*4
        elif num5=="C" or num5== "c":
            sum5=4*4
        elif num5=="E" or num5== "e":
            sum5=0*4
        elif num5=="F" or num5== "f":
            sum5=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")


        if num6=='O'or num6=='o':
            sum6=10*4
        elif num6=='A+'or num6=='a+':
            sum6=9*4
        elif num6=="A" or num6== "a":
            sum6=8*4
        elif num6=="B+" or num6== "b+":
            sum6=7*4
        elif num6=="B" or num6== "b":
            sum6=6*4
        elif num6=="C+" or num6== "c+":
            sum6=5*4
        elif num6=="C" or num6== "c":
            sum6=4*4
        elif num6=="E" or num6== "e":
            sum6=0*4
        elif num6=="F" or num6== "f":
            sum6=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        root=Tk()
        answer_label=Label(root)
        a=Label(root)
        z=Label(root)
        a.grid(row=1,column=1)
        answer_label.grid(row=2,column=1)
        z.grid(row=3,column=1)
        a.configure(text="YOUR'S TGPA IS")
        answer_label.configure(text=(sum1+sum2+sum3+sum4+sum5+sum6)/24)
        z.configure(text=" O grade point-10 \n A+ grade point-9\n A grade point-8\n B+ grade point-7 \n B grade point-6 \n C+ grade point-5 \n C grade point-4 \n E - Reappear \n F-Fail")
    else:
        tkinter.messagebox.showinfo('ERROR',"FILL ALL THE TEXT BOXES ")
        
#**************************Frame for SEM1****************************************************

def sem1():
    top=Toplevel()
    my_font=Font(family="Times New Roman",size=12,weight="bold",underline=1)
    tf=Frame(top,width=250,height=250)
    top.title("CGPA CALCULATOR")
    Head=Label(top,text="MY CGPA CALCULATOR", font=my_font).grid()
    L1=Label(tf,text="SEMESTER 1",font=('arial',13,'bold','underline'),fg="Red")
    L2=Label(tf,text="SUBJECT",font=('arial',13,'bold'))
    L3=Label(tf,text="CREDIT",font=('arial',13,'bold'))
    L4=Label(tf,text="GRADE",font=('arial',13,'bold'))
    L5=Label(tf,text="MTH165",font=('arial',13,'bold'))
    L6=Label(tf,text="MEC107",font=('arial',13,'bold'))
    L7=Label(tf,text="PHY119",font=('arial',13,'bold'))
    L8=Label(tf,text="PEL121",font=('arial',13,'bold'))
    L9=Label(tf,text="ECE216",font=('arial',13,'bold'))
    L10=Label(tf,text="CSE202",font=('arial',13,'bold'))
    global text1
    text1= StringVar()
    E7=Entry(tf,text=text1,font=('arial',13,'bold'),bg="powder blue")
    global text2
    text2= StringVar()
    E8=Entry(tf,text=text2,font=('arial',13,'bold'),bg="powder blue")
    global text3
    text3= StringVar()
    E9=Entry(tf,text=text3,font=('arial',13,'bold'),bg="powder blue")
    global text4
    text4= StringVar()
    E10=Entry(tf,text=text4,font=('arial',13,'bold'),bg="powder blue")
    global text5
    text5= StringVar()
    E11=Entry(tf,text=text5,font=('arial',13,'bold'),bg="powder blue")
    global text6
    text6= StringVar()
    E12=Entry(tf,text=text6,font=('arial',13,'bold'),bg="powder blue")
    E1=Label(tf,text="4",font=('arial',13,'bold'))
    E2=Label(tf,text="4",font=('arial',13,'bold'))
    E3=Label(tf,text="4",font=('arial',13,'bold'))
    E4=Label(tf,text="4",font=('arial',13,'bold'))
    E5=Label(tf,text="4",font=('arial',13,'bold'))
    E6=Label(tf,text="4",font=('arial',13,'bold'))
    L1.grid(row=0,column=0)
    L2.grid(row=1,column=0)
    L3.grid(row=1,column=1)
    L4.grid(row=1,column=2)
    L5.grid(row=2)
    L6.grid(row=3)
    L7.grid(row=4)
    L8.grid(row=5)
    L9.grid(row=6)
    L10.grid(row=7)
    E1.grid(row=2 ,column=1)
    E2.grid(row=3 ,column=1)
    E3.grid(row=4 ,column=1)
    E4.grid(row=5 ,column=1)
    E5.grid(row=6 ,column=1)
    E6.grid(row=7 ,column=1)
    E7.grid(row=2 ,column=2)
    E8.grid(row=3 ,column=2)
    E9.grid(row=4 ,column=2)
    E10.grid(row=5 ,column=2)
    E11.grid(row=6 ,column=2)
    E12.grid(row=7 ,column=2)
    B1=Button(tf,text="CALCULATE TGPA",command=addF)
    B3=Button(tf,text="CALCULATE FOR S2",command=sem2)
    B6=Button(tf,text="CALCULATE CGPA",command=final)
    B1.grid(sticky=W)
    B3.grid(sticky=W)
    B6.grid(sticky=W)
    tf.grid()
    top.mainloop()
    

#*****************************Function for Sem2**************************************************

def addFF():
    if (text1.get()!= "" and text2.get()!= "" and text3.get()!= "" and text4.get()!= "" and text5.get()!= "" and text6.get()!= ""):
        num7 =str(text1.get())
        num8 =str(text2.get())
        num9 =str(text3.get())
        num10=str(text4.get())
        num11 =str(text5.get())
        num12 =str(text6.get())
        if num7=='O'or num7=='o':
            sum7=10*4
        elif num7=='A+'or num7=='a+':
            sum7=9*4
        elif num7=="A" or num7== "a":
            sum7=8*4
        elif num7=="B+" or num7== "b+":
            sum7=7*4
        elif num7=="B" or num7== "b":
            sum7=6*4
        elif num7=="C+" or num7== "c+":
            sum7=5*4
        elif num7=="C" or num7== "c":
            sum7=4*4
        elif num7=="E" or num7== "e":
            sum7=0*4
        elif num7=="F" or num7== "f":
            sum7=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        if num8=='O' or num8=='o' :
            sum8=10*3
        elif num8=='A+'or num8=='a+':
            sum8=9*3
        elif num8=="A" or num8== "a":
            sum8=8*3
        elif num8=="B+" or num8== "b+":
            sum8=7*3
        elif num8=="B" or num8== "b":
            sum8=6*3
        elif num8=="C+" or num8== "c+":
            sum8=5*3
        elif num8=="C" or num8== "c":
            sum8=4*3
        elif num8=="E" or num8== "e":
            sum8=0*3
        elif num8=="F" or num8== "f":
            sum8=3
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")


        if num9=='O'or num9=='o':
            sum9=10*4
        elif num9=='A+'or num9=='a+':
            sum9=9*4
        elif num9=="A" or num9== "a":
            sum9=8*4
        elif num9=="B+" or num9== "b+":
            sum9=7*4
        elif num9=="B" or num9== "b":
            sum9=6*4
        elif num9=="C+" or num9== "c+":
            sum9=5*4
        elif num9=="C" or num9== "c":
            sum9=4*4
        elif num9=="E" or num9== "e":
            sum9=0*4
        elif num9=="F" or num9== "f":
            sum9=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        if num10=='O'or num10=='o':
            sum10=10*2
        elif num10=='A+'or num10=='a+':
            sum10=9*2
        elif num10=="A" or num10== "a":
            sum10=8*2
        elif num10=="B+" or num10== "b+":
            sum10=7*2
        elif num10=="B" or num10== "b":
            sum10=6*2
        elif num10=="C+" or num10== "c+":
            sum10=5*2
        elif num10=="C" or num10== "c":
            sum10=4*2
        elif num10=="E" or num10== "e":
            sum10=0*2
        elif num10=="F" or num10== "f":
            sum10=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")

        if num11=='O'or num11=='o':
            sum11=10*3
        elif num11=='A+'or num11=='a+':
            sum11=9*3
        elif num11=="A" or num11== "a":
            sum11=8*3
        elif num11=="B+" or num11== "b+":
            sum11=7*3
        elif num11=="B" or num11== "b":
            sum11=6*3
        elif num11=="C+" or num11== "c+":
            sum11=5*3
        elif num11=="C" or num11== "c":
            sum11=4*3
        elif num11=="E" or num11== "e":
            sum11=0*3
        elif num11=="F" or num11== "f":
            sum11=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")


        if num12=='O'or num12=='o':
            sum12=10*4
        elif num12=='A+'or num12=='a+':
            sum12=9*4
        elif num12=="A" or num12== "a":
            sum12=8*4
        elif num12=="B+" or num12== "b+":
            sum12=7*4
        elif num12=="B" or num12== "b":
            sum12=6*4
        elif num12=="C+" or num12== "c+":
            sum12=5*4
        elif num12=="C" or num12== "c":
            sum12=4*4
        elif num12=="E" or num12== "e":
            sum12=0*4
        elif num12=="F" or num12== "f":
            sum12=0
        else:
            tkinter.messagebox.showinfo('ERROR',"Grade does not exist ")
        root=Tk()
        answer_label1=Label(root)
        a1=Label(root)
        z1=Label(root)
        a1.grid(row=1,column=1)
        answer_label1.grid(row=2,column=1)
        z1.grid(row=3,column=1)

        a1.configure(text="YOUR'S TGPA IS")
        answer_label1.configure(text=(sum7+sum8+sum9+sum10+sum11+sum12)/20)
        z1.configure(text=" O grade point-10 \n A+ grade point-9\n A grade point-8\n B+ grade point-7 \n B grade point-6 \n C+ grade point-5 \n C grade point-4 \n E - Reappear \n F-Fail")
    else:
        tkinter.messagebox.showinfo('ERROR',"FILL ALL THE TEXT BOXES ")
    
#*******************************Databse for CSE()************************************************
    
import sqlite3
db=sqlite3.connect("py3.db")
c=db.cursor()
def table():
    #c.execute("""CREATE TABLE class5(regno TEXT,name TEXT,semester1 TEXT,semester2 TEXT,cgpa TEXT)""")
    c.execute("INSERT INTO class5 VALUES(?,?,?,?,?)",(e.get(),e5.get(),e2.get(),e3.get(),e4.get()))
    db.commit()
    r=c.execute("SELECT * FROM class5")
    print(r.fetchall())



#**************************Frame for sem2*****************************************************

def sem2():
    top=Toplevel()
    tb=Frame(top,width=250,height=250)
    L1=Label(tb,text="SEMESTER 2",font=('arial',13,'bold','underline'),fg="Red")
    L2=Label(tb,text="SUBJECT",font=('arial',13,'bold'))
    L3=Label(tb,text="CREDIT",font=('arial',13,'bold'))
    L4=Label(tb,text="GRADE",font=('arial',13,'bold'))
    L5=Label(tb,text="CSE211",font=('arial',13,'bold'))
    L6=Label(tb,text="MTH401",font=('arial',13,'bold'))
    L7=Label(tb,text="PES314",font=('arial',13,'bold'))
    L8=Label(tb,text="INT213",font=('arial',13,'bold'))
    L9=Label(tb,text="INT306",font=('arial',13,'bold'))
    L10=Label(tb,text="CSE205",font=('arial',13,'bold'))
    global text1
    text1= StringVar()
    E7=Entry(tb,text=text1,font=('arial',13,'bold'),bg="powder blue")
    global text2
    text2= StringVar()
    E8=Entry(tb,text=text2,font=('arial',13,'bold'),bg="powder blue")
    global text3
    text3= StringVar()
    E9=Entry(tb,text=text3,font=('arial',13,'bold'),bg="powder blue")
    global text4
    text4= StringVar()
    E10=Entry(tb,text=text4,font=('arial',13,'bold'),bg="powder blue")
    global text5
    text5= StringVar()
    E11=Entry(tb,text=text5,font=('arial',13,'bold'),bg="powder blue")
    global text6
    text6= StringVar()
    E12=Entry(tb,text=text6,font=('arial',13,'bold'),bg="powder blue")
    E1=Label(tb,text="4",font=('arial',13,'bold'))
    E2=Label(tb,text="3",font=('arial',13,'bold'))
    E3=Label(tb,text="4",font=('arial',13,'bold'))
    E4=Label(tb,text="2",font=('arial',13,'bold'))
    E5=Label(tb,text="3",font=('arial',13,'bold'))
    E6=Label(tb,text="4",font=('arial',13,'bold'))
    B2=Button(tb,text="CALCULATE TGPA",command=addFF)
    B4=Button(tb,text="CALCULATE FOR SEM1",command=sem1)
    B5=Button(tb,text="CALCULATE CGPA",command=final)
    L1.grid(row=0,column=0)
    L2.grid(row=1,column=0)
    L3.grid(row=1,column=1)
    L4.grid(row=1,column=2)
    L5.grid(row=2)
    L6.grid(row=3)
    L7.grid(row=4)
    L8.grid(row=5)
    L9.grid(row=6)
    L10.grid(row=7)
    E1.grid(row=2 ,column=1)
    E2.grid(row=3 ,column=1)
    E3.grid(row=4 ,column=1)
    E4.grid(row=5 ,column=1)
    E5.grid(row=6 ,column=1)
    E6.grid(row=7 ,column=1)
    E7.grid(row=2 ,column=2)
    E8.grid(row=3 ,column=2)
    E9.grid(row=4 ,column=2)
    E10.grid(row=5 ,column=2)
    E11.grid(row=6 ,column=2)
    E12.grid(row=7 ,column=2)
    B2.grid(sticky=W)
    B4.grid(sticky=W)
    B5.grid(sticky=W)
    l22=Label(tb,text="SUBMIT YOUR DETAILS",font=('arial',13,'bold'),fg="blue")
    l22.grid(row=9,column=2)
    l=Label(tb,text="Enter Registration number",font=('arial',13,'bold'))
    l.grid(row=10,column=2)
    global e
    e=Entry(tb,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e.grid(row=10,column=3)
    l5=Label(tb,text="Enter your name",font=('arial',13,'bold'))
    l5.grid(row=11,column=2)
    global e5
    e5=Entry(tb,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e5.grid(row=11,column=3)
    l2=Label(tb,text="Semester 1 TGPA",font=('arial',13,'bold'))
    l2.grid(row=12,column=2)
    global e2
    e2=Entry(tb,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e2.grid(row=12,column=3)
    l3=Label(tb,text="Semester 2 TGPA",font=('arial',13,'bold'))
    l3.grid(row=13,column=2)
    global e3
    e3=Entry(tb,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e3.grid(row=13,column=3)
    l4=Label(tb,text="Enter CGPA",font=('arial',13,'bold'))
    l4.grid(row=14,column=2)
    global e4
    e4=Entry(tb,bd=5,font=('arial',13,'bold'),bg="powder blue")
    e4.grid(row=14,column=3)
    b=Button(tb,text="OK",command=table,font=('arial',13,'bold'))
    b.grid(row=15,column=3)
    tb.grid()
    top.mainloop()
def cgpa():
    top=Toplevel()
    tc=Frame(top,width=200,height=200)
    cgp1=Label(tc,text="ENTER TGPA 1:",font=('arial',13,'bold'))
    cgp2=Label(tc,text="ENTER TGPA 2:",font=('arial',13,'bold'))
    cgp3=Label(tc,text="YOUR CGPA IS:",font=('arial',13,'bold'))
    e_cgp1=Entry(tc,font=('arial',13,'bold'),bg="powder blue")
    e_cgp2=Entry(tc,font=('arial',13,'bold'),bg="powder blue")
    cgp1.grid(row=0 ,column=0 )
    cgp2.grid(row=1 ,column=0 )
    cgp3.grid(row=2 ,column=0 )
    e_cgp1.grid(row=0 ,column=1)
    e_cgp2.grid(row=1 ,column=1 )
    tc.grid()
def wel():
    top=Toplevel()
    frame2=Frame(top,width=700,height=300)
    my_font2=Font(family="Times New Roman",size=12)
    welcome=Label(top,text="WELCOME TO TGPA/CGPA CALCULATOR",font=my_font2)
    sem=Label(top,text="'SELECT' SEMESTER",font=('arial',13,'bold','underline'),fg="Red")
    b3=Button(top,text="SEMESTER 1",command=sem1)
    b4=Button(top,text="SEMESTER 2",command=sem2)
    welcome.grid(row=0,column=0)
    b3.grid(sticky=E)
    sem.grid(row=1)
    b4.grid(sticky=E)
    frame2.grid()


def final():
	global e1
	global e2
	master = Tk()
	Label(master, text="TGPA 1",font=('arial',13,'bold')).grid(row=0)
	Label(master, text="TGPA 2",font=('arial',13,'bold')).grid(row=1)
	e1 = Entry(master,font=('arial',13,'bold'),bg="powder blue")
	e2 = Entry(master,font=('arial',13,'bold'),bg="powder blue")
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	Button(master, text='Show',command=Result).grid(row=3, column=1, sticky=W, pady=4)
    # mainloop()

def Result():
	tkinter.messagebox.showinfo("CGPA",(int(e1.get())+int(e2.get()))/2)

def select():
    top=Toplevel()
    af=Frame(top,width=250,height=250)
    top.title("Course")
    Head=Label(top,text="SELECT YOUR COURSE",font=('arial',13,'bold','underline'),fg="Red")
    B1=Radiobutton(af,text="B.tech(CSE)",value=1,command=wel,font=('arial',13,'bold'))
    B6=Radiobutton(af,text="OTHER",value=6,command=o_sem1,font=('arial',13,'bold'))
    B1.grid(sticky=W)
    B6.grid(sticky=W)
    Head.grid(sticky=W)
    af.grid()

top=Tk()
def click_me():
    if(not entry1.get().isdigit()):
        tkinter.messagebox.showinfo('ERROR',"Registration number is in digits only")
    else:
        button.config(command=wel)
'''canvas = Canvas(width = 300, height = 200)
    # pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
    # load the .gif image file
    # put in your own gif file here, may need to add full path
gif1 = PhotoImage(file = 'LPU.Gif')
    # put gif image on canvas
  # pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image = gif1, anchor = NW)
    # run it ...'''
frame2=Frame(top,width=300,height=300)
my_font2=Font(family="Times New Roman",size=25) 
name=Label(top,text="Registration number",font=('arial',13,'bold'))
password=Label(top,text="Password",font=('arial',13,'bold'))
entry1=Entry(top,font=('arial',13,'bold'),bg="powder blue")
entry2=Entry(top,show="*",font=('arial',13,'bold'),bg="powder blue")
button=Button(top,text="login",command=lambda:[click_me(),select()])
name.grid(row=0,column=0)
entry1.grid(row=0,column=1,sticky=W)
password.grid(row=1)
entry2.grid(row=1,column=1,sticky=W)
#tick=Checkbutton(top,text="keep me logged in")
#tick.grid(columnspan=2)
button.grid()
frame2.grid()
top.mainloop()
