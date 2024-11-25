SELECT 
    member_id, 
    member_name, 
    gender, 
    DATE_FORMAT(date_of_birth, '%Y-%m-%d') date_of_birth
FROM member_profile
WHERE 
    DATE_FORMAT(date_of_birth, '%m') = 3 
    AND gender = 'W' 
    AND tlno is not null
ORDER BY member_id;