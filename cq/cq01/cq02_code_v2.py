def get_first_val(inp_val: str) -> str:
    return inp_val[0]

def password_creator(first_name, last_name, birth_year) -> None:
    """Generate and print the password."""
    print(get_first_val(inp_val=first_name) + get_first_val(inp_val=last_name) + str(birth_year) + get_first_val(inp_val=str(birth_year)))

password_creator("John", "Doe", 1990)
password_creator("Alice", "Smith", 1985)