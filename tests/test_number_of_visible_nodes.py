from meta.coding.number_of_visible_nodes import TreeNode, visible_nodes


class TestVisibleNodes:
  def setup_class(self) -> None:
      print('setting up')


  def test_visible_nodes_tree_1(self) -> None:
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    output_1 = visible_nodes(root)
    assert output_1 == 4


  def test_visible_nodes_tree_1(self) -> None:
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(15)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    root.right.left =TreeNode(14)
    root.right.right = TreeNode(16)
    output_2 = visible_nodes(root)
    assert output_2 == 5


  def teardown_class(self) -> None:
      print('tearing down')
