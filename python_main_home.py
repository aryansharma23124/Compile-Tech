import os
import subprocess
a=int(input("Enter"))
if(a==1):
    with open("output.txt", "w+") as output:
        subprocess.call(["python", "./hello.py"], stdout=output);
elif(a==2):
    os.system("g++ test_cp.cpp -o test_cp ")
    with open("output.txt","w+") as output:
        subprocess.call("./test_cp",stdout=output)
else:
    os.system("gcc test.c -o test")
    #from subprocess import call
    with open("output.txt","w+") as output:
        subprocess.call("./test",stdout=output);
    #call(["./test", "args", "to", "test"])