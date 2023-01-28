import os
import pandas as pd
os.system('clear')

#Fetches User Choice
def FetchData(choice):
    if choice == 1:
        #Simple Age Data Option
        #User Input State, Create DF, Print DF
        state = str(input("Enter State Abbreviation: "))
        df = pd.read_csv("Data/VAERS.csv", encoding= 'unicode_escape')

        #Clean Data
        df2 = df[(df.STATE == state)]
        df3 = df2[['STATE','AGE_YRS','PRIOR_VAX','SYMPTOM_TEXT']]
        df4 = df3.dropna()
        
        #Display Data
        print(df4.to_string)
        input("   Press enter to Continue   ")
        return True
    elif choice == 2:
        return True
    elif choice == 3:
        return True
    elif choice == 4:
        return True
    elif choice == 5:
        return True
    elif choice == 6:
        return False    
    else:
        return True