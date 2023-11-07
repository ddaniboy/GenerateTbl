
# How To Use?

### Creating new table.
```python
NameOfTable = GenerateTable("Colunm1", "Colunm2")
```
### Add a new rows with informations.

```python
NameOfTable.add("Information in Colunm 1", "Information in Colunm 2")
```

### Merge informations to table.

```python
result = NameOfTable.merge()
print(results)
```

Result:
```bash
_____________________________________________________
| Colunm1                 | Colunm2                 |
-----------------------------------------------------
| Information in Colunm 1 | Information in Colunm 2 |
-----------------------------------------------------
```


# New Function - (11/23):
* clear - to clear the table.
* getline - return dictionary with informations from the selected line.
* mergeline - merges information from rows in the table.
* remove - used for remove row from table.
