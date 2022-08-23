dic={'a':[1,2,3],'b':[4,5,6],'c':[6,7,8]}
for i in dic:
    x=dic[i]
    sum=0
    list=[]
    j=0
    while j<len(x):
        sum=sum+x[j]
        j=j+1
    list.append(sum)
    dic[i]=list
print(dic)