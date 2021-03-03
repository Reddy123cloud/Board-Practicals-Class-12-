print('''MENU DRIVEN PROGRAM
1. Adding a new record [EID, Ename, designation, salary]
2. Display the detail of all employees whose salary is more than 50000
ENTER YOUR CHOICE (1/2)''')

import pickle

def Command1():
    f=open("Employee.dat","ab+")
    n=int(input("Enter the number of Employees To be added or press 0 if no Employee to be added"))
    for i in range(n):
        ID = int(input("Enter the ID"))
        Name=input("Enter the name")
        design=input("Enter the Designation")
        salary=int(input("Enter the Salary"))
        T = [ID,Name,design,salary]
        pickle.dump(T,f)
    f.close()
    print("Operation Successful")
def Command2():
    try:
        f=open("Employee.dat","rb")
    except:
        print("File does not exist")
        return
    try:
        while True:
            T = pickle.load(f)
            if T[3]>50000:
                return T
    except:
        f.close()

while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        Command1()
    elif ch==2:
        print(Command2())
    else:
        raise SystemExit 
        
