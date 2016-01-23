import sys
arg=sys.argv
n=int(arg[1])
def FizzBuzz(n):
    for i in range(1,n):
        if i%2==0 and i%3==0:
            print i," fizzbuzz"
            continue
        if i%3==0:
            print i," buzz"
            continue
        if i%2==0:
            print i, " fizz"
            continue
        else:
            print i
FizzBuzz(n)
