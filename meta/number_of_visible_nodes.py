"""Number of Visible Nodes
There is a binary tree with N nodes. 
You are viewing the tree from its left side and can see only the leftmost nodes at each level. 
Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. 
The leftmost node at a level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, 
and the value of each node is between 0 and 1,000,000,000
Output
An int representing the number of visible nodes.
Example
            8  <------ root
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13            
output = 4"""

class TreeNode: 
  def __init__(self, key: int) -> None: 
    self.left = None
    self.right = None
    self.val = key 

def visible_nodes(root: TreeNode, level: int = 0, stage_level: set = set()) -> int:
  """Runs left side in a tree

  Args:
      root (TreeNode): tree object
      level (int, optional): tree level. Defaults to 0.
      stage_level (set, optional): set of levels. Defaults to set().

  Returns:
      int: [description]
  """
  if level == 0:
    stage_level.add(level)
    level += 1
    if root.left:
      stage_level.add(level)
      visible_nodes(root.left, level)
  else:
    level += 1
    if root.left:
      stage_level.add(level)
      visible_nodes(root.left, level)
    if root.right:
      stage_level.add(level)
      visible_nodes(root.right, level)
  return len(stage_level)
  
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
  ROOT_1 = TreeNode(8)
  ROOT_1.left = TreeNode(3)
  ROOT_1.right = TreeNode(10)
  ROOT_1.left.left = TreeNode(1)
  ROOT_1.left.right = TreeNode(6)
  ROOT_1.left.right.left = TreeNode(4)
  ROOT_1.left.right.right = TreeNode(7)
  ROOT_1.right.right = TreeNode(14)
  ROOT_1.right.right.left = TreeNode(13)
  EXPECTED_1 = 4
  OUTPUT_1 = visible_nodes(ROOT_1)
  check(EXPECTED_1, OUTPUT_1)

  ROOT_2 = TreeNode(10)
  ROOT_2.left = TreeNode(8)
  ROOT_2.right = TreeNode(15)
  ROOT_2.left.left = TreeNode(4)
  ROOT_2.left.left.right = TreeNode(5)
  ROOT_2.left.left.right.right = TreeNode(6)
  ROOT_2.right.left =TreeNode(14)
  ROOT_2.right.right = TreeNode(16)

  EXPECTED_2 = 5
  OUTPUT_2 = visible_nodes(ROOT_2)
  check(EXPECTED_2, OUTPUT_2)
