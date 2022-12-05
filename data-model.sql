CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.Checkin-In` ( 
	user_id              STRING    NOT NULL  ,
	checkin_date         DATE      
 );

CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.Marketing` ( 
	user_id              STRING    NOT NULL ,
	marketing_channel    STRING      
 );

CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.Users` ( 
	user_id              STRING    NOT NULL ,
	subscription_id      STRING      ,
	has_voucher          BOOLEAN      ,
	is_active            BOOLEAN      ,
	user_created_date    DATE      ,
	newsletter_subscription BOOLEAN      ,
	gender               STRING      ,
	age                  INT      
 );

CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.cancellations` ( 
	user_id              STRING      NOT NULL  ,
	cancellation_date    DATE      ,
	lead_time_in_hours   NUMERIC      
 );

CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.diagnosis` ( 
	user_id              STRING      NOT NULL  ,
	condition            STRING      ,
	severity             STRING      ,
	ask_your_doctor_count INT      ,
	gross_price          INT      
 );

CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.subscriptions` ( 
	subscription_id      STRING      ,
	purchase_date        DATE      ,
	subscription_start_date DATE      ,
	subscription_end_date DATE      ,
	user_id              STRING      NOT NULL  ,
	subscription_interval INT      ,
	lead_time_in_h       INT      
 );

CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.voucher` ( 
	user_id              STRING     NOT NULL   ,
	first_voucher_type   STRING      
 );
CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.formel_marketing` ( 
	marketing_channel              STRING   ,
	monthly_total_spend  INTEGER     
 );
CREATE TABLE IF NOT EXISTS `my-project-1535534415901.formel_Uzi.formel_subscriptions` ( 
	user_id STRING    ,
    subscription_id STRING ,
	first_voucher_type STRING,
	purchase_date DATE,
	subscription_start_date DATE,
	subscription_end_date DATE,
	subscription_interval DATE,
	cancellation_date DATE,
	lead_time_in_hours NUMERIC,
	gross_price NUMERIC,
	user_created_date DATE,
	newsletter_subscription BOOLEAN,
	gender STRING,
	age INTEGER,
	disgnosis_condition STRING,
	diagnosis_severity STRING,
	ask_your_doctor_count NUMERIC,
	checkin_date DATE,
	checkin_score NUMERIC,
	marketing_channel STRING
 );