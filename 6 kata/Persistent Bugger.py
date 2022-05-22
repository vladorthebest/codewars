def persistence(num):
    n = 0
    while len(str(num))!=1:
        m = 1
        n +=1
        for i in str(num):
            m = m *int(i)
        num = m
    return n