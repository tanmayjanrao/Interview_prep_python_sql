SELECT * FROM employees;


SELECT * FROM employees
WHERE name LIKE 'R%';


SELECT * FROM employees
WHERE salary >= 30000;

SELECT * FROM employees
WHERE salary BETWEEN 30000 AND 40000;


SELECT * FROM employees
WHERE department = 'IT';

SELECT * FROM employees
WHERE department IN ('IT', 'HR');


SELECT * FROM employees
ORDER BY salary DESC;


SELECT COUNT(*) AS total_employees
FROM employees;
