from antlr4.error.ErrorListener import ErrorListener

class LexicalErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # 'offendingSymbol' contains the invalid character
        error_message = (
            f"❌ Oops! Lexical Error:\n"
            f"   🔍 {msg}\n"
            f"   📍 line {line}, column {column}"
        )
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors
