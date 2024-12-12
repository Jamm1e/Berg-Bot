info_track = {'first_name': 0,"last_name": 1, "birth_date": 2, "email": 3, "address": 4, "entry_term": 5, "major": 6, "gpa": 7}

# for k,v in info_track.items():
#     print(f'enter {k} code {v}')

accum = 0
lst = ['why', 'what', 'where']
lstresp = ['It works for why', 'It works for what', 'It works for where']

while True:
    email = input("Enter your email. (Enter help if needed) ")
    if email.lower() == 'help':
        question = input("What do you need help with? ")
        print(question.split())
        print([x for x in question.split() if x in lst])
        print(lstresp[lst.index(''.join([x for x in question.split() if x in lst]))])
        break
        
        #if question.split() in lst:




#for question in range(8):
    #print(question)
    
