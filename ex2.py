arr=input().split(",")
dict1=dict()
while len(arr) != 0:
    ele=arr[0]
    thiscount=arr.count(ele)
    dict1[ele]=thiscount
    while ele in arr:
        arr.remove(ele)        
out={i:j for i,j in sorted(dict1.items(),key=lambda item: item[1])}
out_list=list(out)
out_list.reverse()
for i in range(len(out_list)):
    out_list[i]=int(out_list[i])
print(out_list)
