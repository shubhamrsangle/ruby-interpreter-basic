'''
if->i
expression->E
s->statement
p->end
e->else
'''
from lexanalysis import *
arb=[]
class parser():
    tk={}
    parsetable=[["S->a","","","S->iESR",""],["","","R->eSp","","R->p"],["","E->b","","",""]]
    terminal={}
    nonterminal={}
    def __init__(self):
        parser.terminal['a']=0
        parser.terminal['b']=1
        parser.terminal['e']=2
        parser.terminal['i']=3
        parser.terminal['p']=4
        parser.nonterminal['S']=0
        parser.nonterminal['R']=1
        parser.nonterminal['E']=2
    def map2(self,tok):
        n=len(tok)
        parser.tk["if"]='i'
        parser.tk["else"]='e'
        parser.tk["end"]='p'
        parser.tk["True"]='b'
        parser.tk["False"]='    b'
    def parse(self,tok):
        try:
            st=[]
            index=0
            st.insert(0,"$")
            st.insert(0,'S')
            a=parser.tk[tok[0]]
            x=st[0]
        except:
            return False
        while x!="$":
            if a=="@":
                print("Variable can't start with @")
                return False
            elif x==a:
                index+=1
                
                st.pop()
                if index==len(a):
                    return True
                a=tok[index]
            elif 65<=ord(a)<=91:
                print("error")
                return False
            elif parser.parsetable[parser.nonterminal[x]][parser.terminal[a]]=="":
                print("parsing error")
                return False
            else:
                string=parser.parsetable[parser.nonterminal[x]][parser.terminal[a]][3:]
                for k in string[::-1]:
                    st.insert(0,k)
            x=st[0]
        print("no match")
        return False
a=input().strip().split(' ')
arb=arb+token(a)
if a[0]=="if" or a[0]=="for":
    while 1:
        a=input().strip().split(' ')
        if a[0]=="end":
            break
        arb=arb+token(a)
f=parser()
f.map2(arb)
print(f.parse(arb))
