  HOST gitlab
      HostName 114.242.245.101
      User root
      Port 5023
      IdentityFile ~/.ssh/id_rsa
      ServerAliveInterval 60


  HOST api
      HostName 114.242.245.101
      User root
      Port 5024
      IdentityFile ~/.ssh/id_rsa
      ServerAliveInterval 60

  HOST az
      HostName liferay3171.chinacloudapp.cn
      User sunzqc
      Port 22
      IdentityFile ~/.ssh/id_rsa
      ServerAliveInterval 60
