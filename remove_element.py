class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        leng = len(A)
        j = 0
        for i in range(leng):
            if A[i] != elem:
                A[j] = A[i]
                j += 1
        return j
