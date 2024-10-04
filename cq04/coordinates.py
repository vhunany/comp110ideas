xs = "01"
ys = "23"
result = ""

def get_coords() -> None:
    x_idx: int = 0
    while x_idx < len(xs):
        y_idx: int = 0
        while y_idx < len(ys):
            result += f"({xs[x_idx]},{ys[y_idx]}) "  # Concatenate the coordinates
            y_idx += 1
        x_idx += 1

if __name__ == "__main__":
    get_coords()
    print(result)

