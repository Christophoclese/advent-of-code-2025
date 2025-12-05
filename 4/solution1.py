from pathlib import Path


def getNeighborCount(row, col, map):
    neighbors = 0
    height = len(map) - 1
    width = len(map[0]) - 1

    # up-left
    if row > 0 and col > 0 and map[row - 1][col - 1] == "@":
        neighbors += 1
    # up
    if row > 0 and map[row - 1][col] == "@":
        neighbors += 1
    # up-right
    if row > 0 and col < width and map[row - 1][col + 1] == "@":
        neighbors += 1
    # left
    if col > 0 and map[row][col - 1] == "@":
        neighbors += 1
    # mid
    # if map[row][col] == "@":
    #    neighbors += 1
    # right
    if col < width and map[row][col + 1] == "@":
        neighbors += 1
    # down-left
    if row < height and col > 0 and map[row + 1][col - 1] == "@":
        neighbors += 1
    # down
    if row < height and map[row + 1][col] == "@":
        neighbors += 1
    # down-right
    if row < height and col < width and map[row + 1][col + 1] == "@":
        neighbors += 1

    return neighbors


def startForklifts(floor):
    total = 0

    for row_index, row in enumerate(floor):
        for col_index, pos in enumerate(row):
            if pos == "@":
                # Check for less than 4 '@' neighbors
                if 4 > getNeighborCount(row_index, col_index, floor):
                    # new_string = (
                    #    floor[row_index][:col_index]
                    #    + "x"
                    #    + floor[row_index][col_index + 1 :]
                    # )
                    # floor[row_index] = new_string
                    total += 1
    return total


def main():
    input_path = Path(__file__).resolve().parent / "input"
    with input_path.open("r", encoding="utf-8") as f:
        input = f.read().strip().splitlines()

    print(f"Rolls forked: {startForklifts(input)}")


if __name__ == "__main__":
    main()
