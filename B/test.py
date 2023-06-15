class Solution:
    stones = [2, 7, 4, 1, 8, 1]

    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        s = self.stones
        length = len(s)

        while length != 1:
            m = max(s)
            s.remove(m)

            for i in range(len(s)):
                if s[i] == max:
                    s.remove(s[i])
                    continue
            semi = max(s)
            nokori = m-semi
            s.remove(semi)
            s.append(nokori)
            length = len(s)
        print(s)
