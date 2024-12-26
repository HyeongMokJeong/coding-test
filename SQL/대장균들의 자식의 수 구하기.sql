select
    ID,
    ifnull(T.C, 0) as CHILD_COUNT
from ECOLI_DATA
left join (
    select
        PARENT_ID,
        count(1) as C
    from ECOLI_DATA
    group by PARENT_ID
) T on ID = T.PARENT_ID
order by ID;
