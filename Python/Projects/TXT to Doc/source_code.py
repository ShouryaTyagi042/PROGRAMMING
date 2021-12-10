import mysql.connector
from tabulate import tabulate

say = "Login"
print("=" * len(say.center(130, ".")))
print(say.center(130, "."))
print("=" * len(say.center(130, ".")))
print()

user_name = input("Enter your mysql username:  ")
mysql_passwd =  input("Enter your mysql password:  ")
host_name = input("Enter your host name:  ")

try:
    # Establishing connection with MySql Database .
    myconnection = mysql.connector.connect(host=host_name,user=user_name,passwd=mysql_passwd)
    mycursorconnection = myconnection.cursor()
    # Creating database
    print()
    print("MYSQL CONNECTION SUCCESFULLY CREATED ")


    try :
        mycursorconnection.execute("CREATE DATABASE College_Management_System")
        print()
        print("DATABASE College_Management_System CREATED")
    except mysql.connector.errors.DatabaseError :
        print()
        print("Databse College_Management_System already exists ! ")

    mydb = mysql.connector.connect(host=host_name,user=user_name,passwd=mysql_passwd,database="College_Management_System")
    mycursor = mydb.cursor()

    def create_student_table():
        mycursor.execute("CREATE TABLE Student ( FirstName varchar(50), LastName varchar(50), MainsRank int , College varchar(50) , Branch varchar(50) )")
        mydb.commit()

    try :
        create_student_table()
        print("Required tables created !")
        print()

    except :
        print("Required tables already exists")
        print()
    def take_data() :
        # print()
        path = input("Enter your txt file path :")
        fh = open(path,"r")
        records = fh.read().splitlines()
        # print(record)
        return records
    mycursor.execute('DELETE FROM Student')
    mydb.commit()

    for record in take_data() :
        data = record.split("||")
        # print(data)
        query = "insert into student(FirstName,LastName,MainsRank,College,Branch) values(%s,%s,%s,%s,%s)"
        values = (data[0],data[1],data[2],data[3],data[4])
        mycursor.execute(query,values)
        mydb.commit()

    def main() :
        while True :
            heading = "COLLEGE MANAGEMENT SYSTEM"
            print("="*len(heading.center(130,"-")))
            print("+"*len(heading.center(130,"-")))
            print(heading.center(130,"-"))
            print("+"*len(heading.center(130,"-")))
            print("="*len(heading.center(130,"-")))
            print()
            print("1. Show Table  ")
            print("2. Create PDF")
            print("3. Exit")
            print()
            choice = input("Enter your choice: ")
            print()
            if choice == "1" :
                show_table()
            # elif choice == "2" :
            #     create_pdf()
            elif choice == "3" :
                confirm = input("Do YOU REALLY WANT TO EXIT Y OR N :")
                if confirm == "Y" :
                    print("BYE")
                    break
                elif confirm == "N" :
                    print("YOU CAN CONTINUE ")

            else :
                print("INVALID choice")

    def show_table() :

        heading = "COLLEGE MANAGEMENT SYSTEM "

        sub_1 = "STUDENT"
        sub_2 = "<SHOW>"
        print("="*len(heading.center(130,"-")))
    # print("+"*len(heading.center(130,"-")))
        print(heading.center(130,"-"))
        print(sub_1.center(130,"-"))
        print(sub_2.center(130,"-"))
    # print("+"*len(heading.center(130,"-")))
        print("="*len(heading.center(130,"-")))
        print()

        mycursor.execute("SELECT * FROM Student ")
        rec = mycursor.fetchall()
        print("-"*136)
        print(tabulate(rec , headers= ["FirstName","LastName","MainsRank","College","Branch"]))
        print("-"*136)
        print()

    # def create_pdf() :


    main()





except mysql.connector.errors.ProgrammingError as e :
    print()
    print("Error",e)
    print("Incorrect User or password")
