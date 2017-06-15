# mysql 二进制包安装

```
shell
>
 groupadd mysql
shell
>
 useradd -r -g mysql -s /bin/false mysql
shell
>
 cd /usr/local
shell
>
 tar zxvf /path/to/mysql-VERSION-OS.tar.gz
shell
>
 ln -s full-path-to-mysql-VERSION-OS mysql
shell
>
 cd mysql
shell
>
 mkdir mysql-files
shell
>
 chmod 750 mysql-files
shell
>
 chown -R mysql .
shell
>
 chgrp -R mysql .
shell
>
 bin/mysql_install_db --user=mysql    # MySQL 5.7.5
shell
>
 bin/mysqld --initialize --user=mysql # MySQL 5.7.6 and up
shell
>
 bin/mysql_ssl_rsa_setup              # MySQL 5.7.6 and up
shell
>
 chown -R root .
shell
>
 chown -R mysql data mysql-files
shell
>
 bin/mysqld_safe --user=mysql 
&

# Next command is optional
shell
>
 cp support-files/mysql.server /etc/init.d/mysql.server
```

> 当执行 bin/mysqld --initialize --user=mysql 出错提示缺少包 libaio.so.1 时 执行 sudo apt install libaio-dev 上面操作会生成随机密码，用此密码登录后修改root密码

```
set password for root@localhost = password('123');
```



