# Tools
1. supervisor 
> 进程管理工具


# 生成密码和token

    import secrets
    import string

     characters = string.ascii_letters + string.digits


     def get_password(size):
         security_password = ''.join(secrets.choice(characters) for i in range(size))
         return security_password

     bt = secrets.token_bytes(16)
     ht = secrets.token_hex(32)
     ut = secrets.token_urlsafe(32)
   
---
# python3 二进制包安装
1. 下载解压后进入目标文件夹  ./configure --prefix=/usr/local/python36
2. sudo apt install -y zlib1g-dev libssl-dev
> 安装相关的包，总是提示缺少

3. make
4. sudo make install
5. 建立软链接到/usr/bin目录

---

# python 启动http服务器
python -m http.server 8888 -b ip
> 默认8000端口 localhost地址

# python启动ftp服务器
1. 安装 pyftpdlib pip install pyftpdlib
2. python -m pyftpdlib 

---

    import optparse
    import os
    
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import ThreadedFTPServer
    
    
    def main():
        """Start a stand alone anonymous FTP server."""
        usage = "python -m pyftpdlib [options]"
        parser = optparse.OptionParser(usage=usage, description=main.__doc__)
        parser.add_option('-i', '--interface', default=None, metavar="ADDRESS",
                          help="specify the interface to run on (default all "
                               "interfaces)")
        parser.add_option('-p', '--port', type="int", default=2121, metavar="PORT",
                          help="specify port number to run on (default 2121)")
        parser.add_option('-w', '--write', action="store_true", default=False,
                          help="grants write access for the anonymous user "
                               "(default read-only)")
        parser.add_option('-d', '--directory', default=os.getcwd(), metavar="FOLDER",
                          help="specify the directory to share (default current "
                               "directory)")
    
        options, args = parser.parse_args()
    
        # Define a anonymous user having  r/w permissions or not
        perm = options.write and "elradfmwM" or "elr"
    
        # Instantiate a dummy authorizer for managing 'virtual' users
        authorizer = DummyAuthorizer()
    
        # Define a new user having full r/w permissions and a read-only
        # anonymous user
        authorizer.add_user('user', '12345', options.directory, perm='elradfmwM')
        authorizer.add_anonymous(options.directory, perm=perm)
    
        # Instantiate FTP handler class
        handler = FTPHandler
        handler.authorizer = authorizer
    
        # Define a customized banner (string returned when client connects)
        handler.banner = "Welcome to my FTP Server"
    
        # Specify a masquerade address and the range of ports to use for
        # passive connections.  Decomment in case you're behind a NAT.
        # handler.masquerade_address = '151.25.42.11'
        # handler.passive_ports = range(60000, 65535)
    
        # Instantiate FTP server class and listen on 0.0.0.0:2121
    
        address = (options.interface or '127.0.0.1', options.port or 2121)
        # server = FTPServer(address, handler)
        server = ThreadedFTPServer(address, handler)
    
        # set a limit for connections
        server.max_cons = 256
        server.max_cons_per_ip = 5
    
        # start ftp server
        server.serve_forever()
    
    
    if __name__ == '__main__':
        main()
       
---
    
# python ftp 上传下载
> python 自带的ftplib包实现了上传和下载详情参照api文档

---
    import optparse
    from ftplib import FTP
    
    
    def ftp_connect(host, port, username, password):
        ftp_server = FTP()
        ftp_server.connect(host, port)
        ftp_server.login(username, password)
        return ftp_server
    
    
    # 从ftp下载文件
    def download_file(ftp_server, remotepath, localpath):
        buf_size = 1024
        fp = open(localpath, 'wb')
        ftp_server.retrbinary('RETR ' + remotepath, fp.write, buf_size)
        ftp.set_debuglevel(0)
        fp.close()
    
    
    # 从本地上传文件到ftp
    def uploadfile(ftp_server, remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'rb')
        ftp_server.storbinary('STOR ' + remotepath, fp, bufsize)
        ftp_server.set_debuglevel(0)
        fp.close()
    
    
    def main():
        """Up or Download file from FTP server."""
        usage = "python -t upload or download -h host -p port -f filename"
        parser = optparse.OptionParser(usage=usage, description=main.__doc__)
        parser.add_option('-t', '--type', default=None, metavar="TYPE",
                          help="upload or download file")
        parser.add_option('-i', '--interface', default=None, metavar="INTERFACE",
                          help="specify the ftp host ")
        parser.add_option('-p', '--port', type="int", default=2121, metavar="PORT",
                          help="specify port number to run on (default 2121)")
        parser.add_option('-f', '--filename',
                          help="the filename you wanna upload or download")
        return parser
    
    
    if __name__ == "__main__":
        options, args = main().parse_args()
    
        ftp = ftp_connect(options.interface, options.port, "user", "12345")
        if options.type == "upload":
            uploadfile(ftp, "send/apitest111.sql", options.filename)
        else:
            download_file(ftp, options.filename, "E:/idea_workspace/py/ftp/sql.sql")
        ftp.quit()

---
    
    
  

