def greet(name: str) -> str:
    print("Hello " + name + ", your name starts with an " + str(name[0]) + " and ends with an " + str(name[len(name) - 1]))
    return "I'm so happy to see you " + name + "!"

def main() -> None:
    print(greet(name="Viktora"))

main()
