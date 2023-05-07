import os
import shutil


#check if the directory exists or not

if (not os.path.exists("./Code/os_module/data")) : #checks path exists or not
        os.mkdir(f"./Code/os_module/data") ## create a directory
else: print("path exists")


os.getcwd() #  get current working directory
os.chdir(r"path") #change your directory
os.rename("./Code/os_module/data1", "./Code/os_module/data3") #renaming a file or folderos.rmdir("./Code/os_module/data3") #for removing folders if it is blank
shutil.rmtree("./Code/os_module/data3") # if it not empty

os.makedirs("A/B/C/D") # for creating directories and sub-directories
os.removedirs("A/B/C/D") # for removing them

os.remove("./Code/os_module/file.txt") #to remove a file


folders = os.listdir("./Code/os_module") # for listing folders and files
for j in folders: print(j)

for root,directory,file in os.walk(os.getcwd()):
    print(root)

print("PRINTING DIRECTORIES\n")
for root,directory,file in os.walk(os.getcwd()):
    print(directory) #for listing directories

print("PRINTING FILES\n")
for root,directory,file in os.walk(os.getcwd()):
    print(file) #for listing files

# for a specific file
print("PRINTING SPECIFIC FILES\n")
for root,directory,file in os.walk(os.getcwd()):
    for f in file:
        if ".py" in f:
            print(f)

check_file = os.path.isfile("./Code/os_module/main.py") # for checking if file exists or not
print (check_file)

check_folder = os.path.isdir("./Code/os_module") # for checking folder exists or not
print(check_folder)

size = os.stat("./Code/os_module/main.py").st_size # for getting the size of the file
print(f"Size of file is : {size} bytes")
print("Size : ",os.path.getsize("./Code/os_module/main.py"),"bytes") #it also gives the size in bytes

name = os.name
print(name) #name of the operating system of the depndent module imported



path = os.environ["UserProfile"] + "\Desktop" # to get a desktop folder path
print(path)

path2 = os.path.join(os.environ["UserProfile"],"Desktop") # to get a desktop folder path
print(path2)

path3 = os.path.normpath(os.path.expanduser("~/Documents")) #Another wayof getting the path
print(path3)

info_file = os.stat("./Code/os_module/main.py")
print(info_file)

path_variable = os.environ.get("PATH") # for getting the path set in the path varible
print(path_variable) 

user = os.getlogin() #for getting the username
print(user)
