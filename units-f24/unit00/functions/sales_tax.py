print("_ _ _reciept_ _ _")
amount: int = 100
sales_tax: float = 7
currency: str = "$"

def amount_you_owe(amount_due: int, tax: float) -> float:
    tax_fraction = tax / 100

    total_amount = amount_due * (1 + tax_fraction)
    return total_amount

def format_price(price: float, currency: str) -> str:
    result = currency + str(price)
    
    return result

print("amount: " + format_price(amount, currency))

print("sales tax: " + str(sales_tax) + "%")

print("total: " + format_price(amount_you_owe(amount, sales_tax), currency))

print("Thank you for shopping with us!")