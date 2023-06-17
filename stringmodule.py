def uppeR(s):
    if type(s)==str:
        o=[]
        for x in s:
        
            if 97<=ord(x)<=122:
                x=chr(ord(x)-32)
                o.append(x)
            else:
                o.append(x)
        return ''.join(o)
    else:
        return 'please enter string'

def loweR(s):
    if type(s)==str:
        o=[]
        for x in s:
        
            if 65<=ord(x)<=90:
                x=chr(ord(x)+32)
                o.append(x)
            else:
                o.append(x)
        return ''.join(o)
    else:
        return 'please enter string'
     


def capitalizE(s):
    if type(s)==str:                                #l=[]
        return uppeR(s[0])+loweR(s[1:])             #if 97<=ord(s[0])<=122:
    else:                                           #l.append(chr(ord(s[0])-32))
        return 'please enter string'                #for x in s[1:]:
                                                        #if 65<=ord(x)<=90:
                                                           #x=chr(ord(x)+32)
                                                           #l.append(x)
                                                        #else:
                                                           #l.append(x)
                                                    #return ''.join(l)

def titlE(s):
    if type(s)==str:
        a=[]
        if 97<=ord(s[0])<=122:
            a.append(chr(ord(s[0])-32))
        else:
            a.append(s[0])
        for x in range(1,len(s)):
            if s[x-1]==' ':
                if 97<=ord(s[x])<=122:
                    a.append(chr(ord(s[x])-32))
                else:
                    a.append(s[x])
            else:
                if 65<=ord(s[x])<=90:
                    a.append(chr(ord(s[x])+32))
                else:
                    a.append(s[x])
    else:
        return 'please enter string'
    return ''.join(a)


def isuppeR(s):
    if type(s)==str:
        for x in s:
            if 97<=ord(x)<=122:
                return False
    else:        
        return 'please enter string'        
    return True


def isloweR(s):
    if type(s)==str:
        for x in s:
            if 65<=ord(x)<=90:
                return False
    else:
        return 'please enter string'
    return True


def isalphA(s):
    if type(s)==str:
        for x in s:
            if 0<=ord(x)<=64 or 91<=ord(x)<=96 or 123<=ord(x)<=127:
                return False
            else:
                continue
        return True
    else:
        return 'please enter string'
    
def isdigiT(s):
    if type(s)==str:
        for x in s:
            if 0<=ord(x)<=47 or 58<=ord(x)<=127:
                return False
            else:
                continue
        return True
    else:
        return 'please enter string'
    
def isalphanuM(s):
    if type(s)==str:
        for x in s:
            if 0<=ord(x)<=47 or 58<=ord(x)<=64  or 91<=ord(x)<=96 or 123<=ord(x)<=127:
                return False
            else:
                continue
        return True
    else:
        return 'please enter string'
    
    
def swapcasE(s):
    if type(s)==str:
        l=[]
        for x in s:
            if 97<=ord(x)<=122:
                l.append(chr(ord(x)-32))
            elif 65<=ord(x)<=90:
                l.append(chr(ord(x)+32))
            else:
                l.append(x)
    else:
        return 'please return string'
    return ''.join(l)