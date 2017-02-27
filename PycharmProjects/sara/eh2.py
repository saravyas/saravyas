class goto1(Exception):
    pass
class goto2(Exception):
    pass
class goto3(Exception):
    pass


def loop():
    print 'start'
    num = input()
    try:
        if num<=0:
            raise goto1
        elif num<=2:
            raise goto2
        elif num<=4:
            raise goto3
        elif num<=6:
            raise goto1
        else:
            print 'end'
            return 0
    except goto1 as e:
        print 'goto1'
        loop()
    except goto2 as e:
        print 'goto2'
        loop()
    except goto3 as e:
        print 'goto3'
        loop()
