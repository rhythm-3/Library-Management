#PYTHON MODULE :Issue
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime , timedelta
from mysql.connector import(connection)
import os

def clrscreen():
    print('\n'*5)

def ShowIssuedBooks():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='sqluser', password ='password', host = 'localhost', database = 'library')
        Cursor = cnx.cursor()
        # query = ("SELECT B.bno,bname, M.mno, mname,doi,dor FROM bookRecord B, issue I, Member M where B.bno=I.bno and I.mno=M.mno")
        query = ("SELECT * from issue")
        Cursor.execute(query)
        result = Cursor.fetchall()
        print("----------------------------------------------------------------------------")
        for row in result:
            print("Book Code : ",row[0])
            # print("Book Name : ",row[1])
            print("Member Code : ",row[1])
            # print("Member Name : ",row[3])
            print("Date of issue : ",row[2])
            print("Date of return : ",row[3])
            print("----------------------------------------------------------------------------")

        # for(Bno, Bname, Mno, Mname, doi, dor) in Cursor:
        #     print("============================================================================")
        #     print("Book Code : ",Bno)
        #     print("Book Name : ",Bname)
        #     print("Member Code : ",Mno)
        #     print("Member Name : ",Mname)
        #     print("Date of issue : ",doi)
        #     print("Date of return : ",dor)
        #     print("============================================================================")
        #     Cursor.close()
        #     cnx.close()
        #     print("You have done it!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

def issueBook():
    try:
        cnx = connection.MySQLConnection (user = 'sqluser',password = 'password',host = 'localhost',database = 'library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code to issue : ")
        mno = input("Enter Member Code : ")
        print("Enter Date of Issue(Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Qry = ("INSERT INTO issue (bno,mno,doi)VALUES(%s, %s, %s)")
        data = (bno,mno,date(YY,MM,DD))
        Cursor.execute(Qry,data)

   # To make sure data is commited to the database cnx.commit()
        cnx.commit()
        cnx.close()
        print("Record Inserted............")
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close() 

def returnBook():
    try:
        cnx = connection.MySQLConnection (user = 'sqluser',password = 'password',host = 'localhost',database = 'library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code to be returned to library : ")
        Mno = input("Enter Member Code Member who is returning Book : ")
        retDate = date.today()
        Qry = ("Update issue set dor = %s WHERE bno= %s and mno = %s")
        rec = (retDate,bno,Mno)
        Cursor.execute(Qry,rec)

   # To make sure data is commited to the database cnx.commit()
        cnx.commit()
        cnx.close()
        print("Record Closed Successfully............")
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close() 