-- 코드를 입력하세요
SELECT TO_CHAR(sales_date,'YYYY') AS YEAR,
TO_NUMBER(TO_CHAR(sales_date,'MM')) AS MONTH,
GENDER,
COUNT(DISTINCT USER_ID) AS USERS
FROM USER_INFO A
JOIN ONLINE_SALE B
USING(USER_ID)
WHERE GENDER IS NOT NULL
GROUP BY TO_CHAR(sales_date,'YYYY'),TO_CHAR(sales_date,'MM'),GENDER
ORDER BY YEAR,MONTH,GENDER;
