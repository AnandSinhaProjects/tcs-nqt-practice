'''

Palindrome String
Easy Accuracy: 50.77% Submissions: 95420 Points: 2

Given a string S, check if it is palindrome or not.

Example 1:

Input: S = "abba"
Output: 1
Explanation: S is a palindrome

Example 2:

Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome

 

Your Task:
You don't need to read input or print anything. Complete the function isPlaindrome()which accepts string S and returns an integervalue 1 or 0.


Expected Time Complexity: O(Length of S)
Expected Auxiliary Space: O(1)


Constraints:
1 <= Length of S<= 105

'''

s = input()
if s == s[::-1]:
    print('1')
else:
    print('0')