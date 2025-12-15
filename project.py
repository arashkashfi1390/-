save_file = 'contect'
def saves(name_file,esms,shomares) : 
    f =  open(name_file+".txt",'w')
    for i in range(len(esms)) : 
        f.write(esms[i]+":"+shomares[i])
    f.close()
    f = open('contect.txt','r')
    print(f.read())
    f.close()
def code (name_file) : 
    f = open(name_file+'.txt','r')
    a = f.readlines() 
    l1 =  []
    for i in a : 
        b = i.split(':')
        l1.extend(b)
    f.close()
    p =  []
    n =  []
    for i in range(len(l1)): 
        if i%2 ==  0 : 
            p.append(l1[i])
        else: 
            n.append(l1[i])
    return p,n 
def azafe_adam(name_file,esm,shomare) : 
    esms,shomares = code(name_file)
    name =  esm
    n_p =  shomare
    if esm not in esms and shomare not in shomares : 
        f  =  open(name_file+'.txt','a')
        f.write(name+":"+n_p+'\n')
        f.close()
    else: 
        if esm in esms : 
            c = esms.index(esm)
            shomares.pop(c)
            shomares.insert(c,shomare)
        else: 
            c = shomares.index(shomare)
            esms.pop(c)
            esms.insert(c,esm)
        saves(save_file,esms,shomares)
def search_people(name_file,esm) : 
    poeple,number  = code(name_file)
    name =  esm 
    if name in poeple : 
        s = poeple.index(name)
        print(number[s])
    else: 
        print("not in side ")
def search_numbers(name_file,shomare)  : 
    poeple,number  = code(name_file)
    phone_number = shomare
    if phone_number in number :
        s = number.index(phone_number)
        print(poeple[s])
    else: 
        print("not in the list ")

'''
def edit(name_file,esm,shomare): 
    name =  esm
    phone_number =  shomare
    poeple,number =  code(name_file)
    if name in poeple : 
        number.pop(poeple.index(name))
        number.insert(poeple.index(name),phone_number)
    elif phone_number in number : 
        poeple.pop(number.index(phone_number))
        poeple.insert(number.index(phone_number),name)
    saves(name_file=name_file,poeple=poeple,numbers=number)
'''
def delet (name_file,fromats,esm,shomare) : 


    if fromats==  2 : 
        phone_number =  shomare
        poeple,numbers= code(name_file=name_file)
        numbers.insert(numbers.index(phone_number),'')
        numbers.remove(phone_number)
    elif fromats == 1 : 
        name =  esm
        poeple,numbers= code(name_file=name_file)
        numbers.pop(poeple.index(name))
        poeple.remove(name)
    saves(name_file=name_file,esms=poeple,shomares=numbers)
def output(name_file) : 
    f =  open(name_file+'.txt','r')
    print(f.read())
    f.close()
def clear(namefile) : 
    f= open(namefile+'.txt','w')
    f.write('')
    f.close()
w =  True
while w : 
    print("what you want to do ?")
    print("new ")
    print('search people')
    print("search numbers ") 
    print("del")
    print("output")
    print("clear")
    print("type exit ot exit")
    a =  input()
    if a ==  '1' : 
        esm =  input("enter the esm you want to add: ")
        shomare =  input("enter the shomare you want to add: ")
        azafe_adam(save_file,esm,shomare)
    if a ==  "2 ": 
        esm = input("enter the name you want to search: ")
        search_people(save_file,esm)
    if a ==  "3" : 
        shomare =  input("enter the shomare you want to search: ")
        search_numbers(save_file,shomare)
    if a ==  "4" : 
        print("you could just del the phone number of a person(2) or del the whole name and the phone number(1)")
        b = int(input("enter your number"))
        esm =  '' 
        shomare = ''
        if b == 1 : 
            esm = input('enter the name you want to del')
        if b ==2 : 
            shomare =  input('enter the number you want to del')
    
        delet(save_file,b,esm,shomare)
    if a == '5' : 
        output(save_file)
    if a =='6' : 
        clear(save_file)
    if a == 'exit' : 
        w = not True