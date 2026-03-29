USE demodb

CREATE TABLE customers
(
    ID INT AUTO_INCREMENT primary key,
    Name varchar(20) not null,
    city varchar(20) not null
)