# mysql innodb 外键级联删除  
  
    CREATE TABLE fc1 (
        i INT PRIMARY KEY,
        j INT
    ) ENGINE = InnoDB;

    CREATE TABLE fc2 (
        m INT PRIMARY KEY,
        n INT,
        FOREIGN KEY ni (n) REFERENCES fc1 (i)
            ON DELETE CASCADE
    ) ENGINE = InnoDB;
  
  
 > 当删除fc1表中的数据，会自动删除对应fc2中外键关联的记录 
  ---
