#! /usr/bin/python2.7
# The script cleans the folder from older version tarantool rpm packages
import argparse
import os
import sys
import re

# Function for definition tarantool version in rpm package
def tarantool_version (file_name):
    parts = file_name.split('-')
    for part in parts:
        if re.match('[0-9].[0-9].*', part):
            version = part
            break
    return version

# Function for definition number of rmp package
def packages_number (file_name):
    parts = file_name.split('-')
    n = len(parts)
    part = parts[n - 1]
    parts = part.split('.')
    number = parts[0]
    return number

# Program body
def main():
    try:
        folder_directory=sys.argv[1]
    except IndexError:
        print ('error: the folder directory is not specified')
    files = os.listdir(folder_directory)
    files = filter(lambda x: x.endswith('.rpm'), files)
    print (files)
    name = files[0]
    print (name)
"""# Create dist version_number - file     
    vf = {}
    for f in files:
        vf[tarantool_version(f) + '-' + packages_number(f)] = f
    vers_list = vf.keys()
    vers_list = list(vers_list)
    vers_list.sort(reverse = True)
    print(vers_list)
    last_version_parts = vers_list[0].split('-')
    last_version = last_version_parts[0]
    last_number = last_version_parts[1]
    print ('last_version ' + last_version)
    print ('last_number ' + last_number)
    cur_version = 0
    cur_number = 0
    for v in vers_list:
        print v
        parts = v.split('-')
        version = parts[0]
        number = parts[1]
        print version
        print number
        if version == last_version :
            if int(number) <= int(last_number) - 10:
                os.remove(folder_directory + '/' + vf[v])
                print ('remove '+ folder_directory + '/' + vf[v]) 
        else:
            if version == cur_version :
                if int(number) <= int(cur_number):
                    os.remove(folder_directory + '/' + vf[v])
                    print ('remove '+ folder_directory + '/' + vf[v])
                else:
                    cur_number = number
            else:
                cur_version = version
                cur_number = number
"""
if __name__=="__main__":
    main()
