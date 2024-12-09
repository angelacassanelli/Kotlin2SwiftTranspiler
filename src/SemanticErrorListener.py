from antlr4.error.ErrorListener import ErrorListener

class SemanticErrorListener:

    """
    SemanticErrorListener:
        A custom error listener for handling semantic errors.

        This class is used to capture and store semantic errors detected during parsing, 
        typically when a variable or function is used incorrectly according to the language's semantics.

        Attributes:
            errors (list): A list that stores error messages related to semantic errors.
    """

    def __init__(self):

        """
        Initializes a new SemanticErrorListener.

        Sets up an empty list `errors` to store any semantic error messages detected during analysis.
        """
 
        super().__init__()
        self.errors = []


    def semantic_error(self, line, column, msg):

        """
        Called when a semantic error is detected.

        Args:
            line (int): The line number where the error occurred.
            column (int): The column number where the error occurred.
            msg (str): The error message describing the semantic issue.

        Formats the error message and stores it in the `errors` list.
        """

        error_message = (
            f"❌ Oops! Semantic Error Detected:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)


    def has_errors(self):
       
        """
        Checks if any semantic errors have been detected.

        Returns:
            bool: True if there are errors in the `errors` list, False otherwise.
        """
 
        return len(self.errors) > 0


    def get_errors(self):
        
        """
        Retrieves the list of semantic error messages.

        Returns:
            list: A list of error messages that have been captured by the listener.
        """
        
        return self.errors
