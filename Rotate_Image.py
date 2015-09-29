class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        while left <= right and top <= bottom:
            for i, num in zip(xrange(top, bottom + 1), xrange(bottom + 1 - top)):
                temp_m = []
                temp_m.append(matrix[i][right]) 
            for i, j in zip(xrange(left, right + 1), xrange(top, bottom + 1)):
                matrix[j][right] = matrix[top][i]

            for i, num in zip(xrange())
