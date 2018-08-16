'''

range(3)
print(a)

for i in range(10):
    print(i)
    
for i in range(5, 10):
    print(i)


for i in range(2, 12, 3):
    print(i)


for i in range(-7, -30, -5):
    print(i)

    


for n in range(10):
    if n==6:
        break
    print(n, end=',')


for n in range(10):
    if n% 2==0:
        print("even",n)
        continue
    print("odd",n)
    
'''

  
def is_prime(n):
    for i in range(2, n):
        if n% i ==0:
            return False
    return True

    
n =input("enter a no: ")
for x in range(2, int(n)):
    if is_prime(x):
        print(x,"is prime")
    else:
        print(x,"not prime")
