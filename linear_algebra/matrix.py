"""
Created on 16/09/2025
Contains Matrix class
"""

class Matrix:
    """
    Matrix class
    """
    def __init__(self, elements: list[list]) -> None:
        """

        :param elements: numeric values of the matrix
        :param shape: the shape of the matrix in (rows, columns)
        """
        self.elements = elements
        self.shape = (len(elements), len(elements[0]))


    def __str__(self) -> str:
        return f"Vector: {self.elements}"
