class Solution:

    modulo = pow(10, 9) + 7

    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        return (max(j - i for i, j in zip(horizontalCuts,
                                          horizontalCuts[1:])) *
                max(j - i for i, j in zip(verticalCuts, verticalCuts[1:])) %
                Solution.modulo)
