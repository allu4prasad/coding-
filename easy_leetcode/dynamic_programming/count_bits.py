class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        binary = ''
        for i in range(0, n+1):
            binary = str(bin(i).count('1'))
            res.append(binary)
        return res
