from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # 'offendingSymbol' contains an invalid character
        error_message = (
            f"❌ Oops! Syntax Error Detected:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors
