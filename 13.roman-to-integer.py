class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": -2, "IX": -2, "XL": -20,
                 "XC": -20, "CD": -200, "CM": -200}
        for i in range(len(s) - 1):
            if s[i] + s[i + 1] in trans.keys():
                answer = answer + trans[s[i]] + trans[s[i] + s[i + 1]]
            else:
                answer = answer + trans[s[i]]
        answer = answer + trans[s[-1]]
        return answer

    """
    Runtime: 128 ms, faster than 95.13% of Python3 online submissions for Roman to Integer
    good job!
    i use dict to transfer roman to integer,in every character in string, i in the same time check if s[i]+s[i+1] is
    a special case(IV,IX.....),then i simply subtract these special case's effect, like if IV exist, the value will be 2
    less, because we plus 5 and 1,but it in fact means 4, so 2 should be subtracted from the value to make it right
    """
