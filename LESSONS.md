# Lessons: Python OOP & SQL Tricks

Reference curriculum for the `daily-exercises` project. Each day = 2 Python
exercises + 2 SQL exercises. Use this file (together with `progress.json`) as
the source of truth for what's next.

## How to use this file with Claude Code

```
Read LESSONS.md and progress.json, then create day-0X/ with exercises
for the next topic in the list that hasn't been covered yet.
```

Claude Code will pick the next uncovered topic, generate exercises in the
same style as `day-01/`, and update `progress.json` automatically.

---

## Python Track (OOP → Dataclasses → Patterns → Advanced)

| # | Topic | Description |
|---|-------|-------------|
| 1 | Dataclasses & Validation | `@dataclass`, `__post_init__`, field defaults, computed properties |
| 2 | Abstract Base Classes | `ABC`, `@abstractmethod`, enforcing interfaces across subclasses |
| 3 | Dunder Methods | `__eq__`, `__repr__`, `__lt__`, `__hash__`, making custom objects comparable/sortable |
| 4 | Properties & Descriptors | `@property`, setters/deleters, computed vs. stored attributes |
| 5 | Class vs. Static Methods | `@classmethod` factories, `@staticmethod` utilities, alt constructors |
| 6 | Composition over Inheritance | building objects out of smaller objects instead of deep hierarchies |
| 7 | Design Pattern: Strategy | swapping algorithms at runtime via interchangeable classes |
| 8 | Design Pattern: Factory | centralizing object creation logic |
| 9 | Design Pattern: Observer | pub/sub between objects, event-driven updates |
| 10 | Type Hints & Generics | `TypeVar`, `Generic[T]`, `Protocol` for structural typing |
| 11 | Context Managers | `__enter__`/`__exit__`, `contextlib.contextmanager` for resource handling |
| 12 | Iterators & Generators in Classes | `__iter__`, `__next__`, lazy evaluation with custom objects |
| 13 | Mixins | reusable behavior via multiple inheritance without deep hierarchies |
| 14 | Error Handling in OOP | custom exception hierarchies, `raise ... from`, fail-fast design |

## SQL Track (Postgres-focused)

| # | Topic | Description |
|---|-------|-------------|
| 1 | Window Functions Basics | `RANK`, `DENSE_RANK`, `LAG`/`LEAD` for running comparisons |
| 2 | CTEs | `WITH` clauses for readable multi-step queries |
| 3 | Recursive CTEs | hierarchical/tree data (e.g. org charts, categories) |
| 4 | JSON/JSONB Queries | `->`, `->>`, `jsonb_agg`, indexing JSON fields |
| 5 | LATERAL Joins | correlated subqueries that reference preceding tables in the FROM clause |
| 6 | Upserts | `INSERT ... ON CONFLICT DO UPDATE`, idempotent writes |
| 7 | Aggregate Filters | `FILTER (WHERE ...)` for conditional aggregation in one pass |
| 8 | Indexing Tricks | `EXPLAIN ANALYZE`, partial indexes, when a query needs one |
| 9 | Full-Text Search | `tsvector`, `tsquery`, `to_tsvector`, ranking search results |
| 10 | Array Operations | `unnest`, `ANY`, array aggregation and containment checks |
| 11 | Window Frames | `ROWS BETWEEN`, `RANGE`, custom running totals / moving averages |
| 12 | Partitioning | table partitioning strategies for large datasets |
| 13 | Common Anti-Patterns | N+1 queries, `SELECT *` pitfalls, implicit type casts that kill indexes |
| 14 | Transactions & Isolation | `BEGIN`/`COMMIT`, isolation levels, deadlock scenarios |

---

## Notes for Claude Code

- Match the format of `day-01/python_exercise.py` and `day-01/sql_exercise.sql`
  (2 exercises each, test assertions, solutions commented out at the bottom).
- Increase difficulty gradually as topics progress down each table.
- Update `progress.json` after generating a new day (add entry, keep
  `next_up_ideas` in sync by removing what's now covered).
- Don't repeat a topic already marked in `progress.json` unless the user asks
  for a review/refresher explicitly.
