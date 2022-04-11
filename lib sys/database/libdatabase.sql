create database lib;

use lib;


create table info
(
namee varchar(25),
libID varchar(25)primary key,
pswd varchar(25),
Phone_no varchar(25),
email_id varchar(25),
employee_id varchar(25) 
);

drop table info;

SELECT * FROM lib.info;
