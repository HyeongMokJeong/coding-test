select *
from (
    select
        C.CAR_ID,
        C.CAR_TYPE,
        round(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) * 0.01) AS FEE
    from 
        CAR_RENTAL_COMPANY_CAR C
    join 
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
        on P.CAR_TYPE = C.CAR_TYPE
        and P.DURATION_TYPE = '30일 이상'
    where C.CAR_TYPE in ('세단', 'SUV')
        and C.CAR_ID not in (
            select CAR_ID
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where END_DATE > '2022-11-01' and START_DATE < '2022-12-01'
        )
) T
where FEE >= 500000 and FEE < 2000000
order by FEE desc, CAR_TYPE, CAR_ID desc;