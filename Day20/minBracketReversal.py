l=[]
def minBracketReverse(s):
    count=0
    for i in s:
        if i=='{':
            l.append(i)
        else:
            if len(l)==0:
                l.append(i)
            elif len(l)!=0 and l[-1]=='{':   #{{}}}}{{
                l.pop()
            elif len(l)!=0 and l[-1]!='{':
                l.append(i)
    if len(l)==0:
        return count
    elif len(l)==1:
        return -1
    else:
        while len(l)>1:
            c1=l.pop()
            c2=l.pop()
            if c1==c2:
                count+=1
            else:
                count+=2
    if len(l)==0:
        return count
    else:
        return -1
print(minBracketReverse(input()))