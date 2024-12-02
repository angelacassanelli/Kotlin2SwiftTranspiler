class SymbolTable:
    def __init__(self):
        self.scopes = [{"variables": {}, "functions": {}, "classes": set()}] # Stack: each level is a dictionary representing a scope.


    def __repr__(self):
        return f"SymbolTable(scopes={self.scopes})"
    

    def add_scope(self):
        """Adds a new scope by appending an empty dictionary to the stack."""
        self.scopes.append({"variables": {}, "functions": {}, "classes": set()})


    def remove_scope(self):
        """Removes the current scope by popping the top dictionary from the stack.

        Raises:
            ValueError: If trying to remove the global scope (the last remaining scope).
        """
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise ValueError("❌ Cannot remove the global scope.")


    ##### Variables #####


    def lookup_variable(self, name):
        """Searches for a variable in the active scopes, starting from the current one.

        Args:
            name (str): The name of the variable to search for.

        Returns:
            variable: The variable if found, otherwise None.
        """
        for scope in reversed(self.scopes):
            if name in scope["variables"]:
                return scope["variables"][name]
        return None # not found
    

    def lookup_variable_in_current_scope(self, name):
        """Searches for a variable in the current (topmost) scope.

        Args:
            name (str): The name of the variable to search for.

        Returns:
            variable: The variable if found, otherwise None.
        """
        current_scope = self.scopes[-1]["variables"]  # Topmost scope
        return current_scope.get(name, None)


    def add_variable(self, name, variable):
        """Adds a variable to the current scope.

        Args:
            name (str): The name of the variable to add.
            variable (variable): The variable object containing information (e.g., type, value).

        Raises:
            ValueError: If the variable already exists in the current scope.
        """
        current_scope = self.scopes[-1]["variables"]
        if name in current_scope:
            raise ValueError(f"❌ Variable '{name}' is already declared in the current scope.")
        current_scope[name] = variable
        print(f"Variable '{name}' added to the current scope.")


    def update_variable(self, name, new_value):
        """
        Updates an existing variable in the active scopes.

        Args:
            name (str): The name of the variable to update.
            new_value (optional): The new value to assign to the variable.
            new_type (optional): The new type to assign to the variable.

        Raises:
            ValueError: If the variable does not exist in any active scope.
        """
        for scope in reversed(self.scopes):
            if name in scope["variables"]:
                scope["variables"][name].value = new_value
                return
        raise ValueError(f"❌ Variable '{name}' is not declared in any scope.")


    def get_variable_info(self, name):
        """
        Retrieves the type and mutability of a variable by its name.

        Args:
            name (str): The name of the variable.

        Returns:
            tuple: A tuple (type, mutable) if the variable exists, otherwise None.
        """
        variable = self.lookup_variable(name)
        if not variable:
            raise ValueError(f"❌ Variable '{name}' is not declared in any scope.")
        return variable.type, variable.mutable
    
    
    def get_variable_assigned(self, name):
        """
        Checks if the specified variable is declared and assigned.

        Args:
            name (str): The name of the variable.

        Returns:
            bool: True if the variable is declared and assigned, False otherwise.

        Raises:
            ValueError: If the variable is not declared in any scope.
        """
        variable = self.lookup_variable(name)
        if not variable:
            raise ValueError(f"❌ Variable '{name}' is not declared in any scope.")
        return variable.value is not None


    ##### Functions #####


    def lookup_function(self, name, param_types):
        """Searches for a function in the active scopes, starting from the current one.

        Args:
            name (str): The name of the function to search for.

        Returns:
            function: The function if found, otherwise None.
        """
        for scope in reversed(self.scopes):
            if name in scope["functions"]:
                for fun in scope["functions"][name]:
                    if fun["param_types"] == param_types:
                        return fun
        return None


    def add_function(self, name, param_types, return_type):
        """Adds a function to the current scope.

        Args:
            name (str): The name of the function to add.
            function (function): The function object containing information (e.g., type, value).

        Raises:
            ValueError: If the function already exists in the current scope.
        """
        current_scope = self.scopes[-1]["functions"]
        
        if name not in current_scope:
            current_scope[name] = []

        for fun in current_scope[name]:
            if fun["param_types"] == param_types:
                raise ValueError(f"❌ function '{name}' with signature '{param_types}' is already declared in current scope.")
        current_scope[name].append({"param_types": param_types, "return_type": return_type})
        print(f"Function '{name}' added to the current scope.")


    def get_function_return_type(self, name, param_types):
        """
        Retrieves the return type of a function by its name and parameter types.

        Args:
            name (str): The name of the function.
            param_types (list): The list of parameter types of the function.

        Returns:
            str: The return type of the function.

        Raises:
            ValueError: If the function is not found in any scope.
        """
        for scope in reversed(self.scopes):
            if name in scope["functions"]:
                for fun in scope["functions"][name]:
                    if fun["param_types"] == param_types:
                        return fun["return_type"]
        raise ValueError(f"❌ Function '{name}' with parameters {param_types} is not declared in any scope.")


    ##### Classes #####


    def add_class(self, name):
        """
        Adds a class to the current scope.

        Args:
            name (str): The name of the class.

        Raises:
            ValueError: If the class already exists in the current scope.
        """
        current_scope = self.scopes[-1]["classes"]
        if name in current_scope:
            raise ValueError(f"❌ Class '{name}' is already declared in the current scope.")
        current_scope.add(name)
        print(f"Class '{name}' added to the current scope.")


    def lookup_class(self, name):
        """
        Searches for a class in the active scopes, starting from the current one.

        Args:
            name (str): The name of the class to search for.

        Returns:
            bool: True if the class exists, False otherwise.
        """
        for scope in reversed(self.scopes):
            if name in scope["classes"]:
                return True
        return False