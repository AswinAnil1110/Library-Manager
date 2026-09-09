create database library_db;
use library_db;
create table book (id int auto_increment primary key,
title varchar(100),
author varchar(100),
category varchar(100),
price int,
published_date date);
select * from book;