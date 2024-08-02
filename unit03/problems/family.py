"""
Targets: 
- constructor only takes self (Q1.13)
- dictionaries with class objects (Q6.3 - 6.2)
"""

class Child:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Parent:
    def __init__(self):
        # Initialize the attribute with an empty dictionary
        self.children = {}

    def add_child(self, name: str):
        # Create a new Child object and add it to the dictionary
        child = Child(name)
        self.children[name] = child

    def get_child(self, name: str):
        # Retrieve a Child object by name, handle the case where the name might not exist
        if name in self.children:
            return self.children[name]
        else:
            return None
    
    def __str__(self): 
        if not self.children:
            return "Parent has no children."
        
        children_names = ""
        for name in self.children:
            if children_names:
                children_names += ", "  # Add comma separator
            children_names += name
        
        return f"Parent has children: {children_names}"

# Example usage
parent: Parent = Parent()
parent.add_child('Alice')
parent.add_child('Bob')

print(parent)  # Output: Parent has children: Alice, Bob
