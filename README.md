Explanation of the Algorithm:
Initialization:

Start at the top-right corner of the matrix at position (0, cols-1).
Comparison Logic:

If the current element is equal to the target, return True.
If the current element is larger than the target, move left (decrease the column index).
If the current element is smaller than the target, move down (increase the row index).
Termination:

The loop continues until the row index goes out of bounds or the column index goes negative, indicating that the target is not in the matrix.
