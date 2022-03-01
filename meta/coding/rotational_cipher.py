"""Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount.
Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?".
Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A),
and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0).
Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678"""


import string


def rotationalCipher(input: str, rotation_factor: int) -> str:
  """encripts string by a rotation factor

  Args:
      input (str): string to encrypt
      rotation_factor (int): rotator factor

  Returns:
      str: encrypted string
  """
  if not isinstance(input, str):
    raise TypeError('Input must be a string.')
  if not isinstance(rotation_factor, int):
    raise TypeError('Input must be a integer.')

  if not input or not rotation_factor:
    return input
  abc_lower = list(string.ascii_lowercase)
  abc_upper = list(string.ascii_uppercase)
  input = list(input)
  output = []
  for i in input:
    if i.islower():
      index = abc_lower.index(i)
      rotated_index = (index + rotation_factor) % len(abc_lower)
      output.append(abc_lower[rotated_index])
    elif i.isupper():
      index = abc_upper.index(i)
      rotated_index = (index + rotation_factor) % len(abc_upper)
      output.append(abc_upper[rotated_index])
    elif i.isdigit():
      output.append(str(int(i) + rotation_factor)[-1])
    else:
      output.append(i)
  return "".join(output)

def user():
  password = input('please provide password: ')
  rotation_factor = input('please provide rotational factor: ')
  output = rotationalCipher(password, rotation_factor)
  return f'password encrypted: {output}'


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

if __name__ == '__main__':
  INPUT_1 = 'All-convoYs-9-be:Alert1.'
  ROTATION_FACTOR_1 = 4
  EXPECTED_1 = 'Epp-gsrzsCw-3-fi:Epivx5.'
  OUTPUT_1 = rotationalCipher(INPUT_1, ROTATION_FACTOR_1)
  check(EXPECTED_1, OUTPUT_1)

  INPUT_2 = 'abcdZXYzxy-999.@'
  ROTATION_FACTOR_2 = 200
  EXPECTED_2 = 'stuvRPQrpq-999.@'
  OUTPUT_2 = rotationalCipher(INPUT_2, ROTATION_FACTOR_2)
  check(EXPECTED_2, OUTPUT_2)

  INPUT_3 = 'abcdZXYzxy-999.@'
  ROTATION_FACTOR_3 = 0
  EXPECTED_3 = 'abcdZXYzxy-999.@'
  OUTPUT_3 = rotationalCipher(INPUT_3, ROTATION_FACTOR_3)
  check(EXPECTED_3, OUTPUT_3)
