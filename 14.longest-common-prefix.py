class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # return the next new list to compare
        def next_list(a):
            return a[1:]

        # get the first character of every string
        def this_char(a):
            return a[0]

        c = ""

        len_str = min(list(map(len, strs)))  # return the minimun length of string

        for i in range(len_str):
            a = list(map(this_char, strs))
            if min(list(map(ord, a))) == max(list(map(ord, a))):
                c=c + a[0]
                strs = list(map(next_list, strs))
            else:
                break
        return c

   """
   Runtime: 48 ms, faster than 48.74% of Python3 online submissions for Longest Common Prefix.
   note: all the code runtime are concentrated upon 30 to 40 ms
   the little defaults  here is that instead of compare each string one by one, i simply use map to get all their
   first character and transform them to Assic numbers, the use min and max to check if they are all equal.
   This method will cost more time compared with use a simple min_str and compare it with the strings in list one by
   one.
   further more, using map may cost more time ,and since a crated more space to save different list, it also cost more
   space.
   """

   