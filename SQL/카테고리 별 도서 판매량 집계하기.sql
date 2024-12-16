select
    B.CATEGORY,
    sum(BS.SALES) as TOTAL_SALES
from BOOK B
join BOOK_SALES BS on BS.BOOK_ID = B.BOOK_ID
where date_format(BS.SALES_DATE, '%Y-%m') = '2022-01'
group by B.CATEGORY
order by B.CATEGORY;