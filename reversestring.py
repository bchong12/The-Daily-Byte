class Solution:
    #using slice method
    def reverseString(string):
        return string[::-1]
    #using backwards for loop using reverse
    def reverseString(string):
        res = ""
        for i in reversed(range(len(string))):
            res += string[i]
        return res
    reverseString("Hello World")

    