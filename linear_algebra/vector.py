"""
Created on 16/09/2025
Contains Vector class
"""

class Vector:
    """
    Vector class
    """
    def __init__(self, elements: list) -> None:
        self.elements = elements

    def __str__(self) -> str:
        return f"Vector: {self.elements}"