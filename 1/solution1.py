from pathlib import Path


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    dial = 50
    zero_count = 0

    print(f"The dial starts by pointing at {dial}")

    for line in input:
        dir = line[0:1]
        dist = line[1:]

        if dir == "L":
            op = "-"
        elif dir == "R":
            op = "+"

        next = eval(f"{dial} {op} {dist}")
        if next < 0:
            while next < 0:
                next = 100 + next
        elif next > 99:
            while next > 99:
                next = next - 100

        dial = next

        print(f"The dial is rotated {line} to point at {dial}")

        if dial == 0:
            zero_count += 1

    print(f"Zero total: {zero_count}")


if __name__ == "__main__":
    main()
