def debug(*args):
    """Prints the provided arguments as a space-separated string.

    Parameters:
        *args: Any number of arguments to be printed.

    Returns:
        None

    Example:
        >>> debug("Hello", "world", 42)
        Hello world 42
    """
    print(" ".join(map(str, args)))
    return
