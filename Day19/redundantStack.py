l=[]
def isBalanced(s):
    for i in s:
        if i in '({[':
            l.append(i)
        elif i==')':
            if len(l)==0 or l[-1]!='(':
                return False
            l.pop()
        elif i=='}':
            if len(l)==0 or l[-1]!='{':
                return False
            l.pop()
        elif i==']':
            if len(l)==0 or l[-1]!='[':
                return False
            l.pop()
    if len(l)==0:
        return True
    return False
def isRedundant(s):
    count=0
    if isBalanced(s) is False:
        return False
    else:
        for i in s:
            l.append(i)
            if i==')':
                while l.pop()!='(':
                    count+=1
                if count==0 or count==1:
                    return False
                count=0
    return True
print(isRedundant(input()))