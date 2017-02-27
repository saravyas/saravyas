import os
f1=open("saravyas.txt","r")
f3=open("python1.txt","r")
#print f1content.read()
f2=open("c:/users/user/PycharmProjects/project/projectsara.txt","w")
f4=open("c:/users/user/PycharmProjects/project/projectpython1.txt","w")
f5=open("c:/users/user/PycharmProjects/project/projectmerge.txt","w")
for i in f1:
    print i
    f2.write(i)
    f5.write(i)
for i in f3:
    print i
    f4.write(i)
    f5.write(i)
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()



#with statement
#file operation using "with" operator




