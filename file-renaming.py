#!/usr/bin/python3
import string
import os

def file_rename(files,alphadict):
    for file in files:
        file1 = file.split(' ')
        #get the base file name
        base = file1[0]
        file2 = file1[1].split('_')
        #get the name and number that will be used
        name = file2[0]
        num = int(file2[1])
        #create the new filename pattern
        base = base + alphadict[num]
        new = '{} {}'.format(base,name)
        os.rename(file,new)

def main():
    #build the number to alpha dictionary to be used in the file rename script
    alphanum = []
    alpha = []
    for i in range(1,27):
        alphanum.append(i)
    for i in string.ascii_lowercase:
        alpha.append(i)
    alphadict = dict(zip(alphanum, alpha))
    #gather a list of files in the current directory
    files = os.listdir('.')
    #strip out the python files from the list
    new_files = [file for file in files if '.py' not in file]
    #rename the files
    file_rename(new_files, alphadict)

if __name__ == main():
    main()