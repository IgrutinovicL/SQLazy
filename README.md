# SQLazy
Do you find yourself googling for SQLITE queries all of the time? Well if you would like to avoid that part this is the solution.

- One thing you should note is that this is not to replace all of SQLITE3 syntax but to make it easier to do the repetitive stuff.
- This is super basic for now, feel free to modify the code and use it wherever. I would appreciate it if you would post issues you find and/or suggestions! 

#### VERSION -> alpha 


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
table     = SQLazy.CreateTable(conn,"testTable",structure)

```
- Insert values into a table:
```python
vals      = {"USERNAME":"default","PASSWORD":"default","POINTS":50}
SQLazy.InsertIntoTable(conn,"testTable",vals)
```
OR
```python
SQLazy.InsertIntoTable(conn,table,vals)
```
