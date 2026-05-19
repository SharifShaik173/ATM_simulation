import json
import time
from datetime import datetime
current_time=datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

FILE_NAME = "atm_data.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "101": {"name": "sam", "pin": 1433, "balance": 10000.0, "statement": []},
            "102": {"name": "ram", "pin": 1566, "balance": 10000.0, "statement": []},
            "103": {"name": "sanju", "pin": 1933, "balance": 10000.0, "statement": []}
        }

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)
st=time.perf_counter()
data_Set = load_data()
outer_Loop=True
while outer_Loop:
    print("---Login your account---")
    acc_no=(input("enter your account number:"))
    if acc_no in data_Set:
        password=int(input("enter your pin:"))
        if data_Set[acc_no]["pin"]!=password:
            print("incorrect password, try again..")
        else:
            print("login successful")
            while True:
                print("--- ATM Menu--- \n 1. show your balance \n 2. Deposite \n 3. Withdraw \n 4. Tranaction statement \n 5. User Details \n 6.Change password \n 7.logout \n 8.Exit")
                try:
                    x = int(input("choose a number: "))
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue 
                if x==1:
                    print("my balance is :",data_Set[acc_no]["balance"])
                elif x==2:
                    Deposite=float(input("enter your deposite amount:"))
                    data_Set[acc_no]["balance"]+=Deposite
                    print("Do you want to Deposite? \n 1.yes \n 2.no")
                    x=int(input("choose your choice:" )) 
                    if x==1:
                        data_Set[acc_no]["statement"].append(f"Deposite :₹{Deposite} amount at {current_time}")
                        save_data(data_Set)
                        print("your Balance updated successfully")
                    else:
                        print("amount cancelled to deposite")
                elif x==3:
                    Withdraw=float(input("enter a withdraw amount:"))
                    withdraw_password=int(input("enter your password:"))
                    if withdraw_password==data_Set[acc_no]["pin"]:
                        if Withdraw<=data_Set[acc_no]["balance"]:
                            print("continue to withdraw amount: \n 1.Yes\n 2.No")
                            choice=int(input("choose your option:"))
                            if choice==1:
                                data_Set[acc_no]["balance"]-=Withdraw
                                data_Set[acc_no]["statement"].append(f"Withdraw : ₹{Withdraw} amount at {current_time}")
                                save_data(data_Set)
                                print("Transation successful")
                            elif(choice==2):
                                print("Transation cancelled ")
                            else:
                                print("invalid credientials Try Again...")
                        else:
                            print("insufficient balance")
                    else:
                        print("incorrect password Try Again..")
                elif x==4:
                    print("---Bank Statement---")
                    print("user Account no:",acc_no)
                    print("user name :",data_Set[acc_no]["name"])
                    if not len(data_Set[acc_no]["statement"]):
                        print("no transations")
                    else:
                        for transation in data_Set[acc_no]["statement"]:
                            print(transation)
                        print("current Balance:₹",data_Set[acc_no]["balance"])
                elif x==5:
                    print("user Account no:",acc_no)
                    print("user name :",data_Set[acc_no]["name"])
                    print("user Balance:",data_Set[acc_no]["balance"])
                elif x==6:
                    password=int(input("enter your old password:"))
                    if data_Set[acc_no]["pin"]==password:
                        password1=int(input("enter new password:"))
                        password2=int(input("enter password again:"))
                        if data_Set[acc_no]["pin"]==password1 and data_Set[acc_no]["pin"]==password2:
                            print("old and new passwords are same..")
                        elif password1==password2:
                            print("password changed successfully..")
                            data_Set[acc_no]["pin"] = password1
                            save_data(data_Set)
                        elif password1!=password2:
                            print("entered passwords are not same..")
                        else:
                            print("invalid password..")
                    else:
                        print("incorrect password..")
                elif x==7:
                    print("logout successfully")
                    acc_no=None
                    break
                
                elif x==8:
                    print("Thank You for using ATM..")
                    et=time.perf_counter()
                    time_taken=et-st
                    print(f" Total time taken: {time_taken} seconds.")
                    outer_Loop=False
                    break
                else:
                    print("invalid choice, try again")
    else:
        print("invalid check your account number.")
        
