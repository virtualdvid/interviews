"""Return Mismatched Words
Given an input of two strings consisting of english letters (a-z; A-Z) and spaces,
complete a function that returns a list containing all the mismatched words (case sensitive) between them.
You can assume that a word is a group of characters delimited by spaces.
A mismatched word is a word that is only in one string but not the other.
Add mismatched words from the first string before you add mismatched words from the second string in the output array.

Signature
static String[] returnMismatched(String str1, String STR2)
Input
str1: a string
str2: a string
Note: You can only expect valid english letters (a-z; A-Z) and spaces.
Output
An array containing all words that do not match between str1 and str2.
Examples
str1: "Firstly this is the first string"
str2: "Next is the second string"
output: ["Firstly", "this", "first", "Next", "second"]

str1: ""
str2: ""
output: []

str1: ""
str2: "This is the second string"
output: ["This","is","the","second","string"]

str1: "This is the first string"
str2: "This is the second string"
output: ["first", "second"]

str1: "This is the first string extra"
str2: "This is the second string"
output: ["first", "second", "extra"]

str1: "This is the first text"
str2: "This is the second string"
output: ["first", "text", "second", "string"]"""


def return_mismatched_words(str1: str, str2: str) -> list:
  """Returns mismatched words

  Args:
      str1 (str): first phrase
      str2 (str): second phrase

  Returns:
      list: list of mismatched words
  """
  str1_list = str1.split(' ')
  str2_list = str2.split(' ')
  union = str1_list + str2_list
  symetric_diff = list(set(str1_list) ^ set(str2_list))
  stage = [i for i in union if i in symetric_diff]
  return stage

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printStringList(array):
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
    printStringList(expected)
    print(' Your output: ', end='')
    printStringList(output)
    print()
  TEST_CASE_NUMBER += 1

if __name__ == "__main__":
  # Testcase 1
  STR1 = "Firstly this is the first string"
  STR2 = "Next is the second string"
  OUTPUT_1 = return_mismatched_words(STR1, STR2)
  EXPECTED_1 = ["Firstly", "this", "first", "Next", "second"]
  check(EXPECTED_1, OUTPUT_1)

  # Testcase 2
  STR1 = "This is the first string"
  STR2 = "This is the second string"
  OUTPUT_3 = return_mismatched_words(STR1, STR2)
  EXPECTED_3 = ["first", "second"]
  check(EXPECTED_3, OUTPUT_3)

  # Testcase 3
  STR1 = "This is the first string extra"
  STR2 = "This is the second string"
  output_4 = return_mismatched_words(STR1, STR2)
  expected_4 = ["first", "second", "extra"]
  check(expected_4, output_4)

  # Testcase 4
  STR1 = "This is the first text"
  STR2 = "This is the second string"
  output_5 = return_mismatched_words(STR1, STR2)
  expected_5 = ["first", "text", "second", "string"]
  check(expected_5, output_5)
