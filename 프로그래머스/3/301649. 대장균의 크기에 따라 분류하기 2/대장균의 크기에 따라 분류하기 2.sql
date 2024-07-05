-- 코드를 작성해주세요
SELECT B.ID,
CASE WHEN B.COLONY = 1 THEN 'CRITICAL'
WHEN B.COLONY = 2 THEN 'HIGH'
WHEN B.COLONY = 3 THEN 'MEDIUM'
ELSE 'LOW'
END
AS COLONY_NAME
FROM 
(
    SELECT ID,NTILE(4)
    OVER (ORDER BY SIZE_OF_COLONY DESC) AS COLONY
    FROM ECOLI_DATA 
) AS B
ORDER BY B.ID;