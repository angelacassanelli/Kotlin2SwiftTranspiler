class Symbol:

    """
    Represents a symbolic variable in the context of the symbol table.

    The `Symbol` class stores information about a variable, including its name, data type, 
    mutability, and value. It is used to track variables across scopes during semantic analysis.

    Attributes:
        name (str): The name of the variable.
        type (str): The data type of the variable (e.g., "Int", "String").
        mutable (bool): Indicates whether the variable is mutable.
        value (any): The current value of the variable, which can be `None` if not assigned.
    """
    
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
