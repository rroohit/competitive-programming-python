def strStr(haystack: str, needle: str) -> int:
    ans = -1

    for i in range(len(haystack)):
        if i + len(needle) <= len(haystack):
            hay = (haystack[i:i+len(needle)])
            if hay == needle:
                ans = i
                break

    return ans


haystack_str = "a"
needle_str = "a"

print(strStr(haystack_str, needle_str))
