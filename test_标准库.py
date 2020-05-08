import os

#os.mkdir("testdir")
print(os.listdir("./"))
#os.removedirs("testdir")
print(os.getcwd())

print(os.path.exists("newtest"))
if  not os.path.exists("newtest"):
    os.mkdir("newtest")
print(os.path.exists("newtest"))

if not os.path.exists("newtest/data.txt"):
    with open("newtest/data.txt","w") as f:
         f.write("hello, os using")