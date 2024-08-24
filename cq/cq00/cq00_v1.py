def fuel_needed(distance, mpg):
    return distance / mpg

def total_fuel_cost(distance, mpg, price_per_gallon):
    return fuel_needed(distance, mpg) * price_per_gallon

# Example usage:
print(total_fuel_cost(300, 25, 4))  # Should output 48.0


# Can be replaced by one function
"""

def total_fuel_cost(distance, mpg, price_per_gallon):
    return (distance / mpg) * price_per_gallon

# Example usage:
print(total_fuel_cost(300, 25, 4))  # Should output 48.0

"""

