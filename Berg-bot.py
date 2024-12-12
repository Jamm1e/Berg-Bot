info_track = {'first_name': 0,"last_name": 1, "birth_date": 2, "email": 3, "address": 4, "entry_term": 5, "major": 6, "gpa": 7}

# for k,v in info_track.items():
#     print(f'enter {k} code {v}')

accum = 0
lst = ['why', 'what', 'where']
lstresp = ['It works for why', 'It works for what', 'It works for where']


def ifhelp():
    question = input("What do you need help with? ")
    print(question.split())
    print([x for x in question.split() if x in lst])
    print(lstresp[lst.index(''.join([x for x in question.split() if x in lst]))])


def first_name():
    while True:
        first_name = input("Enter your first name. (Enter help if needed) ")
        if first_name.lower != 'help':
            if first_name.isnumeric() == False: #Fix error with input "Yuri10", it is allowed as a valid name
                print(f"{first_name} is a valid first name.")
            else:
                print(f"{first_name} is an invalid first name.")        
        
        elif first_name.lower() == 'help':
            ifhelp()
            break


def last_name():
    while True:
        last_name = input("Enter your last name. (Enter help if needed) ")
        if last_name.lower != 'help':
            if last_name.isnumeric() == False :#Fix error with input "Yuri10", it is allowed as a valid name
                print(f"{last_name} is a valid last name.")
            else:
                print(f"{last_name} is an invalid last name.")        
        
        elif last_name.lower() == 'help':
            ifhelp()
            break


def birth_date():
    while True:
        birth_date = input("Enter your birth date (MMDDYYYY). (Enter help if needed) ")
        if birth_date.lower != 'help':
            if birth_date.isalpha() == True or len(birth_date) != 8:
                print(f"{birth_date} is an invalid birth date.")
            else:
                print(f"{birth_date} is a valid birth date.")
                break
        
        elif birth_date.lower == 'help':
            ifhelp()
            break


def email():
    while True:
        email = input("Enter your email. (Enter help if needed) ")
        if email.lower() != 'help':
            if '@' in email:
                print(f"{email} is a valid email to use.")
                break
            else: 
                print(f"{email} is invalid, try again.")
        
        elif email.lower() == 'help':
            ifhelp()
            break
        
        #if question.split() in lst:


# def address():
#     while True:
#         address = input("Enter your address. (Enter help if needed) ")
#         if address.lower != 'help':


#         #elif email.lower() == 'help':
#             ifhelp()
#             break


def entry_term():
    while True:
        entry_term = input("Enter your enter term (Fall, Winter, Spring, or Summer). (Enter help if needed) ")
        season = ["fall", "winter", "spring", "summer"]
        
        if entry_term.lower() == 'help':
            ifhelp()
            break

        if entry_term.lower() in season:
            print(f"{entry_term} is a valid entry term.")
            break
        else:
            print(f"{entry_term} is a invalid entry term.")       


def major(): 
    while True:
        major = input("Enter your major. (Enter help if needed) ")
        if major.lower() != 'help':
            if major.isnumeric() == True:
                print(f"{major} is a valid major to use.")
            else: 
                print(f"{major} is not valid, try again.")
                break
        
        elif major.lower() == 'help':
            ifhelp()
            break
        

major()



#for question in range(8):
    #print(question)
    
