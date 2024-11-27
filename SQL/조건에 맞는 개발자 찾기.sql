SELECT DISTINCT
    d.id,
    d.email,
    d.first_name,
    d.last_name
FROM developers d
JOIN skillcodes s ON (d.skill_code & s.code) > 0
WHERE s.name IN ('Python', 'C#')
ORDER BY d.id;