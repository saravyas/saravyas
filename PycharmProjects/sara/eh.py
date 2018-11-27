import sys

print "Enter A Number"

try:
    number = int(raw_input("number"))

except ValueError:
    print "error"
    sys.exit()

print "You Entered Number ", number


#need over all error
#and
#like looping or enter correct value

