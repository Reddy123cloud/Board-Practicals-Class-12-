'''
Write a menu driven Python program to create a binary file named STUDENT.DAT with Roll no, Name and Mark.
Display all the records along with line/record number. Also write a function to search for a user entered
roll number and display the details, if not found display appropriate message.
'''

import pickle

def initial():
    try:
        f=open('Student.dat','ab+')
    except:
        return
    r=int(input("Enter the number of children or if no child than enter 0: "))
    for i in range(r):
        Name =input("Enter the name")
        Rollno = int(input("Enter the Roll number"))
        Marks = float(input("Enter the Marks "))
        T = (Name,Rollno,Marks)
        pickle.dump(T,f)

    f.close()
initial()


print('''\n MENU DRIVEN PROGRAM
1. Display all records
2. Enter roll number and search for it than display all the details related to it''')


def Command2():
    f=open("Student.dat","rb")
    Rollnumber=int(input("Enter the roll number to be searched"))
    try:
        while True:
            T = pickle.load(f)
            if T[1]==Rollnumber:
                return T
    except EOFError:
        return 'Record Does not Exist'
    f.close()

def Command1():
    f=open("Student.dat","rb")
    try:
        c=1
        while True:
            T=pickle.load(f)
            print(c,T)
            c+=1
    except EOFError:
        f.close()
    if c==1:
        print("No Records Found")

while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        Command1()
    elif ch==2:
        print(Command2())
    else:
        raise SystemExit 
        
