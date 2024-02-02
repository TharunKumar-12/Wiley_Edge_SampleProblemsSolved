n=int(input())
#Creating seperate list for every dishes to store their durations of time taken by each chef.
a=[]
b=[]
c=[]
for i in range(n):
    dish=input()
    time=int(input())
    if dish=='A':
        a.append(time)
    elif(dish=='B'):
        b.append(time)

    else:
        c.append(time)

min_a=min(a)
min_b=min(b)
min_c=min(c)
min_ab=min_a+min_b
if (min_ab)>min_c:
    print(min_c)
else:
    print(min_ab)