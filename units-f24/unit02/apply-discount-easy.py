def apply_discounts(order_amounts) -> list[float]:
    index: int = 0
    counter: int = 0
    discounted_amounts = []

    while index < len(order_amounts):
        amount = order_amounts[index]

        if amount > 50:
            discount = 0.10
        else:
            discount = 0

        discounted_amount = amount * (1 - discount)
        discounted_amounts.append(discounted_amount)

        counter += 1
        index += 1

    print(f"Total orders processed: {counter}")
    return discounted_amounts

def main() -> None:
    order_amounts = [45, 75, 150, 30]
    discounted_amounts = apply_discounts(order_amounts)
    print(discounted_amounts)

if __name__ == "__main__":
    main()
