def token(s):
    keywords=["print","puts","new","require","break","begin","end","alias","gets","strip","if","else","unless","for","in","while","class","def","define","do","nil",
              "not","rescue","retry","return","self","super","then","do","true","unless","until","yield","case","class","def"]

    methods=["sort","to_i","to_s","map"]

    operators=["+","-","/","%","<",">","*",".","!",":","&","(",")","{","}","[","]","-","?","#","=",'"',"'"]

    op=["(",")","{","}","[","]","'",'"']

    seprator=[",","#",";"]

    tokens=[]
    for j in a:

        if j in keywords:
            #print(j,"->keyword")
            tokens.append(j)

        elif j in methods:
            #print(j,"->methods")
            tokens.append(j)

        elif j in operators:
            #print(j,"->operators")
            tokens.append(j)

        elif j in seprator:
            #print(j,"seprator")
            tokens.append(j)

        else:
            n=len(j)
            s=j
            i=0

            while i<n:
                variable=''

                if s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':

                    while s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':
                        variable+=s[i]
                        i=i+1

                        if i==n:
                            break

                    if variable in keywords:         
                        #print(variable,"->keywords")
                        tokens.append(variable)
                        continue

                    elif variable in methods:
                        #print(variable,"->methods")
                        tokens.append(variable)
                        continue

                    else:
                        #print(variable,"->identifiers")
                        tokens.append(variable)
                        continue

                elif s[i] in operators:
                    oper=''

                    if s[i] in op:
                        #print(s[i],"->operator")
                        tokens.append(s[i])
                        i+=1
                        continue

                    while s[i] in operators:

                        if s[i] in op:
                            tokens.append(oper)
                            tokens.append(s[i])
                            oper=''
                            i+=1
                            continue
                        oper+=s[i]
                        i+=1

                        if i==n:
                            break
                    #print(oper,"->operator")
                    if len(oper)>0:
                        tokens.append(oper)
                    continue

                elif s[i] in seprator:
                    #print(s[i],"->seprator")
                    tokens.append(s[i])
                    i+=1
                    continue

                else:
                    print("error")
                    return "error"
                    break
    return tokens
def output(b,flag,done,FOR):
    
    flag=flag

    if b[0]=="puts":
        c=b[1:]
        d=''.join(c)

        if d in dic:
            print(dic[d])
        else:
            print(eval(d))

    elif b[0]=="print":
        c=b[1:]
        d=''.join(c)

        if d in dic:
            print(dic[d])
        else:
            print(eval(d),end=" ")
            print()
        
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
            dic[b[0]]=eval(q)

    elif b[0]=="if":
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
        FOR[0]=1
        if b[3] in dic:
            
            FOR[1]=dic[b[3]]
        else:

            FOR[1]=b[3]
        if b[5] in dic:
            FOR[2]=dic[b[5]]
        else:
            FOR[2]=b[5]

    return flag,done,FOR    
dic={}
flag=1
done=0
FOR=[0]*3
while 1:
    ifcount=0
    forcount=0
    a=input().strip().split(' ')
    
    if a[0]=="end":
        flag=1
        
    if flag==1 or a[0]=="else" or a[0]=="elsif":
        if a[0]!="end":
            flag,done,FOR=output(token(a),flag,done,FOR)
            
    if FOR[0]==1:
        array=[]
        while forcount<=ifcount:
            #print(ifcount,forcount)
            a=input().strip().split(' ')
            if a[0]=="end":
                forcount=forcount+1
            if a[0]=="if":
                ifcount=ifcount+1
            array.append(a)
        #print(array)
            
        for i in range(int(FOR[1]),int(FOR[2])):
            
            for k in range(0,len(array)):
                
                a=array[k]
                if a[0]=="end":
                    flag=1
                    
                if flag==1 or a[0]=="else" or a[0]=="elsif":
                    
                    if a[0]!="end":
                        flag,done,FOR=output(token(a),flag,done,FOR)
