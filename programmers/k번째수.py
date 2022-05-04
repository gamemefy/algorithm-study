def solution(array, commands):
    
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
    # return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))