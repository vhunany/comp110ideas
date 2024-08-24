def get_tax(price, tax_rate):
    return price * tax_rate

def total_cost(price, tax_rate):
    return price + get_tax(price, tax_rate)

# Example usage:
print(total_cost(100, 0.07))  # Should output 107.0

# Can be replaced by one function
"""

def total_cost(price, tax_rate):
    return price + (price * tax_rate)

# Example usage:
print(total_cost(100, 0.07))  # Should output 107.0

"""
