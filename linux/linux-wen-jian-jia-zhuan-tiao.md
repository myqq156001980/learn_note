# Linux 文件夹转跳

```
export MARKPATH=$HOME/.marks
function jump {
    cd -P "$MARKPATH/$1" 2
>
/dev/null || echo "No such mark: $1"
}
function mark {
    mkdir -p "$MARKPATH/" ; ln -s "$(pwd)" "$MARKPATH/$1"
}
function unmark {
    rm -i "$MARKPATH/$1"
}
function marks {
    ls -l "$MARKPATH" | awk '{if (NR != 1) { printf "%s\t-
>
\t%s\n", $9,$11}}'
}
alias j=jump
alias m=mark
alias um=unmark
alias ms=marks
alias la=ls -la
```

* mark将一个目录加入常用仓库,加参数可以指定名字,如果不加参数则默认为当前目录名字
* marks显示仓库内的目录
* unmark移除不需要的目录
* jump跳转到指定的目录



