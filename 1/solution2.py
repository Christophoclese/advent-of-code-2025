from pathlib import Path


def spinDial(line, dial):
    dir = line[0:1]
    dist = line[1:]
    zero_count = 0

    if dir == "L":
        op = "-"
    elif dir == "R":
        op = "+"

    next = eval(f"{dial} {op} {dist}")
    if next < 0:
        while next < 0:
            next = 100 + next
            zero_count += 1
        else:
            # If we start from 0, and move left, going negative will count an extra 0
            if dial == 0:
                zero_count -= 1
            elif next == 0:
                zero_count += 1
    elif next > 99:
        while next > 99:
            next = next - 100
            zero_count += 1
    elif next == 0:
        zero_count += 1
    return next, zero_count


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    dial = 50
    zeroes = 0

    print(f"The dial starts by pointing at {dial}")

    for line in input:
        dial, new_zeroes = spinDial(line, dial)
        zeroes += new_zeroes
        string = f"The dial is rotated {line} to point at {dial}"
        if new_zeroes:
            string += f"; during this rotation, it points at zero {new_zeroes} times."
        print(string)
    print(f"Zero total: {zeroes}")


if __name__ == "__main__":
    main()
