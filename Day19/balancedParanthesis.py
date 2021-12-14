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
print(isBalanced(input()))