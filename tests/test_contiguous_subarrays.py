import pytest
from meta.coding.contiguous_subarrays import count_subarrays


def test_count_subarrays() -> None:
  input_1 = [3, 4, 1, 6, 2]
  output_1 = count_subarrays(input_1)
  assert output_1 == [1, 3, 1, 5, 1]

  imput_2 = [2, 4, 7, 1, 5, 3]
  output_2 = count_subarrays(imput_2)
  assert output_2 == [1, 2, 6, 1, 3, 1]

  imput_3 = []
  output_3 = count_subarrays(imput_3)
  assert output_3 == []


def test_count_subarrays_wrong_parameter() -> None:
  pass
  # imput_1 = 'a'
  # output_1 = count_subarrays(imput_1)
  # assert output_1 == []

  # with pytest.raises(TypeError):
  #   output_error = count_subarrays('a')
