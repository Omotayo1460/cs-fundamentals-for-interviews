# 🗄️ DBMS — Interview Q&A

[← Back to index](README.md) · Related: [OS](operating-systems.md) · [Networks](computer-networks.md) · [OOP](oop.md)

---

## Core concepts (1-line each)

- **DBMS** = software to store, retrieve, and manage data (MySQL, PostgreSQL, Oracle).
- **RDBMS** = a DBMS based on the relational model (tables of rows & columns).
- **Schema** = the structure/blueprint of the database; **instance** = the actual data at a moment.

---

## Top questions

**1. What is normalization? Why normalize?**
Organizing tables to reduce **redundancy** and avoid update/insert/delete anomalies.
- **1NF** — atomic values, no repeating groups.
- **2NF** — 1NF + no partial dependency (non-key fully depends on the whole primary key).
- **3NF** — 2NF + no transitive dependency (non-key depends only on the key).
- **BCNF** — stricter 3NF: every determinant is a candidate key.

**2. Denormalization?**
Intentionally adding redundancy to speed up reads (fewer joins), at the cost of write
complexity. Used in read-heavy/analytics systems.

**3. Explain ACID properties.**
- **Atomicity** — all or nothing.
- **Consistency** — a transaction moves the DB from one valid state to another.
- **Isolation** — concurrent transactions don't interfere.
- **Durability** — committed data survives crashes.

**4. Primary key vs Unique key vs Foreign key?**
- **Primary** — uniquely identifies a row; not null; one per table.
- **Unique** — unique values but allows one null; many per table.
- **Foreign** — references a primary key in another table (enforces referential integrity).

**5. Clustered vs Non-clustered index?**
A **clustered** index determines the physical order of rows (one per table; usually the
primary key). A **non-clustered** index is a separate structure with pointers to rows
(many allowed). Clustered = faster range scans; non-clustered = extra lookup.

**6. What is an index? Trade-off?**
A data structure (usually a B+ tree) that speeds up lookups. Trade-off: faster **reads**
but slower **writes** (index must be updated) and extra storage.

**7. DELETE vs TRUNCATE vs DROP?**
- **DELETE** — removes rows (with WHERE), logged, can rollback, keeps the table.
- **TRUNCATE** — removes all rows fast, minimal logging, can't filter, resets identity.
- **DROP** — removes the entire table (structure + data).

**8. Types of JOINs?**
- **INNER** — only matching rows.
- **LEFT/RIGHT** — all rows from one side + matches (nulls otherwise).
- **FULL OUTER** — all rows from both, matched where possible.
- **CROSS** — Cartesian product.

**9. WHERE vs HAVING?**
**WHERE** filters rows *before* grouping; **HAVING** filters *after* `GROUP BY`
(works on aggregates like `COUNT`, `SUM`).

**10. What is a transaction?**
A unit of work executed as a whole. Ends with **COMMIT** (save) or **ROLLBACK** (undo).

**11. What are isolation levels?**
Read Uncommitted → Read Committed → Repeatable Read → Serializable. Higher = fewer
anomalies (dirty read, non-repeatable read, phantom read) but less concurrency.

**12. Dirty read, non-repeatable read, phantom read?**
- **Dirty read** — reading uncommitted data.
- **Non-repeatable read** — same row read twice gives different values.
- **Phantom read** — same query returns different *rows* (insert/delete by another txn).

**13. SQL vs NoSQL?**
**SQL** — structured, fixed schema, relational, strong ACID (MySQL, Postgres). **NoSQL** —
flexible schema, horizontally scalable, eventual consistency (MongoDB, Cassandra, Redis).
Choose SQL for complex relations/transactions, NoSQL for scale/flexible data.

**14. What is a candidate key / super key?**
A **super key** is any set of columns that uniquely identifies a row. A **candidate key**
is a minimal super key. The chosen candidate key becomes the **primary key**.

**15. What is a view?**
A virtual table defined by a query. Simplifies complex queries and can restrict access.
A **materialized view** stores the result physically for faster reads.

**16. What is a stored procedure?**
Precompiled SQL stored in the DB and called by name. Reduces network traffic and
centralizes logic.

**17. ER model — entity, attribute, relationship?**
**Entity** = a real-world object (Student). **Attribute** = a property (name). **Relationship**
= association between entities (Student *enrolls in* Course).

**18. Explain CAP theorem (for distributed DBs).**
In a network partition you can only have two of: **Consistency, Availability, Partition
tolerance**. Since partitions happen, real systems trade C vs A.

---

### Quick SQL to remember

```sql
-- 2nd highest salary
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- count per group, only groups with > 5
SELECT dept, COUNT(*) FROM employees
GROUP BY dept HAVING COUNT(*) > 5;
```


## 10 Classic SQL Query Interview Questions and Answers

### Q1: What is the difference between ROW_NUMBER(), RANK(), and DENSE_RANK()? Provide an example.
* **ROW_NUMBER():** Assigns a unique sequential integer to rows, breaking ties randomly if values match.
* **RANK():** Assigns the same rank to identical values, but skips numbers for subsequent ranks (e.g., 1, 2, 2, 4).
* **DENSE_RANK():** Assigns the same rank to identical values without skipping any numbers (e.g., 1, 2, 2, 3).
```sql
SELECT employee_id, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,
       RANK() OVER (ORDER BY salary DESC) as rnk,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rnk
FROM Employee;
```

### Q2: How do you identify a performance bottleneck in a slow-running SQL query, and how would you fix it?
* **Identification:** Use the `EXPLAIN` or `EXPLAIN ANALYZE` commands before the query to inspect the database execution plan and look for expensive sequential scans (Full Table Scans).
* **Optimization:** Add indexes to columns heavily utilized in `WHERE` filtering or `JOIN` conditions, replace resource-heavy subqueries with `WITH` clauses (CTEs), and ensure you are only pulling necessary columns instead of using `SELECT *`.

### Q3: What is the difference between INNER JOIN and LEFT JOIN?
* **INNER JOIN:** Returns records that have matching values in both tables.
* **LEFT JOIN:** Returns all records from the left table, and the matched records from the right table. If no match, returns NULL values for the right table.

### Q4: How do you delete duplicate records from a table while keeping the original?
```sql
DELETE FROM Employee 
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM Employee 
    GROUP BY email
);
```

### Q5: Write a query to find employees who earn more than their managers.
```sql
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

### Q6: How do you select all records where a name starts with the letter 'A'?
```sql
SELECT * FROM customers 
WHERE customer_name LIKE 'A%';
```

### Q7: What is the difference between WHERE and HAVING clauses?
* **WHERE:** Filters individual rows *before* any grouping (GROUP BY) takes place.
* **HAVING:** Filters summarized group data *after* the GROUP BY clause has been applied.

### Q8: How do you get the current date and time in SQL?
```sql
-- In PostgreSQL / MySQL:
SELECT NOW();

-- In SQL Server:
SELECT GETDATE();
```

### Q9: Write a query to get the Nth highest salary using a Window Function.
```sql
WITH RankedSalaries AS (
    SELECT salary, 
           DENSE_RANK() OVER (ORDER BY salary DESC) as rank_num
    FROM Employee
)
SELECT salary 
FROM RankedSalaries 
WHERE rank_num = 2; -- Change 2 to N for any position
```

### Q10: How do you find rows that contain NULL values in a specific column?
```sql
SELECT * FROM orders 
WHERE shipping_date IS NULL;
```
