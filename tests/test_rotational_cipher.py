import pytest
from meta.coding.rotational_cipher import rotationalCipher, user


def test_rotational_cipher() -> None:
  input_1 = 'All-convoYs-9-be:Alert1.'
  rotation_factor_1 = 4
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  assert output_1 == 'Epp-gsrzsCw-3-fi:Epivx5.'

  input_2 = 'abcdZXYzxy-999.@'
  rotation_factor_2 = 200
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  assert output_2 == 'stuvRPQrpq-999.@'

  input_3 = 'abcdZXYzxy-999.@'
  rotation_factor_3 = 0
  output_3 = rotationalCipher(input_3, rotation_factor_3)
  assert output_3 == 'abcdZXYzxy-999.@'


def test_rotational_cipher_wrong_parameters() -> None:
  input_1 = 123
  rotation_factor_1 = 0
  with pytest.raises(TypeError):
    rotationalCipher(input_1, rotation_factor_1)

  input_2 = 'test'
  rotation_factor_2 = '0'
  with pytest.raises(TypeError):
    rotationalCipher(input_2, rotation_factor_2)

  input_3 = 123
  rotation_factor_3 = '0'
  with pytest.raises(TypeError):
    rotationalCipher(input_3, rotation_factor_3)


def test_user(monkeypatch):
  password = 'answer'
  rotation_factor = 5
  answers = iter([password, rotation_factor])
  monkeypatch.setattr('builtins.input', lambda _: next(answers))
  result = user()
  assert result == 'password encrypted: fsxbjw'