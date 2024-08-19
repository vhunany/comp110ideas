"""Tea Party! First exercise -- functions."""

__author__: str = "737070661"


def main_planner(guests: int) -> None: 
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_count=tea_bags(guests), treat_count=treats(guests))}")


def tea_bags(people: int) -> int: 
    return 2 * people


def treats(people: int) -> int: 
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float: 
    tea_bag_cost: float = 0.5
    treat_cost: float = 0.75
    return tea_bag_cost * tea_count + treat_cost * treat_count

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))