#!/bin/bash
IFS=$'\n'
for file in $(ls $1 | grep -vE ".py|.sh");
do 
    #get the base
    base=$(echo $file | cut -d ' ' -f 1)
    #get the name
    name=$(echo $file | cut -d ' ' -f 2 | cut -d '_' -f 1)
    #get the numerical number for letter conversion
    num=$(echo $file  | cut -d '_' -f 2)
    letter=$(printf "\\$(printf "%03o" $((num + 96)))")
    oldname=$(echo $base $name'_'$num)
    newname=$(echo $base$letter $name)
    echo 'Renaming file from' $oldname 'to' $newname'.'
    mv $1/$oldname $1/$newname
done