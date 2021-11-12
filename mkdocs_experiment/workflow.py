""" Module to test mkdocs docstring extraction.

This is to see how mkdocs present documentation from Python code.
"""


from typing import List


def foo(fooz: str) -> List[str]:
    """Example of function documentation.

    Args:
        fooz: what to foo about

    Returns:
        List of foo magic strings
    """
    return [fooz]
