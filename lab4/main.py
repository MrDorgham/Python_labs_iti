import re
import time, datetime
email_regx = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regx = re.compile(r'^(?:\+?01)?[09]\d{10,10}$')







def loginMenu():
    print("you are loged in")


###########################################################################################################################

def isUser():
    global mail

    mail = input("Enter Your Email: ")
    passwd = input("Enter Your Password: ")
    fileobject = open("data/db.txt", "r")

    data = fileobject.readlines()
    for line in data:

        if mail == line.split(":")[2] and passwd == line.split(":")[3]:
            usr_id = line.split(":")[5]

            fileobject.close()

            loginMenu()
            break

    print("Wrong Email or Password !")
    isUser()

###########################################################################################################################

def isValidEmail(msg):
    email = input(msg)
    if re.fullmatch(email_regx, email):
        return email
    else:
        return isValidEmail("Enter a Valid email: ")


def isValidPhone(msg):
    phone = input(msg)
    if re.fullmatch(phone_regx, phone):
        return phone
    else:
        return isValidPhone("Enter a Valid phone number: ")


def isValidName(msg):
    name = input(msg)
    if not any(char.isdigit() for char in name):
        return name
    else:
        isValidName("Enter a Valid Name: ")
    return name
###########################################################################################################################


def Rgstr():
    ts = time.time()
    usr_id = int(ts)
    f_name = isValidName("Enter Your First Name: ")
    l_name = isValidName("Enter Your Last Name: ")
    email = isValidEmail("Enter Your email: ")
    passwd = input("Enter Your Password: ")
    confirmpswd = input("Enter Your Password Again: ")
    while confirmpswd != passwd:
        print("Password doesnot match !")
        passwd = input("Enter Your Password: ")
        confirmpswd = input("Please Confirm Your Password: ")

    phone = isValidPhone("Enter Your phone number: ")

    print("You Have Registered Successfully!")
    print(f"Your data (Name:{f_name} {l_name} Mail:{email} Password:{passwd} Phone Number:{phone} id:{usr_id}")

    fileobject = open("data/db.txt", "a")
    fileobject.writelines(f_name + ":" + l_name + ":" + email + ":" + passwd + ":" + phone + ":" + str(usr_id) + "\n")
    fileobject.close()




###########################################################################################################################


def Main_Menu():
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print ('$$----------------------------------------$$')
    print ('$$    Welcome to the Crowd Funding App    $$')
    print ('$$----------------------------------------$$')
    print ('$$    Press 1 to Registeration            $$')
    print ('$$    Press 2 to Login !                  $$')
    print ('$$    Press 0 to Exit                     $$')
    print ('$$                                        $$')
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    while True:
        user_input = input('Enter Your selection: ')
        try:
            user_input = int(user_input)
            if user_input == 1:
                Rgstr()
                Main_Menu()
            elif user_input == 2:
                isUser()
                Main_Menu()
            elif user_input == 0:
                print("Exit Now ........ !")
                exit()
            else:
                print ("Please Choose from the Menue !")
        except ValueError:
                print ("Pleaes Enter a vaild Number !")

Main_Menu()