import sys

print "enter a number"

try:
    number = int(raw_input("number"))

except ValueError:
    print "error"
    sys.exit()

print "you entered number ", number


#need over all error
#and
#like looping or enter correct value

