#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
def main_dir():
    directory = input("Enter the directory: ")
    filename = input("What is the filename: ")
    name = input("What is your Name?: ")
    address = input("What is your address?: ")
    phone_number = input("What is your phone number?: ")
    if os.path.isfile(filename): #check if file exists
        print("File Exists")
    if os.path.isdir(directory): #check for directory
        print("Directory exists")
        write_File = open(os.path.join(directory,filename),'w')
        write_File.write(name+','+address+','+phone_number+',\n')
        write_File.close()
        
        print("File contents:")
        readFile=open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
            readFile.close()
    else:
        print("Directory Not Here")
main_dir()

    


# In[ ]:




