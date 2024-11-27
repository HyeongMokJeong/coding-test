SELECT
    a.mcdp_cd AS '진료과 코드',
    COUNT(*) AS '5월예약건수'
FROM appointment a
WHERE DATE_FORMAT(a.apnt_ymd, '%Y-%m') = '2022-05'
GROUP BY a.mcdp_cd
ORDER BY COUNT(*), a.mcdp_cd;