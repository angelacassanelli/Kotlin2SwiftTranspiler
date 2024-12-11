from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):

    """
    SyntaxErrorListener:
        A custom error listener for handling syntax errors during ANTLR parsing.

        Inherits from the `ErrorListener` class of ANTLR to capture and store lexical errors 
        encountered during parsing.

        Attributes:
            errors (list): A list that stores error messages related to syntax errors.
    """

    def __init__(self):

        """
        Initializes a new SyntaxErrorListener.

        Sets up an empty list `errors` to store any syntax error messages detected during parsing.
        """

        super().__init__()
        self.errors = []


    def syntax_error(self, line, column, msg):

        """
        Callback method invoked when a syntax error is detected.
        Formats the error message and stores it in the `errors` list.

        Args:
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.
            msg (str): The error message describing the syntax issue.

        """

        error_message = (
            f"❌ Oops! Syntax Error Detected:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)


    def has_errors(self):

        """
        Checks if any syntax errors have been detected.

        Returns:
            bool: True if there are errors in the `errors` list, False otherwise.
        """

        return len(self.errors) > 0


    def get_errors(self):

        """
        Retrieves the list of syntax error messages.

        Returns:
            list: A list of error messages that have been captured by the listener.
        """

        return self.errors
