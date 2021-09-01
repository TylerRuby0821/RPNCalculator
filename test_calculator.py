import pytest
import calculator

def test_for_accurate_answer():
  assert calculator.calculate("8 2 +") == 10
