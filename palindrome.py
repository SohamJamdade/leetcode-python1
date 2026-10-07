class Solution:

  def isPalindrome(self, x):
    if x<0 or (x % 10 ==0 and x !=0):
      return False

    reversed_half = 0

    while x > reversed_half:
      reversed_half =reversed_half * 10 + (x % 10)
      x = x // 10   


# FUNCTION isPalindrome(x):
#     // 1. Filter out impossible cases
#     IF x < 0 OR (x MOD 10 == 0 AND x != 0) THEN
#         RETURN FALSE
#     END IF

#     // 2. Initialize variable to store reversed digits
#     reversed_half = 0

#     // 3. Reverse the last half of the digits
#     WHILE x > reversed_half DO
#         last_digit = x MOD 10
#         reversed_half = (reversed_half * 10) + last_digit
#         x = x DIV 10
#     END WHILE

#     // 4. Compare the two halves
#     // - Even number of digits: both halves must match exactly (x == reversed_half)
#     // - Odd number of digits: drop the middle digit from reversed_half (x == reversed_half DIV 10)
#     RETURN (x == reversed_half) OR (x == reversed_half DIV 10)
# END FUNCTION