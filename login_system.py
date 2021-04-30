from sys import exit
print("LOGIN SYSTEM:")
command=int(input("Type 1 to SIGN IN, 2 to SIGN UP!\n"))
file=open("login_database.txt","a+")
#SIGNING UP
def signUp():
    gmail=checkMail(input("Type your gmail:"),"Up")
    password=checkPassword(input("Password should be at least 8 characters long, which consists of letters, numbers and underscore(_)!\n"))
    confirmation_password=input("Type the password again:\n")
    if confirmation_password==password:
        print("You successfully signed up!\nTry to SIGN IN!\nExiting program...")
        file.write(f"For {gmail}\n{password}\r\n")
        file.close()
    else:
        print("The confirmation password IS WRONG!\nExiting the program...")

def checkMail(mail,aim):
    if "@" not in mail:
        return checkMail(input("Invalid input,TRY AGAIN!\n"),aim)
    if mail.index("@")==0:
        return checkMail(input("Invalid input,TRY AGAIN!\n"),aim)
    if mail[mail.index("@"):]!="@gmail.com":
        return checkMail(input("Only Gmail is acceptable,TRY AGAIN!\n"),aim)
    if aim=="In":
        #file.close()
        file=open("login_database.txt","r")
        for line in file:'''тут есть проблема не работает чтото связано с логином'''
            if line.startswith("For"):
                print(line)
                print(line[4:])
                if line[4:]==mail:
                    print(2435)
                    return
             
        else:
            return checkMail(input("There is no such Gmail in the system.\n"),aim)
    if aim=="Up":
        if mail in file:###
            print("Account with this gmail is already existing!\nTry to SIGN IN!")
            #signIn()
            return #False
    return mail

def checkPassword(password):
    '''Function check the password which should be minimum 8 characters long, including any letter(s) and number(s) and underscore(s)('_')
       Works until the write password!'''
    if len(password)<8:
        print("Password must be AT LEAST 8 characters long!TRY AGAIN!")
        return checkPassword(input())
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
        print("Password must consist of letter(s) and number(s) and underscore(s) ('_')!\nTRY AGAIN!")
        return checkPassword(input())
def signIn():
    gmail=checkMail(input("Type your gmail:"),"In") 


if command==1:
    signIn()
if command==2:
    signUp()
