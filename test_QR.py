"""Tests functions in QR.py
"""


import pytest
import QR


def test_gram_schmidt_unstable():
    """Test QR.gram_schmidt_unstable()
    """
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce Q=[[1, 0], [0, 1]] R=[[1, 0], [1, 1]
    assert QR.gram_schmidt_unstable([[1, 0], [1, 1]]) == [[[1, 0], [0, 1]],
                                                          [[1, 0], [1, 1]]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce Q=[[1, 0], [0, -1] R=[[1, 0], [-3, 3]]
    assert QR.gram_schmidt_unstable([[1, 0], [-3, -3]]) == [[[1, 0], [0, -1]],
                                                            [[1, 0], [-3, 3]]]

def test_gram_schmidt():
    """Test QR.gram_schmidt()
    """
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce Q=[[1, 0], [0, 1]] R=[[1, 0], [1, 1]
    assert QR.gram_schmidt([[1, 0], [1, 1]]) == [[[1, 0], [0, 1]],
                                                 [[1, 0], [1, 1]]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce Q=[[1, 0], [0, -1] R=[[1, 0], [-3, 3]]
    assert QR.gram_schmidt([[1, 0], [-3, -3]]) == [[[1, 0], [0, -1]],
                                                   [[1, 0], [-3, 3]]]


# Run tests if file is run directly
if __name__ == "__main__":
    pytest.main(['test_QR.py'])
