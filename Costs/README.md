# DESCRIPTION
## How much will you spend?


### Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.

> **Note:** If item doesn't exist in the given cost values, the item is ignored.

> **Note:**
> Output should be rounded to two decimal places.

```python
costs = {'socks':5, 'shoes': 60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
#-> 5+60 65
#-> 65 +0.09 of 65 70.85
#-> Output: 70.85
```