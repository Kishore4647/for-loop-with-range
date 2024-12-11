n = 5
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)
print('hi')

'''  
iteration....

1.getting the n number as a input from the user.
2.assuming that given number is 0 and here taking fact = 1 becoz factorial of 0 is 1.
3.using for loop with range to iterate the given range.
4.taking that strating range as 1 and ending range as n+1 then only perform till n.
5.the given n = 5 , it will take 1 as strating range and 5+1 as ending range.
6.i=1, fact=1*1=1
7.i=2, fact=1*2=2
8.i=3, fact=2*3=6
9.i=4, fact=6*4=24
10.i=5,fact=24*5=120
11.loop will end bcoz range is till 6 only.
'''