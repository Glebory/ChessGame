from Chessticles.Pieces.King import *

import unittest
import io
import sys
from contextlib import contextmanager

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class chessTest(unittest.TestCase):
    def test_king(self):
        king = King("black", "board", (0, 5))
        assert (1, 5) in King.check_valid_moves(king)
        assert (8, 4) not in King.check_valid_moves(king)
        pass


