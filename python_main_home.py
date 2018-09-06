import subprocess
a=int(input("Enter"))
if(a==1):
    with open("output.txt", "w+") as output:
        subprocess.call(["python", "./hello.py"], stdout=output);
else:
    #from subprocess import call
    with open("output.txt","w+") as output:
        subprocess.call("./test",stdout=output);
    #call(["./test", "args", "to", "test"])