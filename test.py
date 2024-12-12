def std_dev(X):
    count=len(X)
    total=0
    for i in X:
        total=total+i
     
    mean=total/count
    op=0
    for i in range(0,count):
        op=op+(X[i]-mean)**2
    sigma=float(op/(count-1) )**0.5  
    return sigma
 

X=[1,2,3,4,5,6,7,8,9] 
print(std_dev(X)) 