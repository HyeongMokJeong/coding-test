select
    FH.FLAVOR
from FIRST_HALF FH
join (
    select
        FLAVOR,
        sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
) J on FH.FLAVOR = J.FLAVOR
order by (FH.TOTAL_ORDER + J.TOTAL_ORDER) desc
limit 3;