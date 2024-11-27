#wpt print the given number is perfect number or not
n = 6
a = 0
for i in range(n):
    if n%i==0:  #the sum of its divisors is = to given number is known as perfect number.
        a+=i
if a == n:
    print('it is perfect num' )

'''
iteration...
1.get the integer as a input from the user.
2.assume that given number is 0, so that a=0.
3.using for loop to extract each and every num in the range,
   #first it will take 1 and 6%1=0 ,so a=0+1
   #then it will take 2 and 6%2=0 ,so a=1+2
   #then it will take 3 and 6%3=0 ,so a=3+3
   #then it will take 4 and 6%4 not=0 ,so  a=6 only
   #then it will take 5 and 6%5 not=0 ,so a=6 only
5. the loop will end ,
6.to check the sum of divisors equal to given number -> a==n
7.if condition satisfys print it is a perfect number.
'''