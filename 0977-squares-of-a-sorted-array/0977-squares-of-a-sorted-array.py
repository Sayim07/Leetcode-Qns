class Solution(object):
    def sortedSquares(self, nums):

        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        if len(neg) == 0:
            result = []

            for x in pos:
                result.append(x * x)

            return result

        if len(pos) == 0:
            result = []

            for x in neg:
                result.append(x * x)

            result.reverse()

            return result

        negSquares = []

        for x in neg:
            negSquares.append(x * x)

        negSquares.reverse()

        posSquares = []

        for x in pos:
            posSquares.append(x * x)

        n = len(negSquares)
        m = len(posSquares)

        result = []

        i = 0
        j = 0

        while i < n and j < m:

            if negSquares[i] <= posSquares[j]:
                result.append(negSquares[i])
                i = i + 1
            else:
                result.append(posSquares[j])
                j = j + 1

        while i < n:
            result.append(negSquares[i])
            i = i + 1

        while j < m:
            result.append(posSquares[j])
            j = j + 1

        return result