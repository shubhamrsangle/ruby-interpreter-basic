from lexanalysis import *
from parser import *

def parser(b,flag,done,FOR):
   
    flag=flag

    if b[0]=="puts":
        c=[]
        for j in b[1:]:
            if j in dic:
                c.append(str(dic[j]))
            else:
                c.append(str(j))
        d=''.join(c)
        if d in dic:
            print(dic[d])
        else:
            try:
                print(eval(d))
            except:
                try:
                    d='"'+d+'"'
                    print(eval(d))
                except NameError as e:
                    print("line",linenumber,":")
                    print(e)
                    exit(1)
                
        
    elif b[0]=="print":
        c=[]
        for j in b[1:]:
            if j in dic:
                c.append(str(dic[j]))
            else:
                if j.isalpha():
                    c.append('"'+str(j)+'"')
                    
                    
                else:
                    c.append(str(j))
        d=''.join(c)
        if d in dic:
            print(dic[d])
        else:
            try:
                
                print(eval(d),end=" ")
            except:
                try:
                    d='"'+d+'"'
                    print(eval(d))
                except NameError as e:
                    print("line",linenumber,":",end=" ")
                    print(e)
                    exit(1)
                
        
    elif "=" in b and b[2]!="gets":
        c=b[2:]
        d=[]

        for j in c:

            if j in dic:
                d.append(str(dic[j]))

            else:
                d.append(str(j))
                
        q=''.join(d)
        

        if q in dic:
            dic[b[0]]=dic[q]

        else:
            print(q)
            dic[b[0]]=eval(q)

    elif b[0]=="if":
        z=b[1:]
        first=z[0]
        second=z[2]

        if first in dic:

            if second in dic:
                final=str(dic[first])+str(z[1])+str(dic[second])
                

            else:
                try:
                    final=str(dic[first])+str(z[1])+str(second)
                except:
                    print("line number:",linenumber,"syntax error")
                    exit(1)
                

        else:
            try:

                if second in dic:
                    final=str(first)+str(z[1])+str(dic[second])
                    

                else:
                    final=str(first)+str(z[1])+str(second)
            except:
                print("line number:",linenumber,"syntax error")
                exit(1)
                
                
        #print(eval(final))
        try:
            if eval(final):
                flag=1
                done=0

            else:
                flag=0
                done=1
        except NameError as e:
            print("line",linenumber,":",end=" ")
            print(e)
            exit(1)

    elif b[0]=="elsif" and flag==1:
        flag=0
        done=0
        
    elif b[0]=="elsif" and flag==0:
        z=b[1:]
        first=z[0]
        second=z[2]
        
        if first in dic:
            if second in dic:
                final=str(dic[first])+str(z[1])+str(dic[second])
                
            else:
                final=str(dic[first])+str(z[1])+str(second)
                
        else:
            
            if second in dic:
                final=str(first)+str(z[1])+str(dic[second])
                
            else:
                final=str(first)+str(z[1])+str(second)        
        #print(eval(final))
                
        if eval(final):
            flag=1
            done=0
            
        else:
            flag=0
            done=1
            
    elif b[0]=="else":
        if flag==1:
            flag=0
            
        elif done==1:
            flag=1
    elif b[2]=="gets":
        dic[b[0]]=input()
        
        if len(b)==5:
            if b[4]=="to_i":
                dic[b[0]]=int(dic[b[0]])
                
            elif b[4]=="strip":
                dic[b[0]]=dic[b[0]].strip()
                
        elif len(b)==6:
            if b[5]=="to_i":
                dic[b[0]]=int(dic[b[0]])
                
    elif b[0]=="for":
        if b[2]=="in" and len(b)==6:
            FOR[0]=1
            FOR[3]=b[1]
            if b[3] in dic:
                try:
                
                    FOR[1]=dic[b[3]]
                    dic[b[1]]=int(FOR[1])-1
                except ValueError as e:
                    print("line",linenumber,":",end=" ")
                    print(e)
                    exit(1)
            else:
                try:
    
                    FOR[1]=int(b[3])
                    dic[b[1]]=int(FOR[1])-1
                except NameError as e:
                    print("line",linenumber,":",end=" ")
                    print(e)
                    exit(1)
            if b[5] in dic:
                FOR[2]=dic[b[5]]
            else:
                try:
                    FOR[2]=int(b[5])
                except ValueError as e:
                    print("line",linenumber,":",end=" ")
                    print(e)
                    exit(1)
            return flag,done,FOR

            
        FOR[0]=0
        print("Syntax Error in line",linenumber)
        exit(255)
    return flag,done,FOR
    
dic={}
flag=1
done=0
FOR=[0]*4
linenumber=0
while 1:
    ifcount=0
    forcount=0
    a=input().strip().split(' ')
    linenumber+=1
    #print(len(a))
    
    if a[0]=="end":
        flag=1
        
    if flag==1 or a[0]=="else" or a[0]=="elsif":
        if a[0]!="end":
            flag,done,FOR=parser(token(a),flag,done,FOR)
            
    if FOR[0]==1:
        array=[]
        while forcount<=ifcount:
            #print(ifcount,forcount)
            a=input().strip().split(' ')
            linenumber+=1
            if a[0]=="end":
                forcount=forcount+1
            if a[0]=="if":
                ifcount=ifcount+1
            array.append(a)
        #print(array)
        try:
            
            for i in range(int(FOR[1]),int(FOR[2])):
                dic[FOR[3]]=int(dic[FOR[3]])+1
                
                for k in range(0,len(array)):
                    
                    a=array[k]
                    if a[0]=="end":
                        flag=1
                        
                    if flag==1 or a[0]=="else" or a[0]=="elsif":
                        
                        if a[0]!="end":
                            flag,done,FOR=parser(token(a),flag,done,FOR)
        except ValueError as e:
            print("line",linenumber,":",end=" ")
            print(e)
            exit(1)
