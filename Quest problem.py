noOfCrates= int(input())
noOfCoins=[]
for i in range(noOfCrates):
    x=int(input())
    noOfCoins.append(x)
sum=0
while(len(noOfCoins)>1):
    maxCoins=max(noOfCoins)
    id=noOfCoins.index(maxCoins)
    
    sum+=noOfCoins[id]
    if (id>0 and id<(len(noOfCoins)-1)):
        noOfCoins.pop(id+1),noOfCoins.pop(id-1)
    elif id==0 :
        noOfCoins.pop(id+1)
        
    if (id == (len(noOfCoins)-1)):
        noOfCoins.pop(id-1)
 
    noOfCoins.remove(maxCoins)

if len(noOfCoins)==1:
    sum+=noOfCoins[0]
print(sum)