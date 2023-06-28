create database univaliDB;

use univaliDB;

create table usuarios (
  id int not null auto_increment primary key,
  name varchar(100) not null,
  email varchar(100) not null
);

desc usuarios;

select * from usuarios;