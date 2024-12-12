array_1=[8,69,4,79,6,2,123,1,5,14]
number=69
array_1.sort()
print(array_1)
start=1
end=len(array_1)

def binary_search(array_1,number,start,end):
    
    mid=(start+end)//2

    while(mid!=len(array_1)-1):
        if number>array_1[mid]:
            start=mid
            return binary_search(array_1,number,start,end)

        if number<array_1[mid]:
            end=mid
            return binary_search(array_1,number,start,end)
        
        if number==array_1[mid]:
            
            return print("Yes number exists in the array")
    

    print("No it does not exists")


print(binary_search(array_1,number,start,end))