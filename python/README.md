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
