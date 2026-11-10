#!/bin/bash
SRC=$1
DEST=$2
sudo tar czf $DEST $SRC
mysqldump -u root -pSup3rS3cret! shoplite > $DEST.sql
chmod 777 $DEST*
