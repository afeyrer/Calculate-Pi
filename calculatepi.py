"""
calculatepi.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""
a=input("I will estimate pi. How many terms should I use?")
b=input("How many decimal places should I use in the result?")
z=int(a)
c=int(b)
hundred=range(0,z)
thing=list(hundred)
calc= lambda f: ((-1)**f)/(2*f+1)
y=[calc(x) for x in thing]
total=sum(y)
pi=str(4*total)
print("The approximate value of pi is {0}".format(round(pi,c)))
