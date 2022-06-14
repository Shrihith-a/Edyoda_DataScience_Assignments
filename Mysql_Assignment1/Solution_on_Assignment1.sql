-- 1. Count the number of Salesperson whose name begin with ‘a’/’A’
select * from salespeople;
use sales_emp;

select Snum,Sname from salespeople
where Sname like 'A%'; 

-- 2. Display all the Salesperson whose all orders 
-- worth is more than Rs. 2000.
select * from orders;
select Onum,Amt from orders where Amt >= 2000 
order by Amt desc, Onum; 

-- 3. Count the number of Salesperson belonging to Newyork
select * from salespeople;
select count(*)
from salespeople
where city = 'Newyork';

-- 4. Display the number of Salespeople
--    belonging to London and belonging to Paris.
select Snum, City from salespeople where city = 'London';
select Snum, City from salespeople where city = 'Paris';

-- 5. Display the number of orders taken by each Salesperson 
-- and their date of orders.

select * from orders;
select Onum,Snum,Odate from orders 

