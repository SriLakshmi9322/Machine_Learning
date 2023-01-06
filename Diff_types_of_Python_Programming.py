#Traditional functional programming
TDS=[10,20,30,40,50]
i=0 #initialize
for x in TDS:
    TDS[i]=x+10
    i=i+1 #increment
    
print(TDS)

#Convert above traditional functional programming to better in python
age=[1,2,3,4,]
#i=0
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
for i,e in enumerate(age):
    age=e+10
    
print(age)

#Convert above traditional functional programming to MOST EFFICIENT in python by using
# Map is more effective,scalable and parallel process mechanism
# Use map object instead of for loop
age = [1,2,3,4]
weight = [5,10,15]
def incr(e, f):
    return e+f+10

total = list(map(incr, age, weight))
print(total)

# Let us write even shorter code using lambda
# Lambda is anonymous function/in-line function
# Note that lambda is used only when you don't want to re-use the function and use just at one place
age = [1,2,3,4,]
# i=0
age = list(map(lambda e:e+10,age)) # Lambda is replacing incr function here
print(age)
