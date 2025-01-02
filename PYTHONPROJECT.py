import datetime
class Sbi:
    bank_name="SBI"
    bank_loc="Chaitanyapuri"
    ifsc_code="sbi00123"
    bank_manager="Rahul"
    pi_code=500060
    no_of_customers=0
    customer_details={}
    transaction_details={}

    def __init__(self,name,phone,age,adhaar,address,balance,pin):
        self.name=name
        self.phone=self.validate_phone(phone)
        self.age=self.validate_age(age)
        self.adhaar=self.validate_adhaar(adhaar)
        self.address=address
        self.balance=balance
        self.pin=self.validate_pin(pin)
        # calling fun of increment_account_num() to  increment no_of_customers
        self.increment_account_num()
        acc_num=1000+self.no_of_customers
        # calling the store_customer_data() to store in customer_details
        self.store_customer_data(acc_num,self)

    @classmethod
    def increment_account_num(cls):
        cls.no_of_customers += 1

    @classmethod
    def store_customer_data(cls,acc_num,customer_data):
        cls.customer_details[acc_num]=customer_data
    #! validation of phone
    @staticmethod
    def validate_phone(mobile_num):
        if len(str(mobile_num)) ==10 and str(mobile_num).isdigit():
            return mobile_num
        else:
            raise Exception("Enter valid Mobile number")
    # ! validation of adhaar
    @staticmethod
    def validate_adhaar(ur_adhaar):
        if len(str(ur_adhaar))==12 and str(ur_adhaar).isdigit():
            return ur_adhaar
        else:
            raise Exception("Enter valid Adhaar")
    # ! validation of age
    @staticmethod
    def validate_age(ur_age):
        if ur_age >=18:
            return ur_age
        else:
            raise Exception("Not Eligible to create Account")
    # ! validation of pin
    @staticmethod
    def validate_pin(ur_pin):
        if len(str(ur_pin))==4 and str(ur_pin).isdigit():
            return ur_pin
        else:
            raise Exception("Enter Valid pin")

    #! Displaying the account details
    @classmethod
    def check_balance(cls):
        print("\n----------BALANCE PAGE-----------")
        user_acc_num=int(input("ENTER YOUR ACCOUNT NUMBER:"))
        user_pin=int(input("ENTER YOUR PIN NUMBER:"))

        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            print(f"THe current balance is :{cls.customer_details[user_acc_num].balance}")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN")
        else:
            print("INVALID USER")

    #! Depositing the amount
    @classmethod
    def deposite(cls,count=0):

        if count ==3:
            print("ATTEMPTS ARE OVER")
            return
        print("\n------------DEPOSITE PAGE---------\n")

        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER:"))
        user_pin = int(input("ENTER YOUR PIN NUMBER:"))

        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            amount=int(input("Enter the amount to deposite:"))
            if amount > 0:
                cls.customer_details[user_acc_num].balance += amount
                print(f"Rs.{amount} has been credited to your account ,"
                f"and your current balacne is {cls.customer_details[user_acc_num].balance}")

                if user_acc_num not in cls.transaction_details:
                    cls.transaction_details[user_acc_num]=[{"Date":datetime.datetime.now(),"Type":"Credited","Amount":amount,"Balance":cls.customer_details[user_acc_num].balance}]

                else:
                    cls.transaction_details[user_acc_num] +=[{"Date":datetime.datetime.now(),"Type":"Credited","Amount":amount,"Balance":cls.customer_details[user_acc_num].balance}]
            else:
                print("Enter valid Amount")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN")
        else:
            print("INVALID USER")
            cls.deposite(count + 1)

    @classmethod
    #! withdraw amount
    def withdraw(cls):
        print("\n------------WITHDRAW PAGE----------")
        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER:"))
        user_pin = int(input("ENTER YOUR PIN NUMBER:"))

        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            amount=int(input("Enter the amount to Withdraw:"))

            if amount <= cls.customer_details[user_acc_num].balance and amount >0:
                cls.customer_details[user_acc_num].balance -= amount
                print(f"Rs: {amount} has been debited from your account,"
                f"Your current balance is :{cls.customer_details[user_acc_num].balance}")

                if user_acc_num not in cls.transaction_details:
                    cls.transaction_details[user_acc_num]=[{"Date":datetime.datetime.now(),"Type":"Debited","Amount":amount,"Balance":cls.customer_details[user_acc_num].balance}]

                else:
                    cls.transaction_details[user_acc_num] +=[{"Date":datetime.datetime.now(),"Type":"Debited","Amount":amount,"Balance":cls.customer_details[user_acc_num].balance}]
            else:
                print("Insufficient Balance")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN")
        else:
            print("INVALID USER")

    #! Chnage pin
    @classmethod
    def change_pin(cls):
        print("\n------------RESET PIN----------")
        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER:"))
        user_pin = int(input("ENTER YOUR PIN NUMBER:"))

        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            new_pin=int(input("Enter New Pin:"))
            confirm_pin=int(input("Enter Confirm pin:"))

            if new_pin == cls.customer_details[user_acc_num].pin:
                print("The old pin and New pin shouldn't be Same")
            elif new_pin == confirm_pin:
                cls.validate_pin(new_pin)
                cls.customer_details[user_acc_num].pin =new_pin
                print("Your Pin Updated Successfully ****")
            else:
                print("New_pin and Confirm_pin not Matched")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN")
        else:
            print("INVALID USER")
    #! Modifying customer details
    @classmethod
    def modify_customer_details(cls):
        print("--------------------MODIFY PAGE-------------------------")

        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER:"))
        user_pin = int(input("ENTER YOUR PIN NUMBER:"))
        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            while True:
                print("\nSELECT 1 TO CHANGE NAME","SELECT 2 TO CHANGE ADDRESS",
                "SELECT 3 TO CHANGE MOBILE NUMBER","SELECT 4 TO EXIT\n" ,sep="\n")

                select=int(input("ENTER YOUR CHOICE:"))

                match select:
                    case 1:
                        print(f"Your old name is:{cls.customer_details[user_acc_num].name}")
                        new_name=input("Enter new name:")
                        confirm_name=input("Confirm your name:")
                        if new_name==confirm_name and cls.customer_details[user_acc_num].name != new_name:
                            cls.customer_details[user_acc_num].name=new_name
                            print(f"Your new name is :{new_name}")
                            print("***YOUR NAME CHANGED SUCCESSFULLY***")
                        else:
                            print("New name and Confirm name are not Matching")
                    case 2:
                        print(f"Your old address is:{cls.customer_details[user_acc_num].address}")
                        new_address=input("Enter new Address:")
                        confirm_address=input("Confirm your Address:")
                        if new_address==confirm_address:
                            print(f"Your New Address is:{new_address}")
                            cls.customer_details[user_acc_num].address=new_address
                            print("***YOUR ADDRESS CHANGED SUCCESSFULLY***")
                        else:
                            print("New Address and Confirm Addresss are not Matching")
                    case 3:
                        print(f"Your old MObile number is:{cls.customer_details[user_acc_num].phone}")
                        new_phone_num=input("Enter new Number:")
                        confirm_phome_num=input("Confirm your Number:")
                        if new_phone_num==confirm_phome_num:
                            cls.validate_phone(new_phone_num)
                            print(f"Your New Mobile Number is:{new_phone_num}")
                            cls.customer_details[user_acc_num].phone=new_phone_num
                            print("***YOUR MOBILE NUMBER CHANGED SUCCESSFULLY***")
                        else:
                            print("New MObile number and Confirm Mobile Numbers are not Matching")
                    case 4:
                        print("YOU HAVE DONE WITH MODIFICATION ,THANK YOU**")
                        break
                    case _:
                        print("****SELECT CORRECT OPTION****")
        elif user_acc_num in cls.customer_details and user_pin != cls.customer_details[user_acc_num].pin:
            print("INVALID PIN")
        else:
            print("INVALID USER")
    #! Transferring amount
    @classmethod
    def transfer_money(cls):
        print("------------TRANSFER AMOUNT PAGE---------")
        sender_acc_num=int(input("ENTER SENDER ACCOUNT NUMBER:"))
        sender_pin=int(input("ENTER SENDER PIN:"))

        if sender_acc_num in cls.customer_details and sender_pin==cls.customer_details[sender_acc_num].pin:

            receiver_acc_num=int(input("ENTER RECEIVER ACCOUNT NUMBER:"))
            receiver_ifsc=input("ENTER RECEIVER IFSC CODE:")

            if receiver_acc_num in cls.customer_details and receiver_ifsc==cls.ifsc_code:
                print("\n ***** AMOUNT BEFORE TANSFER*****\n")
                print(f"SENDER AMOUNT IS :{cls.customer_details[sender_acc_num].balance}")
                print(f"RECEIVER AMOUBNT IS :{cls.customer_details[receiver_acc_num].balance}")

                amount=int(input("ENTER AMOUNT TO TRANSFER:"))
                if amount <= cls.customer_details[sender_acc_num].balance:

                    cls.customer_details[sender_acc_num].balance -= amount
                    cls.customer_details[receiver_acc_num].balance += amount

                    print("\n*****AMOUNT AFTER TRANSFER*****\n")
                    print(f"SENDER AMOUNT IS :{cls.customer_details[sender_acc_num].balance}")
                    print(f"RECEIVER AMOUBNT IS :{cls.customer_details[receiver_acc_num].balance}")
                    print(f"{amount} : is TRANSFERED SUCCESSFULLY*****")
                else:
                    print("***INSUFFICIENT BALANCE***")

        elif sender_acc_num in cls.customer_details and sender_pin !=cls.customer_details[sender_acc_num].pin:
            print("INVALID PIN")

        else:
            print("INVALID USER")
    @classmethod
    def mini_statement(cls):
        print("\n --------------MINI STATEMENT----------")
        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER:"))
        user_pin = int(input("ENTER YOUR PIN NUMBER:"))
        if user_acc_num in cls.customer_details and user_pin==cls.customer_details[user_acc_num].pin:
            print("DATE_TIME".ljust(30),"TYPE".center(30),"AMOUNT".center(26),"BALANCE".center(10),sep="|")
            transaction_history=cls.transaction_details[user_acc_num]

            for d in transaction_history:
                print(str(d["Date"]).ljust(30),d["Type"].center(30),str(d["Amount"]).center(26),str(d["Balance"]).center(10), sep="|")

        elif user_acc_num in cls.customer_details and user_pin!=cls.customer_details[user_acc_num].pin:
            print("INVALID PIN")

        else:
            print("INVALID USER")


c1=Sbi("raju",8688172057,25,865845848584,"55/2 kothapet",1000,8888)
c2=Sbi("sujith",6785848859,23,234556781256,"1/14 tkr",5000,6767)
# print(c1.customer_details)
# c2.check_balance()
# c2.deposite()
# c2.withdraw()
# c2.change_pin()
# c2.modify_customer_details()
# c1.transfer_money()
# c2.deposite()
# c2.withdraw()
# c2.deposite()
# print(Sbi.transaction_details)
# c2.mini_statement()
