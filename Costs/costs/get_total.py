# get_total.py

def get_total(costs, items_bought, tax_rate):
    # Calculate the total cost of the items bought
    total_cost = sum(costs.get(item, 0) for item in items_bought)
    
    # Calculate the total cost with tax
    total_cost_with_tax = total_cost * (1 + tax_rate)
    
    # Return the total cost rounded to two decimal places
    return round(total_cost_with_tax, 2)
