class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        else:
            i = j = 0
            next_nee = self.next(needle)
            len_hay = len(haystack)
            len_nee = len(needle)
            while i < len_hay and j < len_nee:
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = next_nee[j]
        if j == len_nee:
            return i - j
        else:
            return -1

    # function to calculate PMT of a string
    def next(self, string):
        len_str = len(string)
        if len_str == 0:
            return None
        elif len_str == 1:
            return [0]
        else:
            i = 2
            next_str = [-1, 0]  #note next[0]=-1 in fact helps to simplify the if sentences,it doesn't mean much
            j = 0
            while 1 < i < len_str:
                if string[i-1] == string[j] or j == -1: #here j==-1 helps next j+=1 to go back to the start of needle
                    i += 1
                    j += 1
                    next_str.append(j)
                else:
                    j = next_str[j]

        return next_str

    """
    Runtime: 76 ms, faster than 8.39% of Python3 online submissions for Implement strStr().
    we implement the kmp algorithm on python,that's why it is a little slow(not implemented on C)
    the basic idea of kmp is that you first get the PMT(partial match table) of your needle, PMT
    measures the longest identical prefix and suffix in a string, like "aa", PM is 1(don't consider the
    whole string),like "abab", PM is 2. as we know the PMT of the whole string(each string is haystack[0:i-1],
    if this place doesn't match, no need to go to i+1 and reexamine j from 0, because we know next(j)(which is PM
    of needle[0:j-1],so we only need to examine haystack[i] and needle[next[j]], for instance, if now first four
    characters of a needle "ababa" has matched with prat of haystack, but the fifth doesn't match, then we just need
    to compare needle[2](which is next[5]) with same unmatched haystack[j], this is because only ab can match the same
    place of the stack. furthermore ,if an unrepeated needle like "abcd", and abc has matched,but d doesn't, then we
    can konw that the needle can be slided to 3places right because we know if it just slide 1 place, as "a" in needle
    now meet "b" in stack, they will never match.

    if using python's own function, the code will simply be
     return haystack.find(needle)
    """

