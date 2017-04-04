#Accept input from a user
x = int(input("Enter a number: "))

if x > 1:
   # check for factors
   for i in range(2,x):
       if (x % i) == 0:
           print x," is not prime"
           break
   else:
       print x,"is prime"
       
else:
   print x,"is not a prime number"
