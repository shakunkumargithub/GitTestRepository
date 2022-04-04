/* Initialize the List */ 
my_list=[2,3,4]

print (list(map(lambda my_list: my_list**2 ,my_list)))

list_tupples =[(0,2),(6,4),(5,6)]
list_tupples.sort(key = lambda x:x[1])
print(list_tupples)
