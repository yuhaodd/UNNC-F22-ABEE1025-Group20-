# Author: Group 20
# Date of the first creation: 2023-01-25
# This file is a simple matrix calculator using python GUI

from tkinter import *

#Create a matrix calculator class
class MatrixCalculator:
    
    global r1,c1 #Declare global variables, row1 and column1
    global r2,c2 #Declare global variables, row2 and column2
    
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name
        
    #Set the window
    def set_init_window(self):
        #Application name
        self.init_window_name.title("Python Matrix Calculator")
        
        #The size of the window
        self.init_window_name.geometry('1300x600')
        
        #The blur degree of the window
        self.init_window_name.attributes("-alpha",0.9)
        
        # The minimum size of GUI window
        self.init_window_name.minsize(1300,600)
        
        # The maximum size of GUI window
        self.init_window_name.maxsize(1700,800) 
        
        #Label:
        #Label of "Matrix A Input"
        self.label1=Label(self.init_window_name,text="Matrix A Input",
                          font=('Calibri 15 bold italic'),
                          bg='LightBlue',width=17,anchor=W)
        self.label1.grid(row=0,column=0,padx=5)
        
        #Label of "Rows and Columns" for Matrix A
        self.label2=Label(self.init_window_name,text="Rows and Columns",
                          font=('Calibri 15'),width=17,anchor=W)
        self.label2.grid(row=1,column=0) 
        
        #Label of "Matrix Elements" for Matrix A
        self.label3=Label(self.init_window_name,text="Matrix Elements",
                          font=('Calibri 15'),width=17,anchor=W)
        self.label3.grid(row=2,column=0) 
        
        #Label of "Matrix B Input"
        self.label4=Label(self.init_window_name,text="Matrix B Input",
                          font=('Calibri 15 bold italic'),
                          bg='LightBlue',width=17,anchor=W)
        self.label4.grid(row=0,column=3,padx=5)
        
        #Label of "Rows and Columns" for Matrix B
        self.label5=Label(self.init_window_name,text="Rows and Columns",
                          font=('Calibri 15'),width=17,anchor=W)
        self.label5.grid(row=1,column=3) 
        
        #Label of "Matrix Elements" for Matrix B
        self.label6=Label(self.init_window_name,text="Matrix Elements",
                          font=('Calibri 15'),width=17,anchor=W)
        self.label6.grid(row=2,column=3) 
        
        #Label of "Result" for Matrix Operation
        self.label7=Label(self.init_window_name,text="Result",
                          font=('Calibri 15 bold italic'),
                          bg='LightBlue',width=17,anchor=W)
        self.label7.grid(row=4,column=0,pady=30) 

        #Label of "Reminder" for Matrix Operation
        self.label8=Label(self.init_window_name,
                      text="Reminder: Click Help Menu for Instructions",
                      font=('Calibri 15 bold italic'),
                      width=30,anchor=W,wraplength=200,justify = 'left')
        self.label8.grid(row=8,column=4,columnspan=2)
    
        #Entry:
        #Entry for Matrix A rows and columns
        self.E_var1=StringVar() 
        self.entry1=Entry(self.init_window_name,
                          textvariable=self.E_var1,
                          font=('Calibri 15'),borderwidth=5)
        self.entry1.grid(row=1,column=1)
        
        #Entry for Matrix A elements
        self.E_var2=StringVar() 
        self.entry2=Entry(self.init_window_name,
                          textvariable=self.E_var2,
                          font=('Calibri 15'),borderwidth=5)
        self.entry2.grid(row=2,column=1)
        
        #Entry for Matrix B rows and columns
        self.E_var3=StringVar() 
        self.entry3=Entry(self.init_window_name,
                          textvariable=self.E_var3,
                          font=('Calibri 15'),borderwidth=5)
        self.entry3.grid(row=1,column=4)
        
        #Entry for Matrix B elements
        self.E_var4=StringVar() 
        self.entry4=Entry(self.init_window_name,
                          textvariable=self.E_var4,
                          font=('Calibri 15'),borderwidth=5)
        self.entry4.grid(row=2,column=4)
        
        #Button:
        #Button to confirm the input of Matrix A
        self.button1=Button(self.init_window_name,text="Confirm", 
                            font=('Calibri 13'),
                            width=10,height=2,bg='Orange',
                            command=self.getcr1)
        self.button1.grid(row=1,column=2,rowspan=2,padx=10)
        
        #Button to confirm the input of Matrix B
        self.button2=Button(self.init_window_name,text="Confirm", 
                            font=('Calibri 13'),
                            width=10,height=2,bg='Orange',
                            command=self.getcr2)
        self.button2.grid(row=1,column=5,rowspan=2,padx=10)
        
        #Button to transpose A
        self.button3=Button(self.init_window_name,text="Transpose A", 
                            font=('Calibri 13'),
                            width=22,bg='Orange', 
                            command=self.transpose_A)
        self.button3.grid(row=3,column=1,pady=5)
        
        #Button to transpose B
        self.button4=Button(self.init_window_name,text="Transpose B", 
                            font=('Calibri 13'),
                            width=22,bg='Orange', 
                            command=self.transpose_B)
        self.button4.grid(row=3,column=4,pady=5)
        
        #Button to add Matrix A and Matrix B
        self.button5=Button(self.init_window_name,text="Add A+B", 
                            font=('Calibri 13'),
                            width=35,height=2,bg='Orange', 
                            command=self.add)
        self.button5.grid(row=5,column=4,columnspan=2)
        
        #Button to subtract Matrix A and Matrix B
        self.button6=Button(self.init_window_name,text="Subtract A-B", 
                            font=('Calibri 13'),
                            width=35,height=2,bg='Orange', 
                            command=self.subtract)
        self.button6.grid(row=6,column=4,columnspan=2,pady=2)
        
        #Button to multiply Matrix A and Matrix B
        self.button7=Button(self.init_window_name,text="Multiply AB", 
                            font=('Calibri 13'),
                            width=35,height=2,bg='Orange', 
                            command=self.multiply)
        self.button7.grid(row=7,column=4,columnspan=2,pady=2)
        
        #Button to clear the input of Matrix A
        self.button8=Button(self.init_window_name,text="Clear A",
                            font=('Calibri 13  italic'),width=10,
                            command=self.clear_A) 
        self.button8.grid(row=3,column=2)
        
        #Button to clear the input of Matrix B
        self.button9=Button(self.init_window_name,text="Clear B",
                            font=('Calibri 13  italic'),width=10,
                            command=self.clear_B) 
        self.button9.grid(row=3,column=5)
        
        #Button to clear porcessing result
        self.button10=Button(self.init_window_name,text="Clear Result",
                            font=('Calibri 13  italic'),width=22,
                            command=self.clear_result) 
        self.button10.grid(row=4,column=1,padx=5)
        
        #Text:
        #Text for displaying the processing result
        self.text1=Text(self.init_window_name,state="normal",
                        width=65,heigh=14,font=('Calibri 15'))
        self.text1.grid(row=5,rowspan=5,columnspan=4)

        #Menu:
        #Create parent menu
        self.Menu_All=Menu(self.init_window_name)
        #Create main menu
        self.Menu1=Menu(self.Menu_All,tearoff=0)
        #Create submenu
        self.Menu1.add_command(label="User Guide",
                               command=self.show_userguide)
        #Parent menu display
        self.Menu_All.add_cascade(label='Help',menu=self.Menu1,
                                  font=('Calibri 12 '))
        #Main menu display
        self.init_window_name.config(menu=self.Menu_All)
                    
    #Set a inside window
    def show_userguide(self):
        Userguide=Tk()
        Userguide.geometry("1000x500")
        Userguide.title("User Guide")

        #Text for Instruction content
        self.content=Text(Userguide,
                       width=125,heigh=25,
                       font=('Calibri 15'))
        self.content.grid(row=0,column=0)
        
        #Insert Texts
        self.content.insert(1.0,
            'INSTRUCTION\n')
        self.content.insert(2.0,
            '    This is a simple python matrix calculator.\n')
        self.content.insert(3.0,
            '    It can compute basic matrix operations including:\n')
        self.content.insert(4.0,
            '    addition, subtraction, \
multiplication, and transpozation.\n')
        self.content.insert(5.0,
            'NOTICE 1\n')
        self.content.insert(6.0,
            '    For Matrix Input:\n')
        self.content.insert(7.0,
            '    1) The inputs of matrix have to be integers.\n')
        self.content.insert(8.0,
            '    2) The two adjacent numbers \
must be separated by a space.\n')
        self.content.insert(9.0,
            '    3) The elements should be input \
from matrix top left to right bottom.\n')
        self.content.insert(10.0,
            '    For Example: Matrix 2x3\n')
        self.content.insert(11.0,
            '                 1 2 3\n')
        self.content.insert(12.0,
            '                 1 2 3\n')
        self.content.insert(13.0,
            '                "Rows and Columns":2 3\n')
        self.content.insert(14.0,
            '                "Elements":1 2 3 1 2 3\n')
        self.content.insert(15.0,
            'NOTICE 2\n')
        self.content.insert(16.0,
            '    For Matrix Operation:\n')
        self.content.insert(17.0,
            '    1) The inputs of matrix must be confirmed \
by Button "Confirm" before any operation.\n')
        self.content.insert(18.0,
            '    2) For "Transpose", \
input one matrix (A or B) is enough.\n')
        self.content.insert(19.0,
            '        For "Add", "Subtract" and "Multiply", \
input both matrix A and martrix B.\n')
        self.content.insert(20.0,
            '    3) The three different clear buttons are responsible for \
deleting the corresponding parts.\n')
        
        #Set Texts unchangable
        self.content.configure(state='disabled')
        
        Userguide.mainloop()
        
    #Get the number of rows and columns for Matrix A
    def getcr1(self): 
        """
        Split the string type data set into a one-dimensional list.
        Return the inputed number of rows and columns for Matrix A.
        
        """
        global r1,c1
        r1,c1=map(int,self.E_var1.get().split())
        self.text1.insert(END, f'Matrix A: Row number:{r1}'
                               f' ,Column number:{c1}.\n')
    
    #Get the number of rows and columns for Matrix B
    def getcr2(self):
        """
        Split the string type data set into a one-dimensional list.
        Return the inputed number of rows and columns for Matrix A.
        
        """
        global r2,c2
        r2,c2=map(int,self.E_var3.get().split())
        self.text1.insert(END, f'Matrix B: Row number:{r2}'
                               f' ,Column number:{c2}.\n')
    
    #Transpose Matrix A
    def transpose_A(self):
        """
        Transpose Matrix A by switch the position 
        of rows and columns for each elements: 
        element[row][column] = element[column][row] 
        
        """
        global r1,c1
        
        #Get the elments of Matrix A in Entry2
        excel=self.E_var2.get()
        self.text1.insert(END,'Input Matrix A:\n')
        excel=excel.split()
        excel=[excel[i:i+c1] for i in range(0,len(excel),c1)]
        for i in range(r1):
            for j in range(c1):
                self.text1.insert(END,excel[i][j]+' ')
            self.text1.insert(END,'\n')
            
        #Perform transpose operation
        New_excel=[['' for j in range(0,r1)] for i in range(0,c1)]
        self.text1.insert(END,'Transpose Matrix A:\n')
        for i in range(c1):
            for j in range(r1):
                New_excel[i][j]=excel[j][i]
                self.text1.insert(END,New_excel[i][j]+' ')
            self.text1.insert(END,'\n')
        New_excel=[j for i in New_excel for j in i]
        New_excel=' '.join(New_excel)
    
    #Transpose Matrix B
    def transpose_B(self):
        """
        Transpose Matrix B by switch the position 
        of rows and columns for each elements: 
        element[row][column] = element[column][row] 
        
        """
        global r2,c2
        
        #Get the elments of Matrix B in Entry4
        excel=self.E_var4.get()
        self.text1.insert(END,'Input Matrix B:\n')
        excel=excel.split()
        excel=[excel[i:i+c2] for i in range(0,len(excel),c2)]
        for i in range(r2):
            for j in range(c2):
                self.text1.insert(END,excel[i][j]+' ')
            self.text1.insert(END,'\n')
            
        #Perform transpose operation
        New_excel=[['' for j in range(0,r2)] for i in range(0,c2)]
        self.text1.insert(END,'Transpose Matrix B:\n')
        for i in range(c2):
            for j in range(r2):
                New_excel[i][j]=excel[j][i]
                self.text1.insert(END,New_excel[i][j]+' ')
            self.text1.insert(END,'\n')
        New_excel=[j for i in New_excel for j in i]
        New_excel=' '.join(New_excel)
    
    #Add Matrix A and Matrix B
    def add(self):
        """
        Add two matrices A and B of the same dimensions.
        
        """
        global r1,c1,r2,c2
        if r2!=c1:
            self.text1.insert(END,'unable to calculate')
            self.text1.insert(END,'\n')
        #Get the elments of Matrix A in Entry2
        else:
            excel=self.E_var2.get()
            self.text1.insert(END,'Input Matrix A:\n')
            excel=excel.split()
            excel=[excel[i:i+c1] for i in range(0,len(excel),c1)]
        for i in range(r1):
            for j in range(c1):
                self.text1.insert(END,excel[i][j]+' ')
            self.text1.insert(END,'\n')
        
        #Get the elments of Matrix B in Entry4
        excel1=self.E_var4.get()
        self.text1.insert(END,'Input Matrix B:\n')
        excel1=excel1.split()
        excel1=[excel1[i:i+c1] for i in range(0,len(excel1),c1)]
        for i in range(r2):
            for j in range(c2):
                self.text1.insert(END,excel1[i][j]+' ')
            self.text1.insert(END,'\n')
        
        #Perform add operation
        add_excel=[[str((int(excel[i][j])+int(excel1[i][j]))) 
                    for j in range(c1)] for i in range(r1)]
        self.text1.insert(END,'Matrix addition result：:\n')
        for i in range(r1):
            for j in range(c1):
                self.text1.insert(END,add_excel[i][j]+' ')
            self.text1.insert(END,'\n')
    
    #Subtract Matrix A and Matrix B
    def subtract(self):
        """
        Subtract two matrices A and B of the same dimensions.
        
        """
        global r1,c1,r2,c2
        if r2!=c1:
            self.text1.insert(END,'unable to calculate')
            self.text1.insert(END,'\n')
        #Get the elments of Matrix A in Entry2
        else:
            excel=self.E_var2.get()
            self.text1.insert(END,'Input Matrix A:\n')
            excel=excel.split()
            excel=[excel[i:i+c1] for i in range(0,len(excel),c1)]
        for i in range(r1):
            for j in range(c1):
                self.text1.insert(END,excel[i][j]+' ')
            self.text1.insert(END,'\n')
            
        #Get the elments of Matrix B in Entry4
        excel1=self.E_var4.get()
        self.text1.insert(END,'Input Matrix B:\n')
        excel1=excel1.split()
        excel1=[excel1[i:i+c1] for i in range(0,len(excel1),c1)]
        for i in range(r2):
            for j in range(c2):
                self.text1.insert(END,excel1[i][j]+' ')
            self.text1.insert(END,'\n')
        
        #Perform subtract operation
        subtract_excel=[[str((int(excel[i][j])-int(excel1[i][j]))) 
                         for j in range(c1)] for i in range(r1)]
        self.text1.insert(END,'Matrix subtraction result：:\n')
        for i in range(r1):
            for j in range(c1):
                self.text1.insert(END,subtract_excel[i][j]+' ')
            self.text1.insert(END,'\n')

    #Multiply Matrix A and Matrix B
    def multiply(self):
        """
        Multiply two matrices A and B of corresponding dimensions.
        The column number of Matrix A = The row number of Matrix B
        
        """
        global r1,c1,r2,c2
        if r2!=c1:
            self.text1.insert(END,'unable to calculate')
            self.text1.insert(END,'\n')
        #Get the elments of Matrix A in Entry2
        else:
            excel=self.E_var2.get()
            self.text1.insert(END,'Input Matrix A:\n')
            excel=excel.split()
            excel=[excel[i:i+c1] for i in range(0,len(excel),c1)]
        for i in range(r1):
            for j in range(c1):
                self.text1.insert(END,excel[i][j]+' ')
            self.text1.insert(END,'\n')
        
        #Get the elments of Matrix B in Entry4
        excel1=self.E_var4.get()
        self.text1.insert(END,'Input Matrix B:\n')
        excel1=excel1.split()
        excel1=[excel1[i:i+c2] for i in range(0,len(excel1),c2)]
        for i in range(r2):
            for j in range(c2):
                self.text1.insert(END,excel1[i][j]+' ')
            self.text1.insert(END,'\n')    
        
        #Perform multiply operation
        mul_excel=[[0 for j in range(c2)] for i in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    mul_excel[i][j]+=int(excel[i][k])*int(excel1[k][j])
        self.text1.insert(END,'Matrix multiplication result：:\n')
        for i in range(r1):
            for j in range(c2):
                self.text1.insert(END,str(mul_excel[i][j])+' ')
            self.text1.insert(END,'\n')  

    #Clear the input of Matrix A
    def clear_A(self):
        self.entry1.delete(-1,END)
        self.entry2.delete(-1,END)
    
    #Clear the input of Matrix B
    def clear_B(self):    
        self.entry3.delete(-1,END)
        self.entry4.delete(-1,END)
    
    #Clear all porcessing results
    def clear_result(self):
        self.text1.delete("0.0","end")
        
def MatrixCalculator_start():
    
    #Instantiate a parent window
    init_window=Tk()      
    GUI=MatrixCalculator(init_window)
    
    #Set the default properties of the root window
    GUI.set_init_window()
    init_window.mainloop()          

MatrixCalculator_start()
