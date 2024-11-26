class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Stack: each level is a dictionary representing a scope.

    def add_scope(self):
        """Adds a new scope by appending an empty dictionary to the stack."""
        self.scopes.append({})

    def remove_scope(self):
        """Removes the current scope by popping the top dictionary from the stack.

        Raises:
            ValueError: If trying to remove the global scope (the last remaining scope).
        """
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise ValueError("Cannot remove the global scope.")

    def add_symbol(self, name, symbol):
        """Adds a symbol to the current scope.

        Args:
            name (str): The name of the symbol to add.
            symbol (Symbol): The symbol object containing information (e.g., type, value).

        Raises:
            ValueError: If the symbol already exists in the current scope.
        """
        current_scope = self.scopes[-1]
        if name in current_scope:
            raise ValueError(f"Symbol '{name}' already declared in the current scope.")
        current_scope[name] = symbol

    def lookup_symbol(self, name):
        """Searches for a symbol in the active scopes, starting from the current one.

        Args:
            name (str): The name of the symbol to search for.

        Returns:
            Symbol: The symbol if found, otherwise None.
        """
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None  # Not found

    def __repr__(self):
        return f"SymbolTable(scopes={self.scopes})"
