select
    month(START_DATE) as MONTH,
    CAR_ID,
    count(1) as RECORES
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
    group by CAR_ID
    having count(1) >= 5
) and date_format(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc;