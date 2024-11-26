SELECT
    fw.warehouse_id,
    fw.warehouse_name,
    fw.address,
    IFNULL(fw.freezer_yn, 'N') AS FREEZER_YN
FROM food_warehouse fw
WHERE fw.address LIKE '%경기%';