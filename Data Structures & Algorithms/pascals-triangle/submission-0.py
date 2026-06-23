def generate(numRows):
    result = [[1]]

    for row in range(1, numRows):
        curr = [1] * (row + 1)

        for col in range(1, row):
            curr[col] = (
                result[row - 1][col - 1] +
                result[row - 1][col]
            )

        result.append(curr)

    return result[:numRows]