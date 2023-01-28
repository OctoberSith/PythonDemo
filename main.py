import os
from menu import MenuSelection
from fetch import FetchData
os.system('clear')

#Loop Program
isOn = True

#While Loop
while (isOn == True): 
    print("=============================")
    print("=                           =")
    print("=    2023 VAERS CSV Info    =")
    print("=       Sid Software        =")
    print("=                           =")
    print("=============================")
    input("   Press enter to Continue   ")
    print("=============================")
    
    #Get User Choice
    os.system('clear')
    choice = int(MenuSelection())
    isOn = FetchData(choice)

    #Exit Message
    os.system('clear')
    print("Thanks for evaluating!")
