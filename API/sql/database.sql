-- DROPS
drop table if exists Days;
drop table if exists Tasks;
drop table if exists Comments;
-- CREATES
create table Days (
    day_id serial,
    day_title varchar(50),
    day_info varchar(200),
    day_dayDate timestamp,
    primary key (day_id)
);

create table Tasks (
    task_id serial,
    task_title varchar(50),
    task_info varchar(200),
    day_id int references Days(day_id) on delete cascade on update cascade,
    primary key (task_id)
);

create table Comments (
    comment_id serial,
    comment_text varchar(200),
    task_id int references Tasks(task_id) on delete cascade on update cascade,
    primary key (comment_id)
);
-- TESTDATA
insert into Days (day_title, day_info, day_dayDate) values ('test day', '', '2019-03-18');
insert into Tasks (task_title, task_info, day_id) values ('test task', 'task for testing api', 1);

select task_id, task_title, task_info, day_title, day_info from tasks 
inner join days on tasks.day_id = days.day_id 
where to_char(days.day_daydate, 'YYYY') = '2018' and to_char(days.day_daydate, 'MM') = '03';
