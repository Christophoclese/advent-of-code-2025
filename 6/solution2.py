from pathlib import Path


def answerProblems(worksheet):
    width = len(worksheet[0])
    height = len(worksheet)

    nums = []
    answers = []

    for col in range(width - 1, -1, -1):
        val = ""
        for row in range(height - 1):
            new_char = worksheet[row][col]
            val += new_char if new_char != " " else ""
        if val:
            nums.append(val)
        if worksheet[row + 1][col] != " ":
            op = worksheet[row + 1][col]
            answers.append(eval(op.join(nums)))
            nums = []
    return answers


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().splitlines()

    print(sum(answerProblems(input)))


if __name__ == "__main__":
    main()
