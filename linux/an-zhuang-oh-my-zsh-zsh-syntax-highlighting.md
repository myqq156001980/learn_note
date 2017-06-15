# 安装0h-my-zsh zsh-syntax-highlighting

```
sudo apt install zsh -y
sudo apt install git -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sed -i 's/ZSH_THEME=".*"/ZSH_THEME="cloud"/g' ~/.zshrc
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh-syntax-highlighting
echo "source ${(q-)PWD}/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" 
>
>
 ${ZDOTDIR:-$HOME}/.zshrc
cat config 
>
>
 ~/.zshrc
source ~/.zshrc
```



