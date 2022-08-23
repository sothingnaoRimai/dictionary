# Take a list having dictionary elements as shown below (Sample Data) and then 
# store all the unique values into a list and print.
# Output :-
# ['2', '7', '9', '5', '1']
a=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
a1=[]
i=0
while i <len(a):
    if i not in a1:
        a1.append(i)
    i=i+1
print(a1)