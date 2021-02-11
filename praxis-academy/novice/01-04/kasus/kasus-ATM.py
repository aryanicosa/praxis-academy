class User():
    inquiry = 0
    test_pw = 0
    atm = False
    def __init__(self, nama):
        self.nama = nama
    
    def check_password(self, password):
        self.password = password
        if self.password == '123':
            test_pw = 0
            return True
        else:
            print("Wrong Password!!!")
            self.test_pw += 1
            if self.test_pw > 3:
                print("This is not your Card")
                self.atm = False
            return False

    def deposit(self, dep):
        self.dep = dep
        self.inquiry += self.dep
        print("Your balance = ", self.inquiry)

    def withdraw(self, wd):
        self.wd = wd
        self.inquiry -= self.wd
        print("Your balance = ", self.inquiry)

    def balance_inquiry(self):
        print("Your balance = ", self.inquiry)
    

print("welcome to simple ATM system")
uname = "user" 
user = User(uname)
user.atm = True 

while user.atm == True:
    pw = input("Input your password first\n")

    while user.check_password(pw) == True:
        print("Choose a service\n1. Deposit\n2. Withdraw\n3. Balance Inquiry\n4. Cancel")

        value = input()
        if value == '1':
            dep_val = int(input("Nilai deposit "))
            user.deposit(dep_val)
        elif value == '2':
            wd_val = int(input("Nilai withdraw "))
            user.withdraw(wd_val)
        elif value == '3':
            user.balance_inquiry()
        elif value == '4':
            print("Cancelling process")
            user.atm = False
            break
        else:
            print("No option!")