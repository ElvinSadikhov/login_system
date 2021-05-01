import os #os.system("cls")
from sys import exit
import time

def reseption():
    global command
    print("[LOGIN SYSTEM]")
    command=input("Type 1 to SIGN IN, 2 to SIGN UP!\n")
    while command!="1" and command!="2":
        command=input("Please print 1 or 2:(0 to exit!)")
        if command=="0":
            print("Exiting...")
            time.sleep(3)
            exit()
    os.system("cls")
    print("[LOGIN SUSTEM]")
        
def signIn():
    global gmail
    gmail=checkMail(input("Type your gmail:"),"In")
    time.sleep(1)
    os.system("cls")
    print("[LOGIN SUSTEM]")
    print(f"Gmail:{gmail}")
    checkPassword(input("Password:"),"In")
    
def signUp():
    global gmail,command2
    gmail=checkMail(input("Type your gmail:\n"),"Up")
    os.system("cls")
    print("[LOGIN SUSTEM]")
    print(f"Gmail:{gmail}")
    password=checkPassword(input("Type a password(must be at least 8 characters long, which consists of letters, numbers and underscore(_)!)\n"),"Up")
    os.system("cls")
    print("[LOGIN SUSTEM]")
    print(f"Gmail:{gmail}")
    confirmation_password=input("Type the password again:\n")
    if confirmation_password==password:
        print("You successfully signed up!\nTry to SIGN IN!\nExiting program...")
        file=open("login_database.txt","a+")
        file.write(f"For {gmail}\n{password}\r\n")
        file.close()
        os.system("cls")
        print("[LOGIN SUSTEM]")
        print("Creating an account...")
        time.sleep(2)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        print("Success!")
        time.sleep(2)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        command2=input("Type 1 to SIGN IN or 0 EXIT!\n")
        while command2!="1" and command2!="0":
            time.sleep(1)
            command2=input("Please enter 1 or 0: ")
        os.system("cls")
        print("[LOGIN SUSTEM]")
    else:
        time.sleep(1)
        os.system("cls")
        print("The confirmation password IS WRONG!\nExiting the program...")
        time.sleep(2)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        
def checkMail(mail,aim):
    '''Regardless what is the aim, function checks for correctness of gmail(YES IT SHOULD BE GMAIL)!
       If aim is In(signing in), then function finds the given gmail in the txt file. 
       Works until the correct mail! Returns mail itself!
       if aim is Up(signing up), then function seaks for existing gmail and if it exists, runs signIn function, otherwise returns gmail itself!
    '''
    if "@" not in mail:
        time.sleep(1)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        return checkMail(input("Invalid input,TRY AGAIN!\nGmail:"),aim)
    if mail.index("@")==0:
        time.sleep(1)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        return checkMail(input("Invalid input,TRY AGAIN!\nGmail:"),aim)
    if mail[mail.index("@"):]!="@gmail.com":
        time.sleep(1)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        return checkMail(input("Only Gmail is acceptable,TRY AGAIN!\nGmail:"),aim)
    if aim=="In":
        file=open("login_database.txt","r")
        for line in file.readlines():
            if line[4:len(mail)+4]==mail:
                file.close()
                gmail=mail
                return mail#
        time.sleep(1)
        os.system("cls")
        print("[LOGIN SUSTEM]")
        return checkMail(input("There is no such Gmail in the system.TRY AGAIN!\nGmail:"),aim)
    if aim=="Up":
        file=open("login_database.txt","a+")#
        file.close()
        file=open("login_database.txt","r")
        for line in file.readlines():
            if line[4:len(mail)+4]==mail:
                file.close()
                time.sleep(1)
                os.system("cls")
                print("[LOGIN SUSTEM]")
                print("Account with this gmail is already existing!\nTry to SIGN IN!")
                time.sleep(1)
                signIn()
                exit()
        file.close()
        return mail

def checkPassword(password,aim):
    '''If aim is ip(sign in), then function searches for given gmail and finds its password,compares it with typed one.
       Works until the correct password! DOESN'T return anything, it just signing in at with the write password!
       if aim is Up(sign up), then function checks the password which should be minimum 8 characters long, including any letter(s) and number(s) and underscore(s)('_')\
       Works until the write password! Returns password! 
    '''
    global gmail
    if aim=="In":
        file=open("login_database.txt","r")
        flag=0
        for line in file.readlines():            
            if line.startswith(f"For {gmail}"):
                flag=1
            if flag==1:
                if line[:len(line)-1]==password:    #last character is \n so we write len-1
                    file.close()
                    time.sleep(1)
                    os.system("cls")
                    print("[LOGIN SUSTEM]")
                    print("Signed in successfully!\nEnjoy!")
                    time.sleep(1)
                    os.system("cls")
                    print("[LOGIN SUSTEM]")
                    print("Exiting...")
                    return True
        time.sleep(1)
        os.system("cls")
        print("[LOGIN SUSTEM]\nPassword is not correct!TRY AGAIN!")
        print(f"Gmail:{gmail}")
        return checkPassword(input("Password:"),aim)
    if aim=="Up":
        if len(password)<8:
            time.sleep(1)
            os.system("cls")
            print("[LOGIN SUSTEM]")
            print("Password must be AT LEAST 8 characters long!TRY AGAIN!")
            print(f"Gmail:{gmail}")
            return checkPassword(input(),aim)
        flag1,flag2,flag3=0,0,0
        for char in password:
            if char.isalpha():
                flag1=1
            elif char.isdigit():
                flag2=1
            elif char=="_":
                flag3=1
        if flag1==1 and flag2==1 and flag3==1:
            return password
        else:
            time.sleep(1)
            os.system("cls")
            print("[LOGIN SUSTEM]")
            print("Password must consist of letter(s) and number(s) and underscore(s) ('_')!\nTRY AGAIN!")
            print(f"Gmail:{gmail}")
            return checkPassword(input(),aim)

reseption()      
if command=="1":
    signIn()
if command=="2":
    signUp()
    if command2=="1":
        signIn()
    else:
        os.system("cls")
        print("Exiting...")
        time.sleep(2)
