SELECT 
    a.animal_type,
    COUNT(*) AS count
FROM animal_ins a
GROUP BY a.animal_type
ORDER BY a.animal_type;