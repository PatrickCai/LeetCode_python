dd = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if matrix == [] or matrix[0] == []:
            return []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        results = []
        while left <= right and top <= bottom:
            for i in xrange(left, right+1):
                results.append(matrix[top][i])
            for i in xrange(top + 1, bottom + 1):
                results.append(matrix[i][right])
            if top < bottom:
                for i in reversed(xrange(left, right)):
                    results.append(matrix[bottom][i])
            if left < right:
                for i in reversed(xrange(top+1, bottom)):
                    results.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return results

a = Solution()
print(a.spiralOrder(dd))
