import os
#Opens file in Read only mode
f=os.open("Factorial.py",os.O_RDONLY)
#Read contents of the file
contents=os.read(f,1024)
os.close(f)#close the file

import os
# Opens file for write only mode
f = os.open("Factorial.py", os.O_WRONLY)
# The content to write into the file, assuming it's a string
content_to_write = "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n"
# Write into the file
os.write(f, content_to_write.encode('utf-8'))
# Close the file
os.close(f)

import os
# Specify the actual path to your directory
directory_path = "C:\Users\S.Prabha\OneDrive\Desktop\Python_Prog"  # Replace with the correct local path
# List contents of the directory
folders = os.listdir(directory_path)
# Print the list of files and directories
print(folders)
# Print each item in the list
for folder in folders:
    print(folder)
