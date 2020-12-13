import pymysql
import datetime
date_t=datetime.datetime.now()
servername="localhost"
username="root"
password=""
dbname="railway_system"
try:
    con=pymysql.connect(servername,username,password,dbname)
except:
    print("connectivity Error")
else:
    print("Connect successfully")

print("<--------Welcome to Railine------------------>")

def book():
    global phone
    #print("\n",l1)
    srt_point=input("Enter the starting point from the above list : ")
    end_point=input("Enter the Ending point from the above list : ")
    number=int(input("Enter the number of ticket you want to book : "))
    date=input("Enter date of journer : ")
    month=input("Enter month of journey: ")
    j_date=date + "-" +month
    
    for i in range(1,number+1):
        today_date=datetime.datetime.now()
        name=input("Enter Passanger name  : ")
        age=int(input("Enter Passanger age : "))
        cursor_2=con.cursor()
        sql="INSERT INTO book_ticket (name,age,starting_point,end_point,book_date,j_date,phone) VALUES ('{}','{}','{}','{}','{}','{}')".format(name,age,srt_point,end_point,date_t,j_date)
        cursor_2.execute(sql)
        con.commit()
        print(i," ticket registered\n")
        
    main()


def signup():
    #global again_pass
    username=input("Enter your username:")
    password=input("Enter your password: ")
    again_pass=input("enter your password again: ")
    phone=int(input("Enter your Phone number"))
    if password==again_pass:
        cursor=con.cursor()
        sql="INSERT INTO user_info (username,pass,phn) VALUES ('{}','{}','{}')".format(username,password,phone)
        cursor.execute(sql)
        con.commit()
        print("Account Create succesfully \n--------")
        log_sign()
        
    else:
        print("Something Went wrong\n------")



def login():
    username=input("Enter your username : ")
    password=input("Enter your password : ")
    if password==password:
        cursor_1=con.cursor()
        sql="SELECT * FROM user_info WHERE username='{}' and pass='{}'".format(username,password)
        cursor_1.execute(sql)
        a=cursor_1.fetchall()
        print("Login successfully")
        main()  
        
        
    else:
        print("Invalid details Login again\n------------")
        login()

def logout():
     #user_id=""
    print("You are logged out properly\n")
    log_sign()

def main():
    print("1.Book a ticket\n2.Update your Profile\n3.Rail enquiry\n4.view ticket\n5.Report Issue\n6.Delete Account\n7.Log Out")
    ch_1=int(input("Enter the choice:"))
    if ch_1==1:
        book()
    elif ch_1==2:
        update()
    elif ch_1==3:
        enquiry()
    elif ch_1==4:
        view()
    elif ch_1==5:
        report()
    elif ch_1==6:
        delete()
    elif ch_1==7:
        logout()
    else:
        print("Invalid Choice")
        
def log_sign():
    print("1.login\n2.signup\n3.main")
    ch=int(input("Enter the choice:"))
    if ch==1:
        login()
    elif ch==2:
        signup()
    elif  ch==3:
        main()
    else:
        print("Something wrong")

log_sign()
    
