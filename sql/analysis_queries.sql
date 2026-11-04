
-- CUSTOMER SUPPORT DATA ANNOTATION PROJECT
-- SQL Analysis Queries

USE customer_support_db;

-- 1. Total number of tickets
SELECT COUNT(*) AS total_tickets
FROM annotated_tickets;


-- 2. Sentiment distribution
SELECT sentiment, COUNT(*) AS total_tickets
FROM annotated_tickets
GROUP BY sentiment
ORDER BY total_tickets DESC;


-- 3. Intent distribution
SELECT intent, COUNT(*) AS total_tickets
FROM annotated_tickets
GROUP BY intent
ORDER BY total_tickets DESC;


-- 4. Priority distribution
SELECT priority, COUNT(*) AS total_tickets
FROM annotated_tickets
GROUP BY priority
ORDER BY CASE
    WHEN priority = 'High' THEN 1
    WHEN priority = 'Medium' THEN 2
    WHEN priority = 'Low' THEN 3
END;


-- 5. Category distribution
SELECT category, COUNT(*) AS total_tickets
FROM annotated_tickets
GROUP BY category
ORDER BY total_tickets DESC;


-- 6. Display all high-priority tickets
SELECT ticket_id, customer_id, message,
       category, intent, priority
FROM annotated_tickets
WHERE priority = 'High'
ORDER BY category;


-- 7. Total number of high-priority tickets
SELECT COUNT(*) AS high_priority_tickets
FROM annotated_tickets
WHERE priority = 'High';


-- 8. High-priority tickets by category
SELECT category,
       COUNT(*) AS high_priority_count
FROM annotated_tickets
WHERE priority = 'High'
GROUP BY category
ORDER BY high_priority_count DESC;


-- 9. Categories having more than 10 tickets
SELECT category, COUNT(*) AS total_tickets
FROM annotated_tickets
GROUP BY category
HAVING COUNT(*) > 10;


-- 10. Priority classification using CASE
SELECT
    ticket_id,
    category,
    priority,
    CASE
        WHEN priority = 'High' THEN 'Immediate Attention'
        WHEN priority = 'Medium' THEN 'Review Required'
        ELSE 'Normal'
    END AS action_required
FROM annotated_tickets;


-- 11. Rank categories by ticket volume using a CTE
WITH category_counts AS (
    SELECT category, COUNT(*) AS total_tickets
    FROM annotated_tickets
    GROUP BY category
)
SELECT
    category,
    total_tickets,
    RANK() OVER (ORDER BY total_tickets DESC) AS category_rank
FROM category_counts;


-- 12. Rank tickets by priority within each category
SELECT
    ticket_id,
    category,
    priority,
    ROW_NUMBER() OVER (
        PARTITION BY category
        ORDER BY
            CASE
                WHEN priority = 'High' THEN 1
                WHEN priority = 'Medium' THEN 2
                ELSE 3
            END
    ) AS ticket_rank
FROM annotated_tickets;

