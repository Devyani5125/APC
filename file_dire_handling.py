# 1.Read-r
# Purpose: Open an existing file only to read its contents.
# f=open("data.txt","r")
# content=f.read()
# f.close()

# 2.Write-
# Purpose: Create a new file or completely overwrite an existing one.
# f=open("data.txt","w")
# f.write("The Good Will Hunting")
# f.close()

# 3.Append-a
# Purpose: Add new content to the end of a file without erasing what's already there.
# f=open("data.txt","a")
# f.write("\nThe Persuit Of Happyness")
# f.close()

# 4.Read+Write-r+
# Purpose: Read and write to an existing file without deleting its old content.
# f=open("data.txt","r+")
# print(f.read())
# f.write("\nDead Poets Society")
# f.close

# 5.Write+read-w+
# Purpose: Wipe the file, write new content, 
# and then also be able to read it back — all in the same session
# f = open("data.txt", "w+")
# f.write("\nHopper"
# "\nSwapped"
# "\nInside Out")
# f.seek(0)
# print(f.read())
# f.close()

# 6.Append+read-a+
# Purpose-Existing content is preserved. 
# New text is appended
# f=open("data.txt","a+")
# f.write("\nGood Vibes,Good life"
# "\nHow to win friend and influence people")
# f.seek(0)
# print(f.read())
# f.close()

# 7.create-x
# Purpose: Safely create a brand-new file, 
# but only if it doesn't already exist.
# f=open("newfile.txt","x")
# f.write("\nThe days at the Morisakhi Bookshop")
# f.close()

# 8.Read Binary-rb
# Purpose: Read non-text (binary) files like images, PDFs, executables
# f=open("image.jpg","rb")
# data=f.read()
# f.close()

# 9.Write Binary-wb
# Purpose: Write raw bytes to a file, overwriting it.
# f=open("image.jpg","wb")
# f.write(b"The art of lazyness")
# f.close()

# 10.Append Binary-ab
# Purpose: Add bytes to the end of a binary file without erasing existing content.
# f=open("data.bin","ab")
# f.write(b"Hello")
# f.close()

# 11.Read+Write Binary-rw+
# Purpose: Read and write binary data on an existing file.
# f = open("data.bin", "rb+")
# data = f.read()
# print(data)
# f.write(b"The Art of being alone")
# f.close()


# directiory
# Definition: Directory handling is the process of creating, viewing, changing, 
# and removing folders using Python. 
# The built-in os module provides functions for performing directory operations.

# 1)get the current directiory
import os

print(os.getcwd())

# 2)creat
import os

os.mkdir("MyFolder")
print("Directory created")

# 3)list files and dire
import os

print(os.listdir())

# 4)remane a dire
import os

os.rename("MyFolder", "NewFolder")
print("Directory renamed")

# 5)remove the empty dir
import os

os.rmdir("NewFolder")
print("Directory removed")