class Symbol:
    def __init__(self, name, type, mutable, value):
        """
        Represents a symbol in the symbol table, such as a variable or a function.

        Args:
            name (str): The name of the symbol (e.g., variable or function name).
            type (str): The type of the symbol (e.g., 'Int', 'String', 'Boolean').
            value (optional): The value of the symbol, if applicable. Defaults to None.
        """
        self.name = name
        self.type = type
        self.mutable = mutable
        self.value = value


    def __repr__(self):
        """
        Returns a string representation of the Symbol object, useful for debugging.

        Returns:
            str: A string in the format 'Symbol(name=<name>, type=<type>, value=<value>)'.
        """
        return f"Symbol(name={self.name}, type={self.type}, value={self.value})"
