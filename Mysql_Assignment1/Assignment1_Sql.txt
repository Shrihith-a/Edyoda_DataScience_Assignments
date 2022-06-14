-- Database Sales creation
CREATE DATABASE SALES_EMP;
SHOW DATABASES;
USE SALES_EMP;
create table salespeople(
Snum int primary key,
Sname varchar(50) unique,
City varchar(50),
Comm decimal(3,2)
);
select * from salespeople;
insert into salespeople values
(1001, 'Peel', 'London', .12),
(1002, 'Serres', 'Sanjose', .13),
(1004, 'Motika', 'London', .11),
(1007, 'Rifkin', 'Barcelona', .15),
(1003, 'Axelrod', 'Newyork', .10);

create table customers(
Cnum int,
Cname varchar(50),
City varchar(50) not null,
Snum int,
primary key(Cnum),
foreign key(Snum) references salespeople(Snum));
-- Snum is foreign key constraint 
-- refers Snum column of SalesPeople table.
select * from customers;
insert into customers values
(2001, 'Hoffman', 'London', 1001),
(2002,  'Giovanni', 'Rome', 1003),
(2003,  'Liu', 'Sanjose', 1002),
(2004,  'Grass', 'Berlin', 1002),
(2006, 'Clemens', 'London', '1001'),
(2008, 'Cisneros', 'Sanjose', 1007),
(2007, 'Pereira', 'Rome', 1004);

create table orders(
Onum int,
Amt decimal(7,2),
Odate date,
Cnum int,
Snum int,
primary key(Onum),
foreign key(Cnum) references customers(Cnum),
foreign key(Snum) references salespeople(Snum)
);
select * from orders;
insert into orders values(3001, 18.69, '1990-10-03', 2008, 1007);
insert into orders values(3003, 767.19, '1990-10-03', 2001, 1001);
insert into orders values(3002, 1900.10, '1990-10-03', 2007, 1004);
insert into orders values(3005,  5160.45, '1990-10-03', 2003, 1002);
insert into orders values(3006,  1098.16, '1990-10-03', 2008, 1007);
insert into orders values(3009, 1713.23, '1990-10-04', 2002, 1003);
insert into orders values(3007,  75.75, '1990-10-04', 2004, 1002);
insert into orders values(3008,  4273.00, '1990-10-05', 2006, 1001);
insert into orders values(3010, 1309.95, '1990-10-06', 2004, 1002);
insert into orders values(3011,  9891.88, '1990-10-06', 2006, 1001);

