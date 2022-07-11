n=int(input("Enter the number of elements in a list:"))
i=0
list1=[]
while(i<n):
    num=int(input("Enter the element:"))
    list1.append(num)
    i+=1
for i in list1:
    if i>0:
        print(i)
    
