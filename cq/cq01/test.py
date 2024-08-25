def get_first_initial(inp_name: str) -> str:
    return inp_name[0]

def get_length(inp_name: str) -> int:
    return len(inp_name)

def password_creator(first_name, last_name, birth_year) -> None:
    print(get_first_initial(inp_name=first_name) + get_first_initial(inp_name=last_name) + str(get_length(inp_name=first_name)) + str(get_length(inp_name=last_name)) + str(birth_year))

password_creator(first_name="John", last_name="Doe", birth_year=1990)
password_creator(first_name="Alice", last_name="Smith", birth_year=1985)


