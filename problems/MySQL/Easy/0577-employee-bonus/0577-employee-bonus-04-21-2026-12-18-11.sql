# Write your MySQL query statement below
Select employee.name,bonus
from employee left join bonus  on employee.empid= bonus.empid
where coalesce(bonus,0) <1000;