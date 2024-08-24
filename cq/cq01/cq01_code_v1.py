def get_tax(price, tax_rate):
    return price * tax_rate

def total_cost(price, tax_rate):
    return price + get_tax(price=price, tax_rate=tax_rate)

print(total_cost(price=100, tax_rate=0.07))