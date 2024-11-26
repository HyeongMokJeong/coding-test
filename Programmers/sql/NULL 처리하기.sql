SELECT 
    ai.animal_type,
    IFNULL(ai.name, 'No name'),
    ai.sex_upon_intake
FROM animal_ins ai
ORDER BY ai.animal_id;