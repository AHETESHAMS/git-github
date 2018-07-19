List=[3,5,4,6,8]
num=int(input('Enter the number:='))
listLen=len(List)
n=int(listLen/2+1)
if(List[n]>num):
    for i in range(0,n):
        if(List[i]==num):
            print('Number found at the location:=',i)
else:
    for i in range(n,listLen):
        if(List[i]==num):
            print('number found at location:=',i)