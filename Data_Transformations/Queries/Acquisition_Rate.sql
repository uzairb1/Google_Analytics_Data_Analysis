select distinct(CONCAT(a.Year,'-', a.Month)) as Year_Month, a.User_Count from
(SELECT extract(Month from user_created_date) as Month,
       SUM(COUNT(*)) OVER (ORDER BY extract(Month from user_created_date)) as User_Count,
       extract(Year from user_created_date) as Year
FROM `my-project-1535534415901.formel_Uzi.Users`
GROUP BY user_created_date
ORDER BY Year,Month) a