import random

data = "";
with open("README.md.nocache", "r") as file:
    data = file.read() 
    data = data.replace("[randomNumberHere]", str(random.randint(1,999999999))) 
    file.close()

with open("README.md", "w") as file:
    file.write(data) 
    file.close()