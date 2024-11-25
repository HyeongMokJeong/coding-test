SELECT 
    c.car_type,
    COUNT(*) AS CARS
FROM car_rental_company_car c
WHERE 
    c.options LIKE '%통풍시트%' 
    OR c.options LIKE '%열선시트%'
    OR c.options LIKE '%가죽시트%'
GROUP BY c.car_type
ORDER BY c.car_type;