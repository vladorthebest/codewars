def snail(snail_map):
    end = []
    n0 = 0
    n1 = len (snail_map)
    try:
        while n0 <= n1-1:

            for i in range(n0, n1):
                end.append(snail_map[n0][i])

            for i in range(n0+1, n1):
                end.append(snail_map[i][n1-1])

            for i in range(n0, n1-1)[::-1]:
                end.append(snail_map[n1-1][i])

            for i in range(n0+1, n1-1)[::-1]:
                end.append(snail_map[i][n0])

            n0+=1
            n1-=1
        return end
    except:
        return []