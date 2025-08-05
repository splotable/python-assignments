my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list[1]=15
second_list=[50,60,70]
my_list.extend(second_list)
print(my_list[2])
my_list.remove(70) #You can also use the del()to do the same,eg: del my_list[-1]
print(sorted(my_list)) #Arrenges in ascending order
print(sorted(my_list,reverse=True)) #Arranges in descending order
print(my_list)
