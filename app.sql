create database Form;
use Form;
create table form(id int primary key auto_increment, fname varchar (50),lname varchar (50),birthday date,gender ENUM('Male','Female'),email varchar (50),phone varchar (12),subjects varchar (50));
desc Form;
select * from form;
desc form;