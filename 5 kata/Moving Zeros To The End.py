def move_zeros(array):
    zeros = []
    while 0 in array:
        array.remove(0)
        zeros.append(0)
    while zeros:
        array.append(zeros.pop())
        
        
    return array