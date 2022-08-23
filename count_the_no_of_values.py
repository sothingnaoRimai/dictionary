dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj4', 'subj5']}
c=[]
for i in dict1:
    c=c+dict1[i]
print(len(c))