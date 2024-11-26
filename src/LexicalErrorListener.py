from antlr4.error.ErrorListener import ErrorListener

class LexicalErrorListener(ErrorListener):
    """
    A custom error listener for handling lexical errors during the tokenization phase.

    Extends:
        antlr4.error.ErrorListener.ErrorListener
    """

    def __init__(self):
        """
        Initializes the LexicalErrorListener with an empty list to store lexical errors.
        """
        super().__init__()
        self.errors = []

    def lexical_error(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Records a lexical error with details about its location and description.

        Args:
            recognizer: The lexer instance that detected the error.
            offendingSymbol: The invalid character or token that caused the error.
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.
            msg (str): A description of the lexical error.
            e: The exception associated with the lexical error (if any).

        Appends a formatted error message to the list of lexical errors.
        """
        error_message = (
            f"❌ Oops! Lexical Error:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)

    def has_errors(self):
        """
        Checks if any lexical errors were recorded.

        Returns:
            bool: True if there are lexical errors, False otherwise.
        """
        return len(self.errors) > 0

    def get_errors(self):
        """
        Retrieves the list of recorded lexical errors.

        Returns:
            list: A list of formatted lexical error messages.
        """
        return self.errors
