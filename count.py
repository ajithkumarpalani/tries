arr=input().split(",")
ele_arr=[]
count_arr=[]
while len(arr) != 0:
    ele=arr[0]
    thiscount=arr.count(ele)
    ele_arr.append(ele)
    count_arr.append(thiscount)
    while ele in arr:
        arr.remove(ele)
for i in range(len(ele_arr)-1):
    for j in range(len(ele_arr)-i-1):
        if count_arr[j] < count_arr[j+1]:
            ele_arr[j],ele_arr[j+1]=ele_arr[j+1],ele_arr[j]
            count_arr[j],count_arr[j+1]=count_arr[j+1],count_arr[j]
print(ele_arr)            
        
