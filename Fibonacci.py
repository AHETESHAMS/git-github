#fibonacci series
t1=0
t2=1
fibbo=0
num=int(input('Enter end number:='))
for i in range(1,num):
    print(t1)
    fibbo=t1+t2
    t1=t2
    t2=fibbo

