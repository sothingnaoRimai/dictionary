# Create a dictionary from 2 lists, where the elements of 1st list are the 
# keys and the elements of the 2nd list are the corresponding values.

# dic= {'Name', 'RAM', 'Age','k'}
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)

# OUTPUT:- {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}
list1=['one', 'two', 'three','four','five']
list2=[1,2,3,4,5,]
new_dict={list1[i]:list2[i] for i in range (len(list1))}
print(new_dict)