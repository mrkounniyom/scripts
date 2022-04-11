#!/usr/bin/env bash

## backup dir format ##
backup_dir=$(date +'%m-%d-%Y')
filename=${backup_dir}'-conf.b.zip'
#echo $filename

echo "> Backing up .config"

#zip -r --exclude=*backups* --exclude=*/.* /var/www/backups/site/$(date +\%Y-\%m-\%d-\%H-\%M).zip /var/www

zip -r --exclude=*BraveSoftware* --exclude=*Bitwarden* ~/.backconf/$filename ~/.config/*
