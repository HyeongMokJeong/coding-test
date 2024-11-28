select
    AI.NAME,
    AI.DATETIME
from ANIMAL_INS AI left join ANIMAL_OUTS AO on AI.ANIMAL_ID = AO.ANIMAL_ID
where AO.ANIMAL_ID is null
order by AI.DATETIME
limit 3;