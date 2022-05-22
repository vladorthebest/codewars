class RomanNumerals:
    
    def to_roman(val):
        values = [(1,'I'), (4,'IV'), (5,'V'), (9,'IX'), (10,'X'), (40,'XL'), (50,'L'), (90,'XC'), (100,'C'), (400,'CD'), (500,'D'), (900,'CM'), (1000,'M')][::-1]
        result = ''
        for value, name in values:
            for i in range(0,val//value):
                result += name
                val -= value
        return result

    def from_roman(roman_num):
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = []
        s = []
        for i in roman_num:
            num.append(values[i])
        print(num)
        for index, i in enumerate(num):
            for j in num[index+1:index+2]:
            
                print(i)
                if i < j:
                    s.append(-i)
                elif i == j:
                    if s:
                        s[-1]+= i
                    else:
                        s.append(i)
                else:
                    s.append(i)
            last = i
        s.append(last)   
        print(s)
        return sum(s)