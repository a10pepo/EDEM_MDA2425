#!/bin/bash
ls bin

ls tmp

ls etc | grep "^t"

ls dev | grep "^tty"

ls dev | grep "^tty.*3$"

ls dev | grep "^t.*C1"

ls -a 

ls etc | grep -v "^t"

ls -r usr

cd tmp | mkdir PRUEBA

ls tmp

date

cd home

pwd

ls -l home

rm -r tmp/PRUEBA/*

mkdir PRUEBA/dir1 PRUEBA/dir2 PRUEBA/dir3
mkdir PRUEBA/dir3/dir31
mkdir PRUEBA/dir3/dir31/311 PRUEBA/dir3/dir31/312

cp -r /etc/motd /tmp/PRUEBA/mensaje

cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1/ && cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2/ && cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3/

ls tmp/PRUEBA/dir1/ tmp/PRUEBA/dir2/ tmp/PRUEBA/dir3/