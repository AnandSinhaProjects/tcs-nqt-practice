'''

Max Sum without Adjacents
Easy Accuracy: 54.99% Submissions: 18913 Points: 2

Given an array Arr of size N containing positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array.

Example 1:

Input:
N = 6
Arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: If you take indices 0, 3
and 5, then Arr[0]+Arr[3]+Arr[5] =
5+100+5 = 110.

Example 2:

Input:
N = 4
Arr[] = {3, 2, 7, 10}
Output: 13
Explanation: 3 and 10 forms a non
continuous  subsequence with maximum
sum.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 106
1 ≤ Arri ≤ 107
'''

def max_sum(arr,n):
    if n==1:
        return arr[0]
    if n==2:
        return max(arr[0],arr[1])
    first = int(arr[0])
    second = int(arr[1])
    curr = 0
    for i in range(2,n):
        curr = max(first + arr[i],second)
        first = second 
        second = curr
    return curr

if __name__ == '__main__':
    n = int(input())
    l = list(map(int,input().split()))
    print(max_sum(l,n))