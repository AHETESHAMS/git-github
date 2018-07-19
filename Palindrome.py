num=int(input('Enter the number:='))
originalNum=num
n=num
reverseNum=0
while(n!=0):
    remainder=int(num%10)
    reverseNum=reverseNum*10+remainder
    n=int(n/10)
if(originalNum==reverseNum):
    print(originalNum,' is a palindrome number')
else:
    print(originalNum,' is not a palindrome number')
