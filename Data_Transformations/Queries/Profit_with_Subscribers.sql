select (sum(t1.Subscribed)*20)-(sum(t2.Unsubscribed)*20) as Profit, 
CONCAT(t1.Year,'-', t1.Month) as Year_Month
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
group by Year_Month, t1.Subscribed, t2.Unsubscribed
order by Year_Month