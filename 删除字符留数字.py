list1=[1,2,'say',4,'sugar',90,11]
list2=[a for a in list1 if type(a)==int]
list3=sorted(list2)
print(list3)
print(list1)
