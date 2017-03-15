# if __name__ == '__main__':
#     s = raw_input()
# def alphanum(s):
#     if('s'.isalpnum()):
#         return True
#     else:
#         return False
# def alpha(s):
#     if(s.isalpha()):
#         return True
#     else:
#         return False
# def digit(s):
#     if(s.isdigit()):
#         return True
#     else:
#         return False
# def lower(s):
#     if(s.islower()):
#         return True
#     else:
#         return False
# def upper(s):
#     if(s.isupper()):
#         return True
#     else:
#         return False
# print alphanum(s)
# print alpha(s)
# print digit(s)
# print lower(s)
# print upper(s)
from __future__ import division
    def average(array):
        for i in range(0,len(array)):
        result1=result1+array[i]
    result=result1/len(array)
    return result
    if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
