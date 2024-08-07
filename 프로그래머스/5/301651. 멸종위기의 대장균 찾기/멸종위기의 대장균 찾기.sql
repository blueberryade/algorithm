-- 코드를 작성해주세요
WITH RECURSIVE GENDATA AS (
    SELECT ID,PARENT_ID,1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT A.ID,A.PARENT_ID,(GENERATION+1) AS GENERATION
    FROM ECOLI_DATA A JOIN GENDATA B
    ON A.PARENT_ID = B.ID
    
)


SELECT COUNT(*) AS COUNT ,GENERATION
FROM GENDATA
WHERE ID NOT IN
(SELECT DISTINCT PARENT_ID FROM GENDATA WHERE PARENT_ID IS NOT NULL)
GROUP BY GENERATION
ORDER BY 2;