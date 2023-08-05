#PYHTON MODULE : MEMBER
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime , timedelta
from mysql.connector import(connection)
import os

def clrscreen():
    print('\n'*5)

def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection (user= 'sqluser', password = 'password', host = 'localhost', database = 'library')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM Member")
        Cursor.execute(query)
        result = Cursor.fetchall()
        # print("----------------------------------------------------------------------------")
        for row in result:
            print("----------------------------------------------------------------------------")
            print("Member Code : ",row[0])
            print("Member Name : ",row[1])
            print("Mobile No. of Member : ",row[2])
            print("Date of Membership : ",row[3])
            print("Address : ",row[4])
            print("----------------------------------------------------------------------------")
            # print(row)
        # for(Mno,Mname,MOB,DOP,ADR) in Cursor:
        #     print("============================================================================")
        #     print("Member Code : ",Mno)
        #     print("Member Name : ",Mname)
        #     print("Mobile No. of Member : ",MOB)
        #     print("Date of Membership : ",DOP)
        #     print("Address : ",ADR)
        #     print("============================================================================")
        #    Cursor.close()
            # cnx.close()
            # print("You have done it!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

def insertMember():
    try:
        cnx = connection.MySQLConnection (user = 'sqluser',password = 'password',host = 'localhost',database = 'library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code : ")
        mname = input("Enter Member Name : ")
        mob = input("Enter Member Mobile No. : ")
        print("Enter Date of Purchase(Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter Member Address : ")
        Qry = ("INSERT INTO Member (mno,mname,mob,dat,addr) VALUES(%s, %s, %s, %s, %s)")
        data = (mno,mname,mob,date(YY,MM,DD),addr)
        Cursor.execute(Qry,data)
        #print("hello")
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
        cnx.close() 

def deleteMember():
    try:
        cnx = connection.MySQLConnection(user = 'sqluser',password = 'password', host = 'localhost', database='library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code to be deleted from the Library : ")
        Qry = ("DELETE FROM Member WHERE mno = %s")
        # del_rec = (mno,)
        Cursor.execute(Qry,(mno,))

        #Make sure data is commited to the Database cnx.commit() 
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfully...........")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close() 

def SearchMember():
    # try:
    #     cnx= connection.MySQLConnection (user= 'sqluser', password = 'password', host = 'localhost', database = 'library')
    #     Cursor = cnx.cursor()
    #     mnm= input("Enter Member Name to be Searched from the Library : ")
    #     query = ("SELECT * FROM Member where mname = %s")
    #     rec_srch = (mnm,)
    #     Cursor.execute(query,rec_srch)
    #     Rec_count =0
    #     for(Mno,Mname,MOB,DOP,ADR) in Cursor:
    #         Rec_count+=1
    #         print("----------------------------------------------------------------------------")
    #         print("Member Code : ",Mno)
    #         print("Member Name : ",Mname)
    #         print("Mobile No. of Member : ",MOB)
    #         print("Date of Membership : ",DOP)
    #         print("Address : ",ADR)
    #         print("----------------------------------------------------------------------------")
    #         if Rec_count%2 == 0:
    #             input("Press any key to continue")
    #             clrscreen()
    #         print(Rec_count,"Record(s) found")
    #     #Make sure data is commited to the database cnx.commit()
    #         Cursor.close()
    #         cnx.close()
           
    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your username or password")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
    #     cnx.close()
    try:
        cnx= connection.MySQLConnection (user= 'sqluser', password = 'password', host = 'localhost', database = 'library')
        Cursor = cnx.cursor()
        mnm= input("Enter Member Name to be Searched from the Library : ")
        query = ("SELECT * FROM Member where mname = %s")
        rec_srch = (mnm,)
        Cursor.execute(query,rec_srch)
        Rec_count =0
        result = Cursor.fetchall()
        #print("----------------------------------------------------------------------------")
        for row in result:
            Rec_count+=1
            print("----------------------------------------------------------------------------")
            print("Member Code : ",row[0])
            print("Member Name : ",row[1])
            print("Mobile No. of Member : ",row[2])
            print("Date of Membership : ",row[3])
            print("Address : ",row[4])
            print("----------------------------------------------------------------------------")

        print(Rec_count,"Record(s) found")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()