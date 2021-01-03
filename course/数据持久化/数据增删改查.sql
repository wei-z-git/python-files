-- -- 完整语法
-- select distinct 字段1，字段2，...   from 库名字.表名字   
- -
where
    约束条件 找id > 3 --         group by 分组依据 1万条结果，分类，员工按部门分类
    --         having 过滤条件 可以去重复例子？
    --         order by 排序的字段 
    --         limit 限制显示的条数
    --         ;
SELECT
    t1.id,
    t1.name,
    t1.post,
    t1.hire_date,
    t2.*
FROM
    emp as t1
    inner JOIN (
        select
            post,
            max(hire_date) as max_date
        FROM
            emp
        GROUP BY
            post
    ) as t2 on t1.post = t2.post
    where t1.hire_date = t2.max_date