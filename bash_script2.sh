#!/bin/bash

counter=0
echo $$ > $var/run/script.pid
while [ $counter -eq 0 ]
do
cd /mnt/local/backups/articles
path=`ls | wc -l`
path2=`ls | wc -c`
if [[ $path -ge 10 || $path2 -ge 750 ]]
then
echo "the number or size of files in the directory exceeds the allowed size. The number of files: $path, the size of file: $path2" | mail -s "files in backups" root@localhost
counter=$(( $counter +1 ))
sleep 1h
counter=0
fi
done

