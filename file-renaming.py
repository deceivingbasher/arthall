#!/usr/bin/python3
from sys import argv,exit
from re import search
from os import rename, listdir, chdir

class InvalidNumber(Exception):
    "Raised when a file has a number greater than 26"
    pass

def file_rename(files, path):
    chdir(path)
    for file in files:
        try:
            if search("^[0-9]{3}\s[a-zA-Z]*_[0-9]{1,2}",file) != None:
                file1 = file.split(' ')
                #get the base file name
                base = file1[0]
                #get the name and number that will be used
                name = file1[1].split('_')[0]
                num = int(file1[1].split('_')[1].split('.')[0])
                ext = file1[1].split('_')[1].split('.')[1]
                #create the new filename pattern
                if num < 1 or num > 26:
                    raise InvalidNumber
                new = '{}{} {}.{}'.format(base,chr(num + 96),name,ext)
                print('Renaming file from {} to {}'.format(file,new))
                #rename the file
                rename(file,new)
            elif search("^[0-9]{3}\s[0-9]{3}\-[0-9]{3}\s[a-zA-Z]*_[0-9]{1,2}",file) != None:
                file1 = file.split(' ')
                #get the base file name
                base = file1[0]
                #store the middle part for later use
                middle = file1[1]
                #get the name and number that will be used
                name = file1[2].split('_')[0]
                num = int(file1[2].split('_')[1].split('.')[0])
                ext = file1[2].split('_')[1].split('.')[1]
                #create the new filename pattern
                if num < 1 or num > 26:
                    raise InvalidNumber
                new = '{}{} {} {}.{}'.format(base,chr(num + 96),middle,name,ext)
                print('Renaming file from {} to {}'.format(file,new))
                #rename the file
                rename(file,new)
            elif search("^[0-9]{3}\s[0-9]{3}\s[a-zA-Z]*_[0-9]{1,2}",file) != None:
                file1 = file.split(' ')
                #get the base file name
                base = file1[0]
                #store the middle part for later use
                middle = file1[1]
                #get the name and number that will be used
                name = file1[2].split('_')[0]
                num = int(file1[2].split('_')[1].split('.')[0])
                ext = file1[2].split('_')[1].split('.')[1]
                #create the new filename pattern
                if num < 1 or num > 26:
                    raise InvalidNumber
                new = '{}{} {} {}.{}'.format(base,chr(num + 96),middle,name,ext)
                print('Renaming file from {} to {}'.format(file,new))
                #rename the file
                rename(file,new)
        except IndexError:
            print('Invalid File Format detected')
            continue
        except InvalidNumber:
            print("This file name, {}, has a number that returns a non-alpha character during conversion".format(file))
        except:
            print('Unknown error on {}'.format(file))
            continue

def main():
    if len(argv) == 1:
        argv.append('.')
    elif argv[1] == '-h':
        print('Usage: file-renaming <path to directory>')
        print('*If no file path is specified, the script will run on the current directory*')
        exit(0)
    #gather a list of files in the current directory
    files = listdir(argv[1])
    #strip out the python files from the list
    new_files = [file for file in files if '.py' not in file]
    #rename the files
    file_rename(new_files, argv[1])

if __name__ == main():
    main()