DROP TABLE IF EXISTS email_schedule;

create table email_schedule
(
	id int,
	subject varchar(100) not null,
	body text,
	status int,
	scheduled_at timestamp not null
);

create table email_recipient
(
	id int,
	email_address varchar(50)
);