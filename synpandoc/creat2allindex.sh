#!/bin/bash  

cd blog
sh ./creat2indexb.sh

cd ../files
sh ./creat2indexf.sh

cd ../images
sh ./creat2indexm.sh

cd ../pages
sh ./creat2indexp.sh

cd ../slides
sh ./creat2indexs.sh

cd ../tools
sh ./creat2indext.sh