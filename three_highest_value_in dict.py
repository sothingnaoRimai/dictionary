# # Write a program to print the top 3 highest values of a given dictionary.
# # Output :-
# # [100,58,56]

d = {'second':58,'third':56,'gratest':100,'fourth':40,'fifth':20}
a=[]
max=0
nd=0
rd=0
for i in d:
    for v in d:
        if d[v]>max:
            max=d[v]
            g=v
        elif d[v] >nd and d[v]<max:
            nd=d[v]
            c=v
        elif d[v] >rd and d[v]<nd:
            rd=d[v]
            f=v
print(max,nd,rd)
