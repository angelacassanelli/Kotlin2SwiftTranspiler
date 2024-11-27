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
            raise ValueError("❌ Cannot remove the global scope.")

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
    
    def lookup_symbol_in_current_scope(self, name):
        """Searches for a symbol in the current (topmost) scope.

        Args:
            name (str): The name of the symbol to search for.

        Returns:
            Symbol: The symbol if found, otherwise None.
        """
        current_scope = self.scopes[-1]  # Topmost scope
        return current_scope.get(name, None)

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
            raise ValueError(f"❌ Symbol '{name}' is already declared in the current scope.")
        current_scope[name] = symbol

    def update_symbol(self, name, new_value=None, new_type=None):
        """
        Updates an existing symbol in the active scopes.

        Args:
            name (str): The name of the symbol to update.
            new_value (optional): The new value to assign to the symbol.
            new_type (optional): The new type to assign to the symbol.

        Raises:
            ValueError: If the symbol does not exist in any active scope.
        """
        for scope in reversed(self.scopes):
            if name in scope:
                symbol = scope[name]
                if new_value is not None:
                    symbol.value = new_value
                if new_type is not None:
                    symbol.type = new_type
                return
        raise ValueError(f"❌ Variable '{name}' is not declared in any scope.")


    def __repr__(self):
        return f"SymbolTable(scopes={self.scopes})"
