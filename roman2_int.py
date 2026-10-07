class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Check if this is a subtraction case
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total    

# FUNCTION romanToInt(s): # type: ignore
#     roman_map = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50,
#         'C': 100, 'D': 500, 'M': 1000
#     }
#     total = 0
#     n = LENGTH(s)

#     FOR i FROM 0 TO n - 1 DO
#         current_val = roman_map[s[i]]

#         // If next symbol is larger, subtract current value
#         IF i + 1 < n AND current_val < roman_map[s[i + 1]] THEN
#             total = total - current_val
#         ELSE
#             total = total + current_val
#         END IF
#     END FOR

#     RETURN total
# END FUNCTION       