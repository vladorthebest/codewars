def valid_solution(board):
    
    for i in board: 
        
        if (0 in i) or len(set(i)) != 9:
            return False
          
    for j in range(len(board[0])):
        stl = []
        for i in board:
            print(i)
            stl.append(i[j])
        if len(set(stl)) !=9 :
            return False
        
        
    cord = [(0,6), (0,3), (0,0), (3,6), (3,3), (3,0), (6,6), (6,3), (6,0)]    
    for c_i, c_j in cord:
        stl = []
        for i in board[c_i:c_i+3]:
            for j in i[c_j:c_j+3]:  
                stl.append(j)
         
        if len(set(stl)) != 9:
            return False
    
    return True