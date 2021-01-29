# SQLazy
Do you find yourself googling for SQLITE queries all of the time? Well if you would like to avoid that part this is the solution.
#### ALPHA


## Examples

- Import SQLazy.py
```python
import SQLazy
```

- Create a database:
```python
conn = SQLazy.CreateDatabase("test.db")
```
- Create a table:
```python
structure = {"USERNAME":"VARCHAR(20)","PASSWORD":"VARCHAR(20)","POINTS":"INTEGER"}
SQLazy.CreateTable(conn,"testTable",structure)

```
- Insert values into a table:
```python
vals      = {"USERNAME":"default","PASSWORD":"default","POINTS":50}
SQLazy.InsertIntoTable(conn,"testTable",vals)
```
