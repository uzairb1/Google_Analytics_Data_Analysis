select 
distinct(extract(Month from a.subscription_start_date)) as Month ,
count(a.marketing_channel)*20 - b.monthly_total_spend as Profit, 
a.marketing_channel as Channel 
from `my-project-1535534415901.formel_Uzi.formel_subscriptions` a, 
`my-project-1535534415901.formel_Uzi.formel_marketing` b 
where a.marketing_channel=b.marketing_channel 
and extract(Year from a.subscription_start_date) = 2021
group by a.marketing_channel, b.monthly_total_spend, Month, a.ask_your_doctor_count 
order by Month