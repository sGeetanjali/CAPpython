'''
a={1,3,4}
print(a)

s={"Ms","Anjali","s"}
print(s)


empty_set =set()
print(empty_set)

set_from_list= set([1,2,1,4,3])
print(set_from_list)
'''

a=set("mississippi")
print(a)



a.add('r')
print(a)
a.remove('m')
print(a)
a.discard('a')
print(a)


a.pop()
print(a)

a.pop()
print(a)

a.clear()
print(a)

a= set ("anjalisaroha")
print(a)
b =set("raveena")
print(b)


c =a - b  #(different)
print(c)
d =a | b  #(union)
print(d)


e =a & b  #(intersection)
print(e)

f = a ^ b  #(symmatric a-b | b-a)
print(f)


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(knights)

for k, v in knights.items():
    print(k, v)




