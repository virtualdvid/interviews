"""Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; 
that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, 
even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 
(the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements)."""


def numberOfWays(arr: list, k: int) -> int:
  """calculates the number of pairs in a given array

  Args:
      arr (list): list of integers to evaluate
      k (int): target pair sum value

  Returns:
      int: total different pairs found in the array
  """
  i = 0
  output = 0
  arr.sort()
  for i, value in enumerate(arr):
    if value > k: break
    target = k - value
    output += arr[i+1:].count(target)
  return output


def numberOfWays2(arr: list, k: int) -> int:
  """calculates the number of pairs in a given array

  Args:
      arr (list): list of integers to evaluate
      k (int): target pair sum value

  Returns:
      int: total different pairs found in the array
  """
  i = 0
  l = 1
  output = 0
  arr.sort()
  while i < len(arr):
    if arr[i] > k:
      break
    if i + l < len(arr) and arr[i] + arr[i + l] == k:
      output += 1
    if i + l == len(arr) or arr[i] + arr[i + l] > k:
      i += 1
      l = 0
    l += 1
  return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

TEST_CASE_NUMBER = 1

def check(expected, output):
  global TEST_CASE_NUMBER
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713 '
  wrongTick = '\u2717 '
  if result:
    print(rightTick, 'Test #', TEST_CASE_NUMBER, sep='')
  else:
    print(wrongTick, 'Test #', TEST_CASE_NUMBER, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  TEST_CASE_NUMBER += 1

if __name__ == "__main__":
  K_1 = 6
  ARR_1 = [1, 2, 3, 4, 3]
  EXPECTED_1 = 2
  OUTPUT_1 = numberOfWays(ARR_1, K_1)
  check(EXPECTED_1, OUTPUT_1)

  K_2 = 6
  ARR_2 = [1, 5, 3, 3, 3]
  EXPECTED_2 = 4
  OUTPUT_2 = numberOfWays(ARR_2, K_2)
  check(EXPECTED_2, OUTPUT_2)
