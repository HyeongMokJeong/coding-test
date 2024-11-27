SELECT
    i.item_id,
    i.item_name
FROM item_info i JOIN item_tree it ON i.item_id = it.item_id
WHERE it.parent_item_id is null;