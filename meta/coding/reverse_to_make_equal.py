"""Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A."""


def are_they_equal(array_a: list, array_b: list) -> bool:
  """Verifies if two arrays are equal

  Args:
      array_a (list): array A
      array_b (list): array B

  Returns:
      bool: verification
  """
  if not array_a or not array_b or len(array_a) > len(array_b):
    return False
  for i in array_a:
    output = True if i in array_b else False
  return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  TEST_CASE_NUMBER += 1

if __name__ == "__main__":
  N_1 = 4
  A_1 = [1, 2, 3, 4]
  B_1 = [1, 4, 3, 2]
  EXPECTED_1 = True
  OUTPUT_1 = are_they_equal(A_1, B_1)
  check(EXPECTED_1, OUTPUT_1)

  N_2 = 4
  A_2 = [1, 2, 3, 4]
  B_2 = [1, 2, 3, 5]
  EXPECTED_2 = False
  OUTPUT_2 = are_they_equal(A_2, B_2)
  check(EXPECTED_2, OUTPUT_2)
