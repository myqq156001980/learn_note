# 分割文件    

    #!/bin/bash

    dir=split-dir
    split_size=100


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
        percent=`echo "scale=2;$split_size/$size_num" | bc`
        split_lines=`echo "scale=2;$lines*$percent" | bc`
        split_lines=`echo $split_lines | awk '{print int($1+0.99)}'`


        split -l $split_lines $i

        for j in `ls | grep xa`
        do
            mv $j $dir/$x_count
            (( x_count++ ))
        done
    done


---

# 上传文件
    #!/bin/bash

    id=$1
    start=$2
    end=$3

    output=output



    for ((i=$start; i<=$end; i++))
    do
        curl_cmd="curl -F 'fileToUpload=@${i}' http://10.26.6.6:8444/api/uploadFile\?id\=$id\&type\=2 -o $output"
        str_len=${#curl_cmd}
        eval printf "%.s\*" {1..$str_len}
        echo "\n"
        echo "$curl_cmd"
        eval "$curl_cmd"
        echo "\n"
        cat $output
        echo "\n"
        eval printf "%.s\*" {1..$str_len}
        echo "\n"
    done 

---

        
