select ROUND((count(subscription_id)*20-(select sum(monthly_total_spend)from `my-project-1535534415901.formel_Uzi.formel_marketing`))
/(select sum(monthly_total_spend) from `my-project-1535534415901.formel_Uzi.formel_marketing`),3)*100 as ROI, 
count(subscription_id)*20 as Revenue,
(select sum(monthly_total_spend) from `my-project-1535534415901.formel_Uzi.formel_marketing`) as Cost,
CONCAT(extract(Year from subscription_start_date),'-',extract(Month from subscription_start_date)) as Year_Month,
from `my-project-1535534415901.formel_Uzi.Subscriptions`
group by Year_Month
order by Year_Month