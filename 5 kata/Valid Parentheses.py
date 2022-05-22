def valid_parentheses(string):
    n=0
    for i in string:
        if i == '(':
            n+=1
        elif i == ')':
            n-=1
        
        if n < 0:
            return False
    if n!= 0:
        return False
    else:
        return True