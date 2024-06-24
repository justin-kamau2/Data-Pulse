my_list = []   #create an empty list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40) #append the following elements to my_list: 10,20,30,40
print(my_list)

my_list.insert(1,15) #insert 15 at the 2nd position of my_list
print(my_list)

my_list.extend([50,60,70]) #Extend my list with another list[50,60,70]
print(my_list)

my_list.pop(-1) #Removing the last element
print(my_list)

my_list.sort()  #Sorting in an ascending order
print(my_list)

index_of_30 = my_list.index(30)
print(index_of_30)



