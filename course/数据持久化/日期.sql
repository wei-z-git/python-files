CREATE TABLE student(
id int,
name char(16),
born_year YEAR,
birth_data date,
class_time time,
reg_time datetime
)
;
INSERT into student VALUES
(3, 'egon', now(), now(), now(), now())
;
INSERT into student VALUES
(4, 'ego1n', '1999', now(), now(), now())
;



CREATE TABLE employee(
    id int,
    name char(10),
    sex enum('male','female','other')
);

INSERT into employee VALUES
(1,'egon','male');