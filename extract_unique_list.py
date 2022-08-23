
# # output [7,8,9,1,3,4,2]
a={"list1":[7,8,9,1],"list2":[9,3,4,8],"list3":[9,4,2,1,9]}

b=[]
for i in a:
    if a[i][0] not in b:
        b.append(a[i][0])
    if a[i][1] not in b:
        b.append(a[i][1])
    if a[i][2] not in b:
        b.append(a[i][2])
    if a[i][3] not in b:
        b.append (a[i][3])
print(b)
