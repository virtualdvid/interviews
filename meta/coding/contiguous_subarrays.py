"""Contiguous Subarrays
You are given an array arr of N integers. For each index i,
you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]"""


def count_subarrays(arr: list) -> list:
  """Counts subarrays per each index in a given array

  Args:
      arr (list): array to evluate

  Returns:
      list: list of contiguous subarrays
  """
  # if not(isinstance(arr, list)):
  #   raise TypeError('Use a list of integers as input.')
  i = 0
  l = 1
  r = 1
  init = True
  result = []
  placeholder = []
  while i < len(arr):
    if init:
      placeholder.append(arr[i])
    # section to evaluate -> right direction
    if i + r < len(arr) and arr[i] > arr[i + r]:
      placeholder.append(arr[i:i+r+1])
      init = False
      r += 1
      bypass = False
    else:
      bypass = True
    # section to evaluate <- left direction
    if i - l >= 0 and arr[i] > arr[i - l]:
      placeholder.append(arr[i-l:i+1])
      init = False
      l += 1
      bypass = False
    else:
      bypass = True
    # section to collect len of subarrays found
    if bypass:
      result.append(len(placeholder))
      placeholder.clear()
      init = True
      i += 1
      l = 1
      r = 1
  return result


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

TEST_CASE_NUMBER = 1

def check(expected, output):
  global TEST_CASE_NUMBER
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', TEST_CASE_NUMBER, sep='')
  else:
    print(wrongTick, 'Test #', TEST_CASE_NUMBER, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  TEST_CASE_NUMBER += 1

if __name__ == "__main__":
  TEST_1 = [3, 4, 1, 6, 2]
  EXPECTED_1 = [1, 3, 1, 5, 1]
  OUTPUT_1 = count_subarrays(TEST_1)
  check(EXPECTED_1, OUTPUT_1)

  TEST_2 = [2, 4, 7, 1, 5, 3]
  EXPECTED_2 = [1, 2, 6, 1, 3, 1]
  OUTPUT_2 = count_subarrays(TEST_2)
  check(EXPECTED_2, OUTPUT_2)
