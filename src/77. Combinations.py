# Approach 1: Recursive
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            rs = []
            rs += self.combine(n - 1, k)
            part = self.combine(n - 1, k - 1)
            for ls in part:
                ls.append(n)
            rs += part
            return rs


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))