select 
    M.MEMBER_NAME,
    R.REVIEW_TEXT,
    date_format(R.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE M
# REST_REVIEW와 조인한다.
# 이미 가장 count(*)가 큰 MEMBER_ID만을 대상으로 추렸다.
join (
    select 
        R.MEMBER_ID, 
        R.REVIEW_TEXT,
        R.REVIEW_DATE
    from REST_REVIEW R
    # count(*)가 가장 큰 member_id를 가진 테이블과 조인한다.
    # REST_REVIEW 테이블에서 count(*)가 가장 큰 MEMBER_ID만 조회
    join (
        select
            MEMBER_ID,
            count(*) as C
        from REST_REVIEW
        group by MEMBER_ID
        order by C desc limit 1
    ) CT on R.MEMBER_ID = CT.MEMBER_ID
) R on M.MEMBER_ID = R.MEMBER_ID
order by R.REVIEW_DATE, R.REVIEW_TEXT;