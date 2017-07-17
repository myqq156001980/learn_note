# ulimit -n 設置文件句柄數
/etc/security/limits.conf 添加

www - nofile 1006154

www 是一个用户，如果是想所有用户生效的话换成 * ，设置的数值与硬件配置有关，别设置太大了。

    * soft nofile 65536

    * hard nofile 65536

> 詳細請查看 man limits.conf

-----
