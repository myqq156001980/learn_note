# 分割文件

  #!/bin/bash

  dir=split-dir


  if [ -d $dir ]
  then
    rm -rf $dir
  fi
  mkdir $dir

  x_count=0
  for i in `ls | grep part`
  do
    echo $i
    size=`ls -l -h $i | awk '{print $5}'`
    lines=`wc -l $i | awk '{print $1}'`
    l=${#size}
    (( l-- ))
    size_num=${size:0:$l}
    percent=`echo "scale=2;100/$size_num" | bc`
    split_lines=`echo "scale=2;$lines*$percent" | bc`
    split_lines=`echo $split_lines | awk '{print int($1+0.99)}'`


    split -l $split_lines $i

    for j in `ls | grep xa`
    do
      mv $j $dir/$x_count
      (( x_count++ ))
    done
  done
  
  
  ----
