from antlr4.error.ErrorListener import ErrorListener

class LexicalErrorListener(ErrorListener):

    """
    LexicalErrorListener:
        A custom error listener for handling lexical errors during ANTLR parsing.

        Inherits from the `ErrorListener` class of ANTLR to capture and store lexical errors 
        encountered during tokenization.

        Attributes:
            errors (list): A list that stores error messages related to lexical errors.
    """

    def __init__(self):

        """
        Initializes a new LexicalErrorListener.

        Sets up an empty list `errors` to store any lexical error messages detected during parsing.
        """

        super().__init__()
        self.errors = []
        

    def lexical_error(self, line, column, msg):

        """
        Callback method invoked when a lexical error is detected.
        Formats the error message and stores it in the `errors` list.


        Args:
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.
            msg (str): The error message describing the lexical issue.

        """

        error_message = (
            f"❌ Oops! Lexical Error Detected:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)


    def has_errors(self):

        """
        Checks if any lexical errors have been detected.

        Returns:
            bool: True if there are errors in the `errors` list, False otherwise.
        """

        return len(self.errors) > 0


    def get_errors(self):

        """
        Retrieves the list of lexical error messages.

        Returns:
            list: A list of error messages that have been captured by the listener.
        """

        return self.errors
