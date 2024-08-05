def generate_summary(inventory):
    total_units = 0
    highest_stock_item = None
    highest_units = None

    # Iterate through each item in the inventory
    for item_name in inventory:
        details = inventory[item_name]
        
        # Update total number of units
        total_units += details['units']

        # Check if this item has the highest number of units
        if highest_units is None or details['units'] > highest_units:
            highest_units = details['units']
            highest_stock_item = item_name

    return {
        'total_units': total_units,
        'highest_stock_item': (highest_stock_item, highest_units)
    }

inventory = {
    'Item A': {'category': 'Electronics', 'units': 8},
    'Item B': {'category': 'Furniture', 'units': 15},
    'Item C': {'category': 'Electronics', 'units': 12},
    'Item D': {'category': 'Office Supplies', 'units': 5}
}

print(generate_summary(inventory))
