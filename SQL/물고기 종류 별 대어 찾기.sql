select
    F.ID,
    FN.FISH_NAME,
    F.LENGTH
from FISH_INFO F 
    join FISH_NAME_INFO FN on F.FISH_TYPE = FN.FISH_TYPE
    join (
        select
            F.FISH_TYPE,
            max(F.LENGTH) as LENGTH
        from FISH_INFO F
        group by FISH_TYPE
    ) F2 on F.FISH_TYPE = F2.FISH_TYPE and F.LENGTH = F2.LENGTH
order by F.ID;