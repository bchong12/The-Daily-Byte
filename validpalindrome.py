import collections

#Time: O(n + 26) Space: O(26)

def palindrome(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetMap = collections.Counter(alphabet)
    p1, p2 = 0, len(string) - 1
    string = string.lower()
    while p1 <= p2:
        if string[p1] not in alphabetMap:
            p1+=1
            continue
        elif string[p2] not in alphabetMap:
            p2-=1
            continue
        if string[p1] != string[p2]: return False
        p1+=1
        p2-=1
    
    return True

print(palindrome("A man, a plan, a canal: Panama."))
