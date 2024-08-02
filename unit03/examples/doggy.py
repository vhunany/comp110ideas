class Dog:
    name: str
    breed: str 
    age: int

    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")

my_dog = Dog("Buddy", "Golden Retriever", 3)
print(my_dog.name)
print(my_dog.breed)
print(my_dog.age)
print(my_dog)
