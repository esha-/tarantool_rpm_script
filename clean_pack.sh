#!/bin/bash
#The script cleans the folder from older version tarantool rpm packages
#set -x
function tarantool_version ()
{
    local file_name=$1
    local file_name=${file_name%.*.rpm}
    local file_version_full=${file_name#*-}
    tarantool_version=${file_version_full%.*}
}

function packages_number ()
{
    local file_name=$1
    local file_name=${file_name%.*.rpm}
    local file_version_full=${file_name#*-}
    local packages_number=${file_version_full##*-}
    return $packages_number
}

folder_name=$1

if [[ "$folder_name" == "" ]]; then
    echo "error: the folder name is not specified"
    exit -1
fi

for file in $( ls $folder_name )
    do  
        echo $file
    done

tarantool_version $file

last_version=$tarantool_version
echo $last_version

packages_number $file
last_number=$(($?-10))
echo $last_number

for file in $( ls $folder_name )
    do
        tarantool_version $file
        file_tarantool_version=$tarantool_version
        packages_number $file
        file_number=$?
        echo $file_number
        if [[ "$file_tarantool_version" == "$last_version" ]]; then
            if [[ "$file_number" -lt "$last_number" ]]; then
                echo "rm -rf $folder_name/$file"
                rm -rf $folder_name/$file
            fi
        fi
    done







