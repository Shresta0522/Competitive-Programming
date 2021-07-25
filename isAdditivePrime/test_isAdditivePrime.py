import os,sys
sys.path.append(os.getcwd())
from isAdditivePrime import isAdditivePrime
import pytest


@pytest.mark.parametrize('m, result',[
	(7, True), (1, True),
	(2, True), (98, False),
	(13, False), (23, True),
	(29, True), (97, True)
])
def test_ishappynumber(m, result):
    assert isAdditivePrime(m) == result