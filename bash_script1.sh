#!/bin/bash

cd /mnt/local/files/articles
path=`ls | wc -l`
if [[ $path -eq 3 ]]
then
gzip /mnt/local/files/articles/articles*
mv /mnt/local/files/articles/articles* /mnt/local/backups/articles
echo "File saved. 3 files were moved to /mnt/local/backups/articles"
else
echo "File saved"
fi

psql -h localhost -U db_admin -d db_admin -c "SELECT * FROM articles" > /mnt/local/files/articles/articles-$(date +%Y-%m-%d-%H-%M-%S)