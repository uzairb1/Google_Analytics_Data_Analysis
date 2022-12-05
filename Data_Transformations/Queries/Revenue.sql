select count(subscription_id)*20 as Revenue, 
CONCAT(extract(Year from subscription_start_date),'-',extract(Month from subscription_start_date)) as Year_Month
from `my-project-1535534415901.formel_Uzi.Subscriptions`
group by Year_Month
order by Year_Month