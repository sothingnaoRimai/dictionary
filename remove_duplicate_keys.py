# Write a program to remove duplicate keys.
# Input :-

# Output :-{“ball”:”red”,”bat”:4,”wickets”:8}

a= {"ball":"red","bat":4, "wickets":8,"ball":"green","bat":3}
b=[]
o=dict()
for i ,j in a.items():
    if j not in b:
        b.append(j)
        o[i]=j
print(o)