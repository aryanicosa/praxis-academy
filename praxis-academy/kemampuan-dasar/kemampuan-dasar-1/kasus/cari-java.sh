#!/bin/bash
dir=$1;
cd $dir
if [ -e *.java ]; then
echo "Ada file Java pada direktori $dir"
else
echo "Tidak ditemukan file Java pada direktori $dir"
fi
