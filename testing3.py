def solve(num,n,k):
    e = 100
    for i in range(0,n,k):
        if num[i]==1:
            e -= 3
        else:
            e -=1
    
    
    return e
        



n = 8
k = 3
num = [1,1, 1, 0, 1, 1, 0, 0, 0, 0]
print(solve(num,n,k))