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
