-- 코드를 작성해주세요
SELECT
    ITEM_ID,
    ITEM_NAME,
    RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (
    SELECT A.ITEM_ID
    FROM ITEM_TREE AS A INNER JOIN ITEM_TREE AS B
        ON A.ITEM_ID = B.PARENT_ITEM_ID
)
ORDER BY ITEM_ID DESC