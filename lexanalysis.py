def token(a):
    keywords=["print","puts","new","require","break","begin","end","alias","gets","strip","if","else","unless","for","in","while","class","def","define","do","nil",
              "not","rescue","retry","return","self","super","then","do","true","unless","until","yield","case","class","def"]

    methods=["sort","to_i","to_s","map"]

    operators=["+","-","/","%","<",">","*",".","!",":","&","(",")","{","}","[","]","-","?","#","="]

    op=["(",")","{","}","[","]"]

    seprator=[",","#",";"]

    tokens=[]
    if a[0]=='':
        return "errorrrr"
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
