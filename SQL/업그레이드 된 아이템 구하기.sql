SELECT 
    i.item_id,
    i.item_name,
    i.rarity
FROM item_info i
WHERE i.item_id IN (
    SELECT DISTINCT t.item_id
    FROM item_info i JOIN item_tree t
    ON t.parent_item_id = i.item_id
    WHERE i.rarity = 'RARE'
)
ORDER BY i.item_id DESC;