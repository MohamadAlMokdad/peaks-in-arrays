"""
This module provides a function to find peaks in a list of numerical values.

A peak is defined as an element that is greater than its immediate neighbors.
"""
from typing import List, Union
def find_peaks(array: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Find peaks in a list of numerical values.

    A peak is defined as an element that is greater than its immediate neighbors.

    """
    if not isinstance(array, list):
        raise ValueError("Input must be a list.")
    peaks = []
    if len(array) < 3:
        return peaks  # Not enough elements to have peaks
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(array[i])

    return peaks
