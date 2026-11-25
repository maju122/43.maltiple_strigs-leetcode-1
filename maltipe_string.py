class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                
                product = d1 * d2
                p1, p2 = i + j, i + j + 1
                total = product + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        # Skip any leading zero and convert digits back to string
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return "".join(str(d) for d in res[start:])
