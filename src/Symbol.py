class Symbol:
    
    def __init__(self, name, type, mutable, value):
        
        """
        Initializes a new variable object.

        Args:
            name (str): The name of the variable.
            type (str): The data type of the variable (e.g., "Int", "String").
            mutable (bool): A flag indicating whether the variable is mutable.
            value (any): The initial value of the variable.
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
        
        return f"Symbol(name={self.name}, type={self.type}, value={self.value}, mutable={self.mutable})"
