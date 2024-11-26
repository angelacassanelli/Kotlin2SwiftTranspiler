from antlr4.error.ErrorListener import ErrorListener

class SemanticErrorListener:
    """
    A custom error listener for handling semantic errors during the analysis phase.

    Unlike syntax errors, semantic errors occur when the structure of the code is 
    correct but its meaning or usage is invalid (e.g., using an undeclared variable).
    """

    def __init__(self):
        """
        Initializes the SemanticErrorListener with an empty list to store semantic errors.
        """
        super().__init__()
        self.errors = []

    def semantic_error(self, msg, line, column):
        """
        Records a semantic error with details about its location and description.

        Args:
            msg (str): A message describing the semantic error.
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.

        Appends a formatted error message to the list of semantic errors.
        """
        error_message = (
            f"❌ Oops! Semantic Error Detected:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)

    def has_errors(self):
        """
        Checks if any semantic errors were recorded.

        Returns:
            bool: True if there are semantic errors, False otherwise.
        """
        return len(self.errors) > 0

    def get_errors(self):
        """
        Retrieves the list of recorded semantic errors.

        Returns:
            list: A list of formatted semantic error messages.
        """
        return self.errors
