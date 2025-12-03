from pathlib import Path


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    range_list = input[0].split(",")
    invalid_ids = []

    for id_range in range_list:
        first, last = [int(x) for x in id_range.split("-")]

        for num in range(first, last + 1):
            s_num = str(num)
            num_digits = len(s_num)
            mid = num_digits // 2
            if s_num[0:mid] == s_num[mid:]:
                invalid_ids.append(num)

    print(f"{sum(invalid_ids)}")


if __name__ == "__main__":
    main()
