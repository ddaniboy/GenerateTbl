# what is it?
A simple tool to generate tables in terminal for more organized results.

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
```
_____________________________________________________
| Colunm1                 | Colunm2                 |
-----------------------------------------------------
| Information in Colunm 1 | Information in Colunm 2 |
-----------------------------------------------------
```
