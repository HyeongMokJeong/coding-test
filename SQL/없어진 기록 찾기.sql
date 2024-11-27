select 
    AO.ANIMAL_ID,
    AO.NAME
from ANIMAL_OUTS AO left join ANIMAL_INS AI ON AO.ANIMAL_ID = AI.ANIMAL_ID
where AI.ANIMAL_ID is null
order by AO.ANIMAL_ID;