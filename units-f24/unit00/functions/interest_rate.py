def combine_names(first_name, last_name):
    print(f"{first_name} {last_name}")
    return f"{first_name} {last_name}"

def length_is_odd(full_name):
    return len(full_name) % 2

def apply_rate_adjustment(base_rate, adjustment_factor):
    return base_rate * adjustment_factor

def determine_interest_rate(first_name, last_name, base_rate):
    return apply_rate_adjustment(base_rate, adjustment_factor = 0.9 + 0.2 * length_is_odd(combine_names(first_name, last_name)))

print(determine_interest_rate("Jane", "Doe", 5.0))
