def fuel_needed(distance, mpg):
   return distance / mpg

def total_fuel_cost(distance, mpg, price_per_gallon):
   print(fuel_needed(distance=distance, mpg=mpg) * price_per_gallon)

total_fuel_cost(distance=300, mpg=25, price_per_gallon=4)



