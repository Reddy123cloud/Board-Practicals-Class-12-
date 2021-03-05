import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd = 'isgsql', database= 'test')
mycursor=mydb.cursor()

def take_values():
    choice = input("Do u want to put some values(y/n): ")
    if choice == 'y':
        n= int(input("Enter the number of employees u want to add or no employees u want to add than type 0: "))
        if n!=0:
            for i in range(n):
                id = int(input("Enter the Employee id"))
                Name = input("Enter the name of the employee")
                Salary = int(input("Enter the salary (a few digit figure)"))
                mycursor.execute("insert into employee values('"+str(id)+"','"+Name+"','"+str(Salary)+"')")
                mydb.commit()
        else:
            pass
    if choice == 'n':
        pass
take_values()

def Command1():
    mycursor.execute("select * from employee where salary>70000")
    records=mycursor.fetchall()
    for x in records:
        print(x)

def Command2():
    mycursor.execute("update employee set salary = salary + 1000 where salary < 80000")
    mydb.commit()

def Command3():
    Employee_Salary = int(input("Enter the Employee salary of the person whose name should be deleted"))
    mycursor.execute("delete from employee where Salary = '"+str(Employee_Salary)+"'")
    mydb.commit()
    print(mycursor.rowcount,"Record Deleted")
def Command4():
    mycursor.execute("Select * from employee order by salary")
    records = mycursor.fetchall()
    for x in records:
        print(x)
def Command5():
    Name = input("Enter the name to be deleted")
    mycursor.execute("delete from employee where Employee_name = Name")
    mydb.commit()
    print(mycursor.rowcount,"Record Deleted")
def display():
    mycursor.execute("Select * from employee")
    records = mycursor.fetchall()
    for x in records:
        print(x)
print("Enter the choice number from the list given below ")
print("1.To read and fetch all the records from EMP table having salary more than  70000.")
print("2.to update the records of employees by increasing salary by  1000 of all those employees who are getting less than  80000")
print("3 to delete the record on the basis of inputted salary")
print("4 to display all records in ascending order of their salary")
print("5 to delete the employee record whose name is read from the keyboard at execution time")
print("6 To diplay all the records")

while True:
    ch = int(input("Enter the choice: "))
    if ch==1:
        Command1()
    elif ch==2:
        Command2()
        display()
    elif ch==3:
        Command3()
        display()
    elif ch==4:
        Command4()
    elif ch==5:
        Command5()
        display()
    elif ch==6:
        display()
    else:
        print("wrong command, retry")
        continue
    Continue=input("Do you wish to continue? (Y/N)")
    if Continue =="N" or Continue=="n":
        print("Thank you")
        break
