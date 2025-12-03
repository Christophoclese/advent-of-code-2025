from pathlib import Path


def find_repeat(x):
    string = str(x)
    num_digits = len(string)
    mid = num_digits // 2

    for i in range(1, mid + 1):
        part = string[0:i]
        if part * (num_digits // i) == string:
            print(f"Found repeat: {string}")
            return True

    return False


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    range_list = input[0].split(",")
    invalid_ids = []

    for id_range in range_list:
        first, last = [int(x) for x in id_range.split("-")]

        for num in range(first, last + 1):
            if find_repeat(num):
                invalid_ids.append(num)

    print(f"{sum(invalid_ids)}")


if __name__ == "__main__":
    main()
