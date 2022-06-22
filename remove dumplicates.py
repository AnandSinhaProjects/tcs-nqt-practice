'''

Remove duplicate elements from sorted Array
Easy Accuracy: 46.78% Submissions: 99149 Points: 2

Given a sorted array A[] of size N, delete all the duplicates elements from A[].
Note: Don't use set or HashMap to solve the problem.


Example 1:

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 1
Explanation: After removing all the duplicates 
only one instance of 2 will remain.

Example 2:

Input:
N = 3
Array = {1, 2, 2}
Output: 2


Your Task:  
You don't need to read input or print anything. Complete the function remove_duplicate() which takes the array A[] and its size N as input parameters and modifies it in place to delete all the duplicates. The function must return an integer X denoting the new modified size of the array. 
Note: The generated output will print all the elements of the modified array from index 0 to X-1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 104
1 ≤ A[i] ≤ 106
'''

n = int(input())
l = list(map(int, input().split()))
ln = []
[ln.append(x) for x in l if x not in ln]
print(ln)
print(len(ln))
