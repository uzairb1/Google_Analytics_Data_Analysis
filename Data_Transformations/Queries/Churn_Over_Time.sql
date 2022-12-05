select (sum(t2.Unsubscribed)/sum(t1.Subscribed)) as Churn, 
t1.Month as Month,
t1.Year as Year
from 
(
 select count(subscription_id) as Subscribed, 
(extract(Month from subscription_start_date)) as Month , 
(extract(Year from subscription_start_date)) as Year 
from `my-project-1535534415901.formel_Uzi.Subscriptions`  
group by Year,Month
order by Month
) 
t1,
(
  select count(subscription_id) as Unsubscribed, 
(extract(Month from subscription_end_date)) as Month, 
(extract(Year from subscription_end_date)) as Year 
from `my-project-1535534415901.formel_Uzi.Subscriptions`
group by Year,Month
order by Month
) 
t2
where t2.Month = t1.Month
and t1.Year = t2.Year
group by t1.Month, t1.Year
order by t1.Month, t1.Year