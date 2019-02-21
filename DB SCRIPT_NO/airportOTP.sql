create table  airport_tbl ( 
                          uuid INT NOT NULL AUTO_INCREMENT, 
                          name VARCHAR(100), otp INT(100), 
                          operations VARCHAR(100), 
                          country VARCHAR(100), 
                          subregion VARCHAR(100), 
                          starrating VARCHAR(30), 
                          PRIMARY KEY(uuid))ENGINE=InnoDB DEFAULT CHARSET=utf8;
