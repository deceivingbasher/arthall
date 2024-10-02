#!/usr/bin/python3
from sys import argv,exit
from os import rename, listdir, chdir

class InvalidNumber(Exception):
    "Raised when a file has a number greater than 26"
    pass

def file_rename(files, path):
    chdir(path)
    for file in files:
        try:
            first = file[:3].strip(' ')
            last = int(file.split('_')[1].split('.')[0].strip(' '))
            ext = file.split('_')[1].split('.')[1].strip(' ')
            base = file.split('_')[0].split(' ')
            if last < 1 or last > 26:
                raise InvalidNumber
            base[0] = first + chr(last + 96)
            new_file = ' '.join(base) + '.' + ext
            print('File is being renamed from {} to {}'.format(file,new_file))
            rename(file,new_file)
        except IndexError:
            print('Invalid File Format detected in {}'.format(file))
            continue
        except InvalidNumber:
            print("This file name, {}, has a number that returns a non-alpha character during conversion".format(file))
        except:
            print('Unknown error on {}'.format(file ))
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
    new_files = [file for file in files if '.wav' in file]
    #rename the files
    file_rename(new_files, argv[1])

if __name__ == main():
    main()