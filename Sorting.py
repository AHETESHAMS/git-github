def bubbleSort(n):
    for i in range(0,4):
        for j in range(0,4):
            if(n[j]>n[j+1]):
                t=n[j]
                n[j]=n[j+1]
                n[j+1]=t
    return (n)
array=[5,4,2,3,6]
print(bubbleSort(array))
