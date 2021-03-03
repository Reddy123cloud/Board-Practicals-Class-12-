'''
A binary file “Book.dat” has structure [BookNo, Book_Name, Author, Price].
'''
import pickle

def Createfile():
    f=open("Book.dat","ab+")
    n= int(input("Enter the number of books to be inputed or if no Books to be recorded than enter 0: "))
    for i in range(n):
        BookNo=int(input("Enter the Book number"))
        Book_Name=input("Enter the Book name")
        Author=input("Enter the name of Author")
        Price = float(input("Enter the Price"))
        T = (BookNo, Book_Name, Author, Price)
        pickle.dump(T,f)
    f.close()
    print("Operation Successful")

def CountRec(Author):
    f = open('Book.dat','rb')
    try:
        c = 0
        while True:
            T = pickle.load(f)
            if T[2].lower() == Author:
                c+=1
    except EOFError:
        f.close()
    print(f'Books written by {Author.upper()} = {c}')

while True:
    ch= int(input("Enter the choice: "))
    if ch==1:
        Createfile()
    elif ch==2:
        Author = input('Enter author name : ').lower()
        CountRec(Author)
    else:
        raise SystemExit

        
        
