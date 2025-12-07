from pathlib import Path


def parse_line(row):
    return [i.strip() for i in [s for s in row.split(" ") if s != ""]]


def parse_worksheet(lines):
    worksheet = []

    for index, line in enumerate(lines):
        worksheet.append(parse_line(line))

    return worksheet


def doMath(array):
    nums = array[:-1]
    op = array[-1]
    return eval(op.join(nums))


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    worksheet = parse_worksheet(input)
    width = len(worksheet[0])
    height = len(worksheet)
    answers = []

    for col, _ in enumerate(range(width)):
        c = []
        for row, _ in enumerate(range(height)):
            c.append(worksheet[row][col])
        answers.append(doMath(c))

    print(sum(answers))


if __name__ == "__main__":
    main()
