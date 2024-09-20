import random
import os
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix-based systems (Linux, macOS, etc.)
    else:
        os.system('clear')
def display():
    print("#=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=#")
    print("#=#=#=                                                          =#=#=#")
    print("#=#=#=             Welcome TO Password Generator                =#=#=#")
    print("#=#=#=                                                          =#=#=#")
    print("#=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=##=#=#=#")

    print("\n" * 2)
    print(" " * 20 + "* * * * * * * * * * * * * ")
    print(" " * 20 + "*                       *")
    print(" " * 20 + "*      Let's create     *")
    print(" " * 20 + "*   a strong password!  *")
    print(" " * 20 + "*                       *")
    print(" " * 20 + "* * * * * * * * * * * * *")
    print("\n" * 2)

    print(" " * 16 + "************************************")
    print(" " * 16 + "*  Follow the instructions below   *")
    print(" " * 16 + "* to generate a secure password.   *")
    print(" " * 16 + "************************************")
    print("\n" * 2)
    print(" "* 19 + "Choose No. of Spacial Character at max 10")
    print(" "* 19 + "Choose No. ofdigits at max 10")
    print(" "* 19 + "Choose No. of Alphabets at max 10")

def get():
        s=int(input("Enter number of special Character You want to Add in password :   "))
        d=int(input("Enter number of digits You want to Add in password  :  "))
        a=int(input("Enter number of alphabets You want to Add in password  :  "))
        return(s,d,a)
def digit_aplpha_special():
              special_characters = (
                  "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
              )
              special_characters=list(special_characters)
              digits=(
                  "0123456789"
              )
              digits=list(digits)
              alphabets=(
                  "abcdefghijklmnopqrstuvwxyz"
              )
              alphabets = list(alphabets)
              return (special_characters,digits,alphabets)
def password_generator(s,d,a):
              sp=[]
              di=[]
              al=[]
              for i in range(0,s):
                sp.append(special_characters[random.randrange(0,s)])
              for i in range(0,a):
                al.append(alphabets[random.randrange(0,a)])
              for i in range(0,d):
                di.append(digits[random.randrange(0,d)])
              concat=sp+al+di
              shuffel=[]
              for i in range(len(concat)):
                shuffel.append(concat[random.randrange(0,len(concat))])
              password= "".join(shuffel)
              print(password)
display()
print("\n" * 2)
choice=input(" DO You Want To Generate Strong Password Then press 'Y' if Dont't Press 'N'")

if (choice=='y' or choice=='Y'):
  again=True
  
  while(again):
        clear_screen()
        s,d,a = get()
        if(a<=10 and d<=10 and s<=10):
              
              special_characters , digits, alphabets = digit_aplpha_special()
              print(special_characters)
              print(digits)
              print(alphabets)
              print("number of the alphabets You choose " +str(a))
              print("number of the digits You choose " +str(d))
              print("number of the alphabets You choose " +str(a))
              password_generator(s,d,a)
              print("\n" * 4)
              choice=input(" DO You Want To Generate Again Strong Password Then press 'Y' if Dont't Press 'N'")
              if (choice=='N' or choice=='n'):
                again=False
                print("****************************************")
                print("*                                      *")
                print("*          T H A N K   Y O U           *")
                print("*                                      *")
                print("****************************************")
                print(" ")
                print(" ")
                print("  @@@@@@@@    @@@  @@@    @@@    @@@    ")
                print("  @@@@@@@@@   @@@  @@@   @@@@    @@@    ")
                print("  @@!   @@@   @@!  @@@  @@!@@    @@!    ")
                print("  @!@   @!@   @!@  !@! @!@  !@!  @!@    ")
                print("  @!@!@!@!    @!@  !@! @!@  !@!  @!!    ")
                print("  !!!@!!!!    !@!  !!! !!!  !@!  !!!    ")
                print("  !!:  !!!    !!:  !!! !!:  !!!  !!:    ")
                print("  :!:  !:!    :!:  !:! :!:  !:!  :!:    ")
                print("  ::   :::    ::::: ::  ::   ::   ::    ")
                print("  :    : :     : :  :    :   :   :      ")
                print(" ")
                print(" ")
                print("****************************************")
                print("*    W e   A p p r e c i a t e   Y o u  *")
                print("****************************************")
        else:
                clear_screen()
                print("\n" * 2)
                print(" " * 16 + "************************************")
                print(" " * 16 + "*         Invalid Input!           *")
                print(" " * 16 + "*    Please enter 'Y' or 'N'.      *")
                print(" " * 16 + "************************************")
                print("\n" * 2)
                input("Press Enter to continue...")
else:
        clear_screen()
        print("\n" * 2)
        print(" " * 16 + "************************************")
        print(" " * 16 + "*       Thank You                  *")
        print(" " * 16 + "*       for coming'.               *")
        print(" " * 16 + "************************************")
        print("\n" * 2)