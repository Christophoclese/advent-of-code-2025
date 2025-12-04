from pathlib import Path


def findBest(bank):
    best = 0

    for index, first_char in enumerate(bank):
        # print(f"{index}: {first_char}")
        # bank.copy().pop(index)
        for second_char in bank[index + 1 :]:
            total = int(first_char + second_char)
            if total > best:
                best = total
    print(f"Best battery in bank '{bank}' is '{best}'")
    return best


def getBest(banks):
    best_batteries = []

    for bank in banks:
        best_batteries.append(findBest(bank))

    print(f"Best batteries: {best_batteries}")
    return best_batteries


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    print(f"Total output joltage: {sum(getBest(input))}")


if __name__ == "__main__":
    main()
