#! /usr/bin/python2.7
# The script cleans the folder from older version tarantool rpm packages
import argparse
import os
import sys
import re

# Function for definition tarantool version in rpm package and its number as integer
def tarantool_version (file_name):
    version  = re.search('[0-9].[0-9].*-[0-9]*', file_name)
    version = version.group(0)
    version = version.replace('.','') 
    parts = version.split('-')
    version = int(parts[0]) * 10000
    vnumber = int(parts[1])
    version = version + vnumber
    return version

###############################################################
# Program body
###############################################################

def main():

    try:
        folder_directory=sys.argv[1]
    except IndexError:
        print ('error: the folder directory is not specified')
    files = os.listdir(folder_directory)
    files = filter(lambda x: x.endswith('.rpm'), files)

# Create dist version_number - file     
    vf = {}
    temp = 0
    i = 0
    for f in files:
        version = tarantool_version(f)
        if version in vf:
            i += 0.001
            version += i
        else:
            i = 0
        vf[version] = f
    vers_list = vf.keys()
    vers_list = list(vers_list)
    vers_list.sort(reverse = True)
# Last version tarantool rpm package    
    last_version = vers_list[0]//10000
    last_number = vers_list[0]%10000

    cur_version = 0
    cur_number = 0

# Leave the 10 packages last version and 1 packages early versions
    for v in vers_list:
        version = int(v//10000)
        number = int(v%10000)
        if version == last_version :
            if number < last_number - 10:
                os.remove(folder_directory + '/' + vf[v])
                print ('remove '+ folder_directory + '/' + vf[v]) 
        else:
            if version == cur_version :
                if number < cur_number:
                    os.remove(folder_directory + '/' + vf[v])
                    print ('remove '+ folder_directory + '/' + vf[v])
                else:
                    cur_number = number
            else:
                cur_version = version
                cur_number = number

if __name__=="__main__":
    main()
