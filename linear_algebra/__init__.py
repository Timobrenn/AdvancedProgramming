from . import matrix
from . import vector

Vector = vector.Vector
Matrix = matrix.Matrix

# This is what you get when you write:
# from linear_algebra import *
__all__ = [Vector, Matrix]