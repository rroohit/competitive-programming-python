def lengthOfLastWord(s: str) -> int:
    isStartCount = False

    ans = 0

    for i in range(len(s)):
        if not isStartCount and s[-i-1] != ' ':
            isStartCount = True

        if isStartCount:
            if s[-i-1] != ' ':
                ans += 1
            else:
                break

    return ans


print(lengthOfLastWord("   fly me   to   the moon  "))
