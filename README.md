# Find Peaks Function 🏔️

## Overview 🌟

This Python module contains a function, `find_peaks`, that identifies peaks in a list of numerical values. A peak is defined as an element that is greater than its immediate neighbors.

## Why I Focused on Pylint 10/10 📝

In writing this code, I aimed for a **Pylint score of 10/10** to ensure high code quality and maintainability. Here are some key reasons for this focus:

- **Readability** 📖: Clear and well-documented code helps others (and my future self) understand the functionality quickly.
- **Error Reduction** ❌: Following best practices and type hints helps catch potential bugs before they happen.
- **Collaboration** 🤝: High-quality code is easier for others to work with, making collaboration smoother.
- **Learning Experience** 📚: Striving for a perfect score challenged me to improve my coding skills and adhere to industry standards.

## What the Code Does ⚙️

The `find_peaks` function performs the following:

1. **Input**: Accepts a list of integers or floats.
2. **Processing**: Iterates through the list to find elements that are greater than their neighbors.
3. **Output**: Returns a list of peak values.

### Example Usage 📊

```python
# Example input
data = [1, 3, 2, 4, 5, 1, 0, 6]

# Finding peaks
peaks = find_peaks(data)

# Output: [3, 5, 6]
print(peaks)
