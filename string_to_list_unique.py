
string="aabbbcccaaadeaaa"
a=[]
i=0
while i<len(string):
    if string[i] not in a:
        a.append(string[i])
    i=i+1
print(a)
