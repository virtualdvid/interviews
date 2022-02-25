from meta.coding.contiguous_subarrays import count_subarrays


def test_count_subarrays() -> None:
  imput_1 = [3, 4, 1, 6, 2]
  output_1 = count_subarrays(imput_1)
  assert output_1 == [1, 3, 1, 5, 1]

  imput_2 = [2, 4, 7, 1, 5, 3]
  output_2 = count_subarrays(imput_2)
  assert output_2 == [1, 2, 6, 1, 3, 1]