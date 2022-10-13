def rd() :
    try:
        fle=open('translate.txt').read()
        print('file loaded XD :')
        words=fle.split('\n')
        wl=list()
        i=0
        while i<len(words)-1 :
            dc={'english' : words[i] , 'finglish' : words[i+1]}
            wl.append(dc)
            i+=2
        return wl
        # print(wl)

    except:
        print('file not found : ')

def en2pr():
    wl=rd()
    user_s=input(' enter english sentence : ').split('.')
    for h in user_s:
        user_w=h.split(' ')
        for word in user_w:
            for i in wl:
                if i['english']==word:
                    print(i['finglish'],end=' ')
                    break
            else:
                print(word,end=' ')
            print()

def pr2en():
    wl=rd()
    user_s=input(' enter persian sentence : ').split('.')
    for h in user_s:
        user_w=h.split(' ')
        for word in user_w:
            for i in wl : 
                if i['finglish']==word:
                    print(i['english'],end=' ')
                    break
            else:
                print(word,end=' ')
            print()

def write(new,newmean):
    with open('translate.txt','a') as f :
        f.write('\n')
        f.write(new+'\n')
        f.write(newmean)
        f.close()

def menu():
    while True :
        print('1- translation english to persian... : ')
        print('2- translation persian to english... : ')
        print('3- write new word... : ')
        print('4- exit... ')
        
        a=int(input('enter ur choice : '))
        if a==1 :
            en2pr()
        if a==2 : 
            pr2en()
        if a==3 :
            words=str(input('enter new word (english or persian) : '))
            meanwords=str(input('enter words meaning (english or persian) : '))
            write(words,meanwords)
        if a==4 :
            break
menu()