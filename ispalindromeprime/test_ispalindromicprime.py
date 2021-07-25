import os,sys
sys.path.append(os.getcwd())
from ispalindromeprime import ispalindromicprime
import pytest


@pytest.mark.parametrize('m, result',[
	(10, False), (2, True),
	(727, True), (98, False),
	(405, False), (151, True),
	(313, True), (0, False)
])
def test_ishappynumber(m, result):
    assert ispalindromicprime(m) == result