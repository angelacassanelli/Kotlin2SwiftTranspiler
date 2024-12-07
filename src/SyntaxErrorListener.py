from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    """
    A custom error listener for handling syntax errors during the parsing phase.

    Extends:
        antlr4.error.ErrorListener.ErrorListener
    """

    def __init__(self):
        """
        Initializes the SyntaxErrorListener with an empty list to store syntax errors.
        """
        super().__init__()
        self.errors = []


    def syntax_error(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Called by ANTLR when a syntax error is encountered during parsing.

        Args:
            recognizer: The parser instance that detected the error.
            offendingSymbol: The invalid token that caused the error (if applicable).
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.
            msg (str): A description of the syntax error.
            e: The exception associated with the syntax error (if any).

        Appends a formatted error message to the list of syntax errors.
        """
        error_message = (
            f"❌ Oops! Syntax Error Detected:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)


    def has_errors(self):
        """
        Checks if any syntax errors were recorded.

        Returns:
            bool: True if there are syntax errors, False otherwise.
        """
        return len(self.errors) > 0


    def get_errors(self):
        """
        Retrieves the list of recorded syntax errors.

        Returns:
            list: A list of formatted syntax error messages.
        """
        return self.errors
