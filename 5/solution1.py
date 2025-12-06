from pathlib import Path


def split_list_after(data, element):
    sublists = []
    current_sublist = []
    for item in data:
        if item == element:
            sublists.append(current_sublist)
            current_sublist = []
        else:
            current_sublist.append(item)
    if current_sublist:  # Add any remaining elements
        sublists.append(current_sublist)
    return sublists


def inRange(n, ranges):
    for r in ranges:
        start, end = [int(s) for s in r.split("-")]
        if int(n) in range(start, end + 1):
            return n


def findFreshIngredients(fresh_ranges, ingredients):
    fresh_ingredients = []

    for ingredient in ingredients:
        if fresh_ingredient := inRange(ingredient, fresh_ranges):
            fresh_ingredients.append(fresh_ingredient)

    return fresh_ingredients


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    ranges, ingredients = split_list_after(input, "")

    print(
        f"There are {len(findFreshIngredients(ranges, ingredients))} fresh ingredients."
    )


if __name__ == "__main__":
    main()
