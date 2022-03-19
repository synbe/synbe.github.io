@echo off

echo 此脚本：当前目录下运行cmd

::set window
title start.....
color 2f
echo Start.....

::change-to-Current-path
cd  %~dp0  
echo Current_Path:%cd%
cmd