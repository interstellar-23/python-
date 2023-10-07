dict1={10230000:"AAA",10230001:"BBBB",10230002:"CCCC"}
dict2={}
for key in dict1:
    if key%2!=0:
        dict2[key]=dict1.get(key)
print(dict2)