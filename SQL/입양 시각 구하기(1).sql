select
    # hour() : 시간을 알려준다 (0 ~ 23)
    hour(DATETIME) as HOUR,
    count(1) as COUNT
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 20
group by HOUR
order by HOUR;