
'''
empty={}
print(type(empty))
print(empty == dict())


a =dict(one=1, two=2, three=3)
b ={"one": 1,"two": 2,"three": 3}
print(a == b)

'''
my_dict ={"name": "Anjali","reg_no": 117098,"contact": 865876987,"course": 'MCA'}
print(my_dict)

print(my_dict ['name'])


my_dict ['name'] = "Saroha"
print(my_dict)

my_dict ['Teacher'] = "manikant roy"
print(my_dict)


my_dict1 = {"marks":[34,56,78], "avg": [23,56,78]}
print(my_dict1)

print(my_dict1.get("avg"))


print(my_dict1.keys())
print(my_dict1.values())
print(my_dict1.items())

print(len(my_dict1.items()))


print(34,23) in my_dict1.items()
for values in   my_dict1.values():
     print(values)

     
 
