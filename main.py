# Search for a value "target" in an m x n matrix of integers.
# Elements in each row are sorted in ascending from left to right.
# Elements in each column are sorted in ascending from top to bottom.


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    # Start from the top-right corner
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    # Perform the staircase search
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True  # Found the target
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    # Target not found
    return False


def main():
    # Example matrix and target
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = int(input("Enter the target you want to search for: "))

    # Perform the search
    result = searchMatrix(matrix, target)

    # Output the result
    if result:
        print(f"Target {target} found in the matrix.")
    else:
        print(f"Target {target} not found in the matrix.")


if __name__ == "__main__":
    main()

