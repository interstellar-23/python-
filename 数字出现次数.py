def count_numbers(list):
    dict1={}
    for num in list:
        if num in dict1:
            dict1[num]+=1
        else:
            dict1[num]=1
    return dict1
dict2=[1,5,6,5,5,5,4,1,1,1,2,5,3,4,6]
print(count_numbers(dict2))