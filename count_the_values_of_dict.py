# Count the total number of items from the values of the dictionary which 
# are in the form of a list.
dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
for new_k, new_val in dict1.items():
    print(new_k,len([item for item in new_val if item]))