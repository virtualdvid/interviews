"""Slow Sums
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: 
Choose any two numbers and replace them with their sum. Moreover, 
we associate a penalty with each operation equal to the value of the new number, 
and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, 
which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. 
The goal in this problem is to find the highest possible penalty for a given input.
Signature:
int getTotalTime(int[] arr)
Input:
An array arr containing N integers, denoting the numbers in the list.
Output format:
An int representing the highest possible total penalty.
Constraints:
1 ≤ N ≤ 10^6
1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
The sum of values of N over all test cases will not exceed 5 * 10^6.
Example
arr = [4, 2, 1, 3]
output = 26
First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
Add 9 + 1 for a penalty of 10. The penalties sum to 26."""


def getTotalTime(arr: list) -> int:
  """Gets the max penalty

  Args:
      arr (list): list of integers to evaluate

  Returns:
      int: max penalty found
  """
  output = 0
  if len(arr) == 1:
      return arr[0]
  while len(arr) > 1:
    # use pop property to extract the max number of the array twice
    penalty = arr.pop(arr.index(max(arr))) + arr.pop(arr.index(max(arr)))
    arr.append(penalty)
    output += penalty
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
  ARR_1 = [4, 2, 1, 3]
  EXPECTED_1 = 26
  OUTPUT_1 = getTotalTime(ARR_1)
  check(EXPECTED_1, OUTPUT_1)

  ARR_2 = [2, 3, 9, 8, 4]
  EXPECTED_2 = 88
  OUTPUT_2 = getTotalTime(ARR_2)
  check(EXPECTED_2, OUTPUT_2)
