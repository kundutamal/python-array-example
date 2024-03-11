"""
In this example we are going to write some content using file write. 
later read the content and display the data in the console.
"""

a = ["wipro ", "TCS ", "Xoriant "]
with open("file.txt", mode="w+") as file:
    for i in a:
        file.writelines(f"{i} \n")

with open("file.txt") as file:
    data = file.readlines()
    for i in data:
        print(i)