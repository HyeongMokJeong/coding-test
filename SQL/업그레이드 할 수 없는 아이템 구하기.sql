select 
    II.ITEM_ID,
    II.ITEM_NAME,
    II.RARITY
from ITEM_INFO II left join ITEM_TREE IT on II.ITEM_ID = IT.PARENT_ITEM_ID
where IT.PARENT_ITEM_ID is null
order by II.ITEM_ID desc;