import sys
print "enter a number"
while True :
    try:
        number = int(raw_input("number\n"))

    except ValueError:
        print "error please enter a number"
        continue
    else :
        break
print "you entered number " , number







