# Linux 文件夹转跳

    export MARKPATH=$HOME/.marks
    function jump {
    	cd -P "$MARKPATH/$1" 2>/dev/null || echo "No such mark: $1"
    }
    function mark {
    	mkdir -p "$MARKPATH/" ; ln -s "$(pwd)" "$MARKPATH/$1"
    }
    function unmark {
    	rm -i "$MARKPATH/$1"
    }
    function marks {
    	ls -l "$MARKPATH" | awk '{if (NR != 1) { printf "%s\t->\t%s\n", $9,$11}}'
    }
    alias j=jump
    alias m=mark
    alias um=unmark
    alias ms=marks
    alias la=ls -la

 - mark将一个目录加入常用仓库,加参数可以指定名字,如果不加参数则默认为当前目录名字
 - marks显示仓库内的目录
 - unmark移除不需要的目录
 - jump跳转到指定的目录

----------

# ubuntu 安装chrom和搜狗
## 搜狗输入法
1. sudo apt-get install fcitx -y
2. sudo apt-get install -f
> 解决安装包的依赖 -f --- --fix-broken
3. sudo dpkg -i sougou.deb
> 去官网下载安装包

## chrome
1. sudo dpkg -i chrome.deb
> 官网安装包
2. sudo apt-get install -f
> 如安装有问题执行
3. 再次执行第一步
---
# 安装0h-my-zsh   zsh-syntax-highlighting

	sudo apt install zsh -y
	sudo apt install git -y
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
	sed -i 's/ZSH_THEME=".*"/ZSH_THEME="cloud"/g' ~/.zshrc
	git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh-syntax-highlighting
	echo "source ${(q-)PWD}/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
	cat config >> ~/.zshrc
	source ~/.zshrc

---

