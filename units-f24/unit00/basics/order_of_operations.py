def puppies(num_of_cats: int, num_of_dogs: int) -> int:
    # Calculate the initial number of pets
    num_of_pets = num_of_dogs + num_of_cats
    
    # Calculate the number of offspring (one per pair of cats and dogs) without using built-in functions or conditionals
    difference = num_of_cats - num_of_dogs
    absolute_difference = (difference ** 2) ** 0.5  # Compute absolute value using squaring and square root
    offspring = (num_of_cats + num_of_dogs - absolute_difference) / 2
    
    # Add the offspring to the total number of pets
    total_pets = num_of_pets + offspring
    
    return int(total_pets)

# Example usage
num_of_cats = 10
num_of_dogs = 5
print(puppies(num_of_cats, num_of_dogs))  # Output: 20










