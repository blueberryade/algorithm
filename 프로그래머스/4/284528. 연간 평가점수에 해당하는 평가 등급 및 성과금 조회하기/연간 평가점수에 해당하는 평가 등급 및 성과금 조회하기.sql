-- 코드를 작성해주세요
# 사번, 성명, 평가 등급, 성과금
SELECT A.EMP_NO,A.EMP_NAME,
       CASE
            WHEN AVG(SCORE) >=96 THEN 'S'
            WHEN AVG(SCORE) >=90 THEN 'A'
            WHEN AVG(SCORE) >=80 THEN 'B'
            ELSE 'C'
            END AS GRADE,
       CASE
            WHEN AVG(SCORE) >=96 THEN A.SAL * 0.2
            WHEN AVG(SCORE) >=90 THEN A.SAL * 0.15
            WHEN AVG(SCORE) >=80 THEN A.SAL * 0.1
            ELSE 0
            END AS BONUS      
FROM HR_EMPLOYEES A JOIN HR_GRADE B
ON A.EMP_NO = B.EMP_NO
GROUP BY A.EMP_NO
ORDER BY A.EMP_NO;