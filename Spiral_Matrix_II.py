class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        matrix = [[ 0 for __ in xrange(n)] for _ in xrange(n)]
        total = n * n
        n_v = 1
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        while n_v <= total:
            for i in xrange(left, right + 1):
                matrix[top][i] = n_v
                n_v += 1
                if n_v >= total:
                    return matrix
                print(matrix)
            for i in xrange(top + 1, bottom):
                matrix[i][right] = n_v
                n_v += 1
                print(matrix)
            for i in reversed(xrange(left + 1, right + 1)):
                matrix[bottom][i] = n_v
                n_v += 1
                print(matrix)
            for i in reversed(xrange(top + 1, bottom + 1)):
                matrix[i][left] = n_v
                n_v += 1
                print(matrix)

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix

a = Solution()
print(a.generateMatrix(4))

