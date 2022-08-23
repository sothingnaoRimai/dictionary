#  Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}

# list = [1, 2, 3, 4]
# dict=c={}
# for name in list:
#     c[name]={}
#     c=c[name]
# print(dict)

list=[1,2,3,4]
dict=c={}
for name in list:
    c[name]={}
    c=c[name]
print(dict)