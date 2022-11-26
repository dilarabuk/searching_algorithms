x = int(input("which number you want to find with linear search algorithm from 'a' list"))
mylist = [10,14,19,26,27,31,33,35,42,44]
currentnode = 0
while mylist[currentnode] != x:
    currentnode+=1
    if currentnode == len(mylist)-1:
        if mylist[currentnode] != x:
            break
print("found in {}'th trial. Chosen number was {}.".format((currentnode+1),mylist[currentnode]))

#HERE IS AN EXAMPLE TO SHOW HOW FAST THE DEFAULT SEARCHING ALGORITHM OF PYTHON

import random
import time
mylist = []
for i in range (0,1000000):
    a = random.randint(0,500000)
    mylist.append(a)
seç = int(input("Choose any number from 0 to 500000"))
start = time.time()
if seç in mylist:
    print("Found",mylist.index(seç))
else:
    print("Not found")
print("found in {} seconds.".format((time.time())-start))


#BINARY SEARCH ALGORITHM FOR A GIVEN LIST, CHOSEN INTERVAL AND NUMBER 


b = [0,1,2,3,4,5,6,7,8,9,10]
def binary (a,low,high,x):

    if high >= low:
        mid = (high + low)//2
        print("Low, Middle, High: ", low, mid, high)
        if a[mid] == x:
            print("Found at current mid index: ", mid)
            return mid
        elif a[mid] > x:
            print("Will search left: low = ", low,"high = ",mid-1)
            return binary(a,low,mid-1,x)
        else:
            print("Wil search right: low = ", mid+1,"High = ", high)
            return binary(a,mid+1,high,x)
#After running the code you can see all the steps respectively        
"""
binary(b,0,9,1)
"""
