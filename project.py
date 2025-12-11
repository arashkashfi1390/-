def code () : 
    f = open('contect.txt','r')
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
def azafe_adam() : 
    name =  input()
    n_p =  input()
    f  =  open('contect.txt','a')
    f.write(name+":"+n_p+'\n')
    f.close()
def saves(poeple,numbers) : 
    f =  open("contect.txt",'w')
    for i in range(len(poeple)) : 
        f.write(poeple[i]+":"+numbers[i])
    f.close()
    f = open('contect.txt','r')
    print(f.read())
    f.close()
def search_people() : 
    pople,number  = code()
    po =  input()
    if po in pople : 
        s = pople.index(po)
        print(number[s])
    else: 
        print("not in side ")
def search_numbers()  : 
    pople,number  = code()
    po =  input()
    if po in number :
        s = number.index(po)
        print(pople[s])
    else: 
        print("not in the list ")

def edit(): 
    n =  input("name") 
    ph =  input("phone number ")
    poeple,number =  code()
    if n in poeple : 
        number.pop(poeple.index(n))
        number.insert(poeple.index(n),ph)
    elif ph in number : 
        poeple.pop(number.index(ph))
        poeple.insert(number.index(ph),n)

    saves(poeple=poeple,numbers=number)
def delet () : 
    print("برای حذف فرد یک را وارد کنید ")
    print("برای حذف شماره تماس دو را وارد کنید ")
    m =  int(input("میخواهید کل فرد را حذف کنید یا فقط شماره تلفن را ")) 
    if m ==  2 : 
        phone_number =  input('phone number  to delet ')
        poeple,number= code()
        number.insert(number.index(phone_number),'')
        number.remove(phone_number)
    elif m == 1 : 
        name =  input(' name   to delet ')
        poeple,number= code()
        print(poeple)
        number.pop(poeple.index(name))
        poeple.remove(name)
    saves(poeple=poeple,numbers=number)
while True : 
    print("چه کاری میخواهید بکنید ")
    print("1-ثبت ادم جدید ")
    print('2-جستوجوی ادم ')
    print("3-doifhodfh")
    print("edit  4") 
    print("dlete 5")
    a =  int(input())
    if a ==  1 : 
        azafe_adam()
    elif a ==  2 : 
        search_people()
    elif a ==  3 : 
        search_numbers()
    elif a ==  4 : 
        edit()
    elif a ==  5 : 
        delet()
    f = open('contect.txt','r')
    print(f.read())