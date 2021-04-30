from sys import exit
print("LOGIN SYSTEM:")
command=int(input("Type 1 to SIGN IN, 2 to SIGN UP!\n"))
def signIn():
    global gmail
    gmail=checkMail(input("Type your gmail:\n"),"In") 
    checkPassword(input("Password:\n"),"In")
    
def signUp():
    gmail=checkMail(input("Type your gmail:\n"),"Up")
    password=checkPassword(input("Type a password(must be at least 8 characters long, which consists of letters, numbers and underscore(_)!)\n"),"Up")
    confirmation_password=input("Type the password again:\n")
    if confirmation_password==password:
        print("You successfully signed up!\nTry to SIGN IN!\nExiting program...")
        file=open("login_database.txt","a+")
        file.write(f"For {gmail}\n{password}\r\n")
        file.close()
    else:
        print("The confirmation password IS WRONG!\nExiting the program...")
        
def checkMail(mail,aim):
    '''Regardless what is the aim, function checks for correctness of gmail(YES IT SHOULD BE GMAIL)!
       If aim is In(signing in), then function finds the given gmail in the txt file. 
       Works until the correct mail! Returns mail itself!
       if aim is Up(signing up), then function seaks for existing gmail and if it exists, runs signIn function, otherwise returns gmail itself!
    '''
    if "@" not in mail:
        return checkMail(input("Invalid input,TRY AGAIN!\n"),aim)
    if mail.index("@")==0:
        return checkMail(input("Invalid input,TRY AGAIN!\n"),aim)
    if mail[mail.index("@"):]!="@gmail.com":
        return checkMail(input("Only Gmail is acceptable,TRY AGAIN!\n"),aim)
    if aim=="In":
        file=open("login_database.txt","r")
        for line in file.readlines():
            if line[4:len(mail)+4]==mail:
                file.close()
                gmail=mail
                return mail#
        return checkMail(input("There is no such Gmail in the system.TRY AGAIN!\n"),aim)
    if aim=="Up":
        file=open("login_database.txt","r")
        for line in file.readlines():
            if line[4:len(mail)+4]==mail:
                file.close()
                print("Account with this gmail is already existing!\nTry to SIGN IN!")
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
                    print("Signed in successfully!\nEnjoy!")
                    return True     
        return checkPassword(input("Password is not correct!TRY AGAIN!\n"),aim)
    if aim=="Up":
        if len(password)<8:
            print("Password must be AT LEAST 8 characters long!TRY AGAIN!")
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
            print("Password must consist of letter(s) and number(s) and underscore(s) ('_')!\nTRY AGAIN!")
            return checkPassword(input(),aim)
        
if command==1:
    signIn()
if command==2:
    signUp()
