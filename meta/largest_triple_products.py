"""Largest Triple Products
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.
Signature
int[] findMaxProduct(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000].
Output
Return a list of n integers output[0..(n-1)], as described above.
Example 1
n = 5
arr = [1, 2, 3, 4, 5]
output = [-1, -1, 6, 24, 60]
The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.
Example 2
n = 5
arr = [2, 1, 2, 1, 2]
output = [-1, -1, 4, 4, 8]
The 3rd element of output is 2*2*1 = 4, the 4th is 2*2*1 = 4, and the 5th is 2*2*2 = 8."""


def findMaxProduct(arr: list) -> list:
  """Finds the max product in an array

  Args:
      arr (list): array of integers

  Returns:
      list: array with max products
  """
  result = []
  prod = lambda _arr: _arr[0] * _arr[1] * _arr[2]
  for i, _ in enumerate(arr):
    if i < 2:
      result.append(-1)
    elif i == 2:
      result.append(prod(arr))
    else:
      sorted_arr = sorted(arr[:i+1], reverse=True)
      result.append(prod(sorted_arr))
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
  rightTick = '\u2713 '
  wrongTick = '\u2717 '
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
  ARR_1 = [1, 2, 3, 4, 5]
  EXPECTED_1 = [-1, -1, 6, 24, 60]
  OUTPUT_1 = findMaxProduct(ARR_1)
  check(EXPECTED_1, OUTPUT_1)

  ARR_2 = [2, 4, 7, 1, 5, 3]
  EXPECTED_2 = [-1, -1, 56, 56, 140, 140]
  OUTPUT_2 = findMaxProduct(ARR_2)
  check(EXPECTED_2, OUTPUT_2)
