"""Example of code."""


def hello(name: str) -> str:
    """Just an greetings example.

    Args:
        name (str): Name to greet.

    Returns:
        str: greeting message

    Examples:
        .. code:: python

            >>> hello("Mike")
            'Hello Mike!'
    """
    return f"Hello {name}!"
