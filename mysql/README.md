# mysql innodb 外键级联删除  
  
  CREATE TABLE fc1 (
      i INT PRIMARY KEY,
      j INT
  ) ENGINE = InnoDB;

  CREATE TABLE fc2 (
      m INT PRIMARY KEY,
      n INT,
      FOREIGN KEY ni (n) REFERENCES fc1 (i)
          <font color=#FF0000 size=7 face="黑体">ON DELETE CASCADE</font>
  ) ENGINE = InnoDB;
  
  
  ---
