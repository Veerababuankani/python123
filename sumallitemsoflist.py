vb=int(input("enter the length of list:" ))
if(vb<=0):
    print("{} invalid input".format(vb))
else:
    l1=[]
    print("enter the values of list")
    for i in range (1,vb+1):
        val=int(input())
        l1.append(val)
    else:
        print("-"*50)
        print("\t\tsum of list")
        print("-"*50)
        print("\t\t{}".format(l1))
total_sum=sum(l1)
print("the sum of all item in the list is:",total_sum)
print("*"*50)
total_product=1
for l2 in l1:
    total_product*=l2
print("the sum of all item in the list is:",total_product)
print("*"*50)
l1.sort()
l1.reverse()
print("{} largest value from list".format(l1[0]))
print("{} small value from list".format(l1[-1]))
