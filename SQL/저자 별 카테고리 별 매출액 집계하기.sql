select
    A.AUTHOR_ID,
    A.AUTHOR_NAME,
    B.CATEGORY,
    sum(B.PRICE * BS.SS) as TOTAL_SALES
from BOOK B
join AUTHOR A on A.AUTHOR_ID = B.AUTHOR_ID
join (
    select
        BOOK_ID,
        sum(SALES) as SS
    from BOOK_SALES
    where date_format(SALES_DATE, '%Y-%m') = '2022-01'
    group by BOOK_ID
) BS on BS.BOOK_ID = B.BOOK_ID
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID, CATEGORY desc;