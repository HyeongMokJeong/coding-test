select
    I.ANIMAL_ID,
    I.ANIMAL_TYPE,
    I.NAME
from ANIMAL_INS I
join ANIMAL_OUTS O on O.ANIMAL_ID = I.ANIMAL_ID
where I.SEX_UPON_INTAKE like 'Intact%'
    and O.SEX_UPON_OUTCOME not like 'Intact%'
order by ANIMAL_ID;