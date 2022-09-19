#*****************simple ATM project****************
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="string1234",
    database="sbi_atm"

)
mycursor=mydb.cursor()
#******************************************************************
print("******************************WELCOME TO SBI ATM***********************")
print("0.Logout and Exit")
print("1.view Account Balance")
print("2.Withdraw cash")
print("3.Deposit cash")
print("4.Change pin")
print("5.Return card")
import random
pin=1212
balance=10000
null="_"
acc_num=12345
#*********Account number************
acc_num=int(input("Enter your account number:"))    
if acc_num==12345:
    print("please choose your choice")

#**********Logout and exit**************
    def Logout_and_exit():
     print("Thank you for visiting SBI ATM")
#************Account balance***********

    def view_account_balance(acc):
      if acc=="current account":
        print(f"your current Account balance is Rs:{balance}")
      else:
        print(f"your savings Account balance is Rs:{balance}")    

#*************withdraw*******************       
    def withdraw_cash():
     print(f"your current total balance is Rs:{total_balance_with} ")

#************deposit******************
    def deposit_cash():
     print(f"your current total balance is Rs:{total_balance}")    

#***********change pin number*******************
    def change_pin():
     print("")    
    def return_card():
     print("please take your ATM card")
    user=int(input("Enter your number:"))
    pin=int(input("Enter your pin:"))
    if pin==1212:
     print("Authorized!")
     if user==0:
       Logout_and_exit()
     if user==1:
         print("Current Account")
         print("Savings Account")
         acc=input("Enter your Account type:").lower().strip()
  
         view_account_balance(acc)
     if user==2:
       withdraw_amount=int(input("enter the amount you want to Withdraw:"))
       total_balance_with=balance-withdraw_amount
       print(f"your successfully withdraw amount is Rs:{withdraw_amount}")
       sql="insert into data(account_number,password,account_balance,withdraw,deposit,available_balance)values(%s,%s,%s,%s,%s,%s)"
       val=(acc_num,pin,balance,withdraw_amount,null,total_balance_with)
       mycursor.execute(sql,val)
       mydb.commit()
       withdraw_cash()

     if user==3:
       deposit_amount=int(input("enter the amount you want to deposit:"))
       total_balance=balance+deposit_amount
       print(f"your successfully deposited amount is Rs:{deposit_amount}")
       sql="insert into data(account_number,password,account_balance,withdraw,deposit,available_balance)values(%s,%s,%s,%s,%s,%s)"
       val=(acc_num,pin,balance,null,deposit_amount,total_balance)
       mycursor.execute(sql,val)
       mydb.commit()
       deposit_cash()

     if user==4:
       ph_num=int(input("enter your phone number:"))
       if ph_num==6379338484:
         print("your phone number is verified")
#**********************generating OTP*********************         
         print("your otp is generating wait a minute")
         OTP=(random.randint(1000,9999))
         print(OTP)
         a=int(input("Enter your otp:"))
         if a==OTP:
          print("Verified otp")
          new_pin=int(input("Enter the new pin you want to change:"))
          pin=new_pin
          re_pin=int(input("Re enter the pin:")) 
          new_pin=re_pin
          print("pin successfully changed")

         else:
           print("invalid otp")      

       else:
        print("invald phone number")

     change_pin()    
     if user==5:
      return_card()    
      
    else:
      print("invalid pin number")
else:
  print("invalid account number")







