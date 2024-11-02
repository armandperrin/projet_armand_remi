# my_module.py


def my_function():
    """This is a sample function.

    This function returns a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello, World!"


class MyClass:
    """This is a sample class.

    This class demonstrates how to define a class with methods.
    """

    def __init__(self, name):
        """Initialize the class with a name.

        Args:
            name (str): The name of the person.
        """
        self.name = name

    def greet(self):
        """Return a greeting message from the instance."""
        return f"Hello, {self.name}!"
