def apply_discounts(order_amounts):
    index = 0  # Indexing variable to keep track of the current position in the list
    counter = 0  # Counter variable to count the number of orders processed
    discounted_amounts = []  # List to store the discounted amounts

    while index < len(order_amounts):  # Continue while there are orders left to process
        amount = order_amounts[index]  # Get the current order amount

        # Apply a discount of 10% if the order amount is greater than $50
        if amount > 50:
            discount = 0.10
        else:
            discount = 0

        discounted_amount = amount * (1 - discount)  # Calculate the discounted amount
        discounted_amounts.append(discounted_amount)  # Store the discounted amount

        counter += 1  # Increment the counter
        index += 1  # Move to the next order

    print(f"Total orders processed: {counter}")
    return discounted_amounts

# Example usage
order_amounts = [45, 75, 150, 30]
discounted_amounts = apply_discounts(order_amounts)
print(discounted_amounts)
