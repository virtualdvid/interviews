from meta.coding.largest_triple_products import findMaxProduct


def setup_function():
    print('setting up')


def test_find_max_product() -> None:
  input_1 = [1, 2, 3, 4, 5]
  output_1 = findMaxProduct(input_1)
  assert output_1 == [-1, -1, 6, 24, 60]

  imput_2 = [2, 4, 7, 1, 5, 3]
  output_2 = findMaxProduct(imput_2)
  assert output_2 == [-1, -1, 56, 56, 140, 140]


def teardown_function():
    print('tearing down')