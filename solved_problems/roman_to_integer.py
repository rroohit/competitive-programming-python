def romanToInt(s: str) -> int:
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    visited_index = -1
    ans = 0

    for i in range(len(s)):
        if i == visited_index:
            continue

        if i + 1 < len(s):
            if roman_values[s[i]] > roman_values[s[i + 1]] or roman_values[s[i]] == roman_values[s[i + 1]]:
                ans += roman_values[s[i]]
            else:
                ans += (roman_values[s[i + 1]] - roman_values[s[i]])
                visited_index = i + 1

        else:
            ans += roman_values[s[i]]

    return ans


print(romanToInt("MCMXCIV"))  # ans => 1994
