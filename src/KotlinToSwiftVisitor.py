from antlr4 import ParseTreeVisitor
from generated.antlr.KotlinParser import KotlinParser
from Symbol import Symbol
from Types import KotlinTypes
from Utils import KOTLIN_2_SWIFT_TYPES, RESERVED_KEYWORDS


class KotlinToSwiftVisitor(ParseTreeVisitor):
    
    """
    This class is responsible for translating Kotlin code into Swift. It uses a tree structure to parse Kotlin code 
    through an ANTLR parser, then converts various constructs into Swift. It also handles semantic checks, such as verifying
    duplicate declarations and ensuring the use of supported types.

    Attributes:
        symbol_table (SymbolTable): The symbol table that stores variables, functions, and classes.
        semantic_error_listener (SemanticErrorListener): A listener for semantic errors.
        kotlin_2_swift_types (dict): A mapping of Kotlin types to Swift types.
        reserved_keywords (set): A set of reserved keywords in Kotlin that cannot be used as identifiers.
    """


    def __init__(self, symbol_table, semantic_error_listener):
        """
        Initializes an instance of the Kotlin-to-Swift translator.

        This constructor sets the symbol table and semantic error listener for error checking
        and handling during translation. It also sets up dictionaries for type mapping and
        reserved keyword management.

        Args:
            symbol_table (SymbolTable): The symbol table that stores information about variables and their types.
            semantic_error_listener (SemanticErrorListener): An object that handles semantic errors, such as undeclared variables, type conflicts, etc.

        Attributes:
            symbol_table (SymbolTable): The symbol table used for managing variables and their types.
            semantic_error_listener (SemanticErrorListener): The object for listening to semantic errors.
            kotlin_2_swift_types (dict): A dictionary that maps Kotlin types to corresponding Swift types.
            reserved_keywords (list): A list of reserved keywords in Kotlin that cannot be used as variable or function names.
        """
        self.symbol_table = symbol_table
        self.semantic_error_listener = semantic_error_listener        
        self.kotlin_2_swift_types = KOTLIN_2_SWIFT_TYPES
        self.reserved_keywords = RESERVED_KEYWORDS


    def visit_program(self, ctx: KotlinParser.ProgramContext):        
        """
        Visits the program node in the Kotlin AST (Abstract Syntax Tree) and translates
        top-level statements into corresponding Swift code.

        This method iterates over the top-level statements of the Kotlin program, converts
        each statement into Swift code, and joins the results into a single Swift program.

        Args:
            ctx (KotlinParser.ProgramContext): The context object representing the program node in the Kotlin AST.

        Returns:
            str: The translated Swift code, with top-level statements joined into a single string.

        Raises:
            ValueError: If the program contains invalid top-level statements.
        """     
        print("🚀 Visiting Kotlin code...")
        print(f"    🔍 Visiting program: {ctx.getText()}")
        
        if(ctx.topLevelStatement()):
            statements = [self.visit_top_level_statement(stmt) for stmt in ctx.topLevelStatement()]
            return "\n".join(filter(None, statements)) # Joins non-empty strings with a newline separator.
        else:
            raise ValueError(f"    ❌ Invalid top level statement in program.")

    def visit_top_level_statement(self, ctx: KotlinParser.TopLevelStatementContext):
        """
        Handles different types of top-level statements in the Kotlin program and directs them 
        to the appropriate visit methods for further processing.

        This method checks the type of the top-level statement (e.g., class declaration or comment),
        and delegates to the corresponding method for further handling. If the statement type is 
        unrecognized, it prints an error message.

        Args:
            ctx (KotlinParser.TopLevelStatementContext): The context object representing the top-level statement 
                                                         in the Kotlin AST.

        Returns:
            str or None: The translated Swift code for the top-level statement, or None if the statement is unrecognized.

        Prints:
            An error message if the statement is unrecognized.
        """
        print(f"    🔍 Visiting top level statement: {ctx.getText()}")
        
        if ctx.classDeclaration():
            return self.visit_class_declaration(ctx.classDeclaration())
        elif ctx.commentStatement():
            return self.visit_comment_statement(ctx.commentStatement())     
        else: 
            print(f"    ❌ Unrecognized statement: {ctx.getText()}")
            return None


    def visit_class_declaration(self, ctx: KotlinParser.ClassDeclarationContext):
        """
        Converts a Kotlin class declaration into a Swift class declaration.

        This method processes a Kotlin class declaration and translates it into Swift syntax, 
        including the class name, properties, constructor, and class body. It also checks for 
        duplicate class declarations in the current scope and ensures that the class is added 
        to the symbol table for semantic analysis.

        The method handles:
        - Class properties (with optional values).
        - Constructor parameters and their default values.
        - Class body content (if available).
        
        If the class has properties, it generates property declarations, assignments, and 
        constructs an initializer method in Swift. If no properties are present, it generates 
        only the initializer method if parameters are specified, otherwise the class will be 
        declared without a constructor body.

        Args:
            ctx (KotlinParser.ClassDeclarationContext): The context object representing the class declaration 
                                                        in the Kotlin AST.

        Returns:
            str: The translated Swift code for the class declaration.

        Raises:
            ValueError: If properties in the class declaration are incorrectly formatted.

        Prints:
            An error message if the class has already been declared in the current scope.
        """
        print(f"    🔍 Visiting class declaration: {ctx.getText()}")

        class_name = self.visit_identifier(ctx.IDENTIFIER())

        if self.check_class_already_declared_in_current_scope(ctx = ctx, class_name=class_name):
            return None
        else:
            self.symbol_table.add_class(class_name)
            self.symbol_table.add_scope()

            propertyList = self.visit_property_list(ctx.propertyList()) if ctx.propertyList() else None
            constructor_params = self.visit_parameter_list(ctx.parameterList()) if ctx.parameterList() else None
            body = self.visit_class_body(ctx.classBody()) if ctx.classBody() else ""            
            
            has_parentheses = ctx.LEFT_ROUND_BRACKET() is not None and ctx.RIGHT_ROUND_BRACKET() is not None                    
            
            if propertyList: 
                properties_declarations = []
                properties_assignments = []
                constructor_params = []

                for property in propertyList:
                    values = property.split()

                    if len(values) == 4:
                        var_keyword, var_name, _, var_type = values
                        var_value = None
                    elif len(values) == 6:
                        var_keyword, var_name, _, var_type, _, var_value = values                    
                    else:
                        raise ValueError(f"    ❌ Invalid properties: {propertyList}")
    
                    properties_declarations.append(f"{var_keyword} {var_name}: {var_type}")
                    properties_assignments.append(f"self.{var_name} = {var_name}")
                    constructor_params.append(f"{var_name}: {var_type}" + (f" = {var_value}" if var_value is not None else ""))
    
                properties_declarations = "\n".join(properties_declarations)
                properties_assignments = "\n".join(properties_assignments)
                constructor_params = ", ".join(constructor_params)

                constructor = f"init({constructor_params}) {{\n{properties_assignments}\n}}"
                class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
                return f"{class_declaration} {{\n{properties_declarations}\n{constructor}\n{body}\n}}"
            
            elif constructor_params:
                constructor = f"init({constructor_params}) {{}}"
                class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
                return f"{class_declaration} {{\n{constructor}\n{body}\n}}"
            
            self.symbol_table.remove_scope()

            class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
            return f"{class_declaration} {{\n{body}\n}}"
    

    def visit_identifier(self, ctx: KotlinParser):
        """
        Handles identifiers in the Kotlin code, ensuring they are not reserved keywords.

        This method checks whether an identifier is a reserved keyword in Kotlin and raises an 
        error if the identifier conflicts with any keyword. It processes the identifier by 
        extracting its name from the given context and ensures that it can be safely used in 
        the translated Swift code.

        Args:
            ctx (KotlinParser): The context object representing the identifier in the Kotlin AST.

        Returns:
            str: The name of the identifier, if it is not a reserved keyword.

        Raises:
            ValueError: If the identifier is a reserved keyword in Kotlin.

        Prints:
            A message indicating the identifier being visited.
        """
        print(f"    🔍 Visiting identifier: {ctx.getText()}")
        
        identifier_name = ctx.getText()
        if identifier_name in self.reserved_keywords:
            raise ValueError(f"    ❌ '{identifier_name}' is a reserved keyword and cannot be used as an identifier.")
        return identifier_name
    

    def visit_property_list(self, ctx: KotlinParser.PropertyListContext):
        """
        Converts a list of Kotlin properties into Swift properties.

        This method iterates over a list of properties in a Kotlin class and translates each
        property into its corresponding Swift declaration using the `visit_property` method.
        It processes the entire property list and returns the converted list of properties 
        in Swift syntax.

        Args:
            ctx (KotlinParser.PropertyListContext): The context object representing the list of properties 
                                                    in the Kotlin AST.

        Returns:
            list: A list of strings representing the properties in Swift syntax.

        Prints:
            A message indicating the property list being visited.
        """
        print(f"    🔍 Visiting property list: {ctx.getText()}")
        
        return [self.visit_property(property) for property in ctx.property_()]


    def visit_property(self, ctx: KotlinParser.PropertyContext):
        """
        Converts a Kotlin property into a Swift property.

        This method processes a Kotlin property and translates it into the corresponding Swift 
        property declaration. It does so by delegating to the `visit_var_declaration` method 
        for further processing of the variable declaration associated with the property.

        Args:
            ctx (KotlinParser.PropertyContext): The context object representing the property 
                                                in the Kotlin AST.

        Returns:
            str: A string representing the Swift property declaration.

        Prints:
            A message indicating the property being visited.
        """
        print(f"    🔍 Visiting property: {ctx.getText()}")
        
        return self.visit_var_declaration(ctx.varDeclaration())
    

    def visit_parameter_list(self, ctx: KotlinParser.ParameterListContext):
        """
        Converts a list of Kotlin parameters into Swift parameters.

        This method processes a list of Kotlin parameters and converts them into a comma-separated 
        list of Swift parameters by delegating to the `visit_parameter` method for each parameter 
        in the list.

        Args:
            ctx (KotlinParser.ParameterListContext): The context object representing the parameter list 
                                                     in the Kotlin AST.

        Returns:
            str: A string representing the Swift parameter list, with each parameter separated by a comma.

        Prints:
            A message indicating the parameter list being visited.
        """
        print(f"    🔍 Visiting parameter list: {ctx.getText()}")
        
        return ", ".join([self.visit_parameter(param) for param in ctx.parameter()])


    def visit_parameter(self, ctx: KotlinParser.ParameterContext):
        """
        Converts a Kotlin parameter into a Swift parameter.

        This method processes a Kotlin parameter, extracting its name and type, and optionally 
        its default value if provided. It then converts the parameter into a Swift-compatible 
        format, with default values handled appropriately.

        Args:
            ctx (KotlinParser.ParameterContext): The context object representing the parameter 
                                                 in the Kotlin AST.

        Returns:
            str: A string representing the Swift parameter, with its name, type, and optional 
            default value (if applicable).

        Prints:
            A message indicating the parameter being visited.
        """
        print(f"    🔍 Visiting parameter: {ctx.getText()}")
        
        param_name = self.visit_identifier(ctx.IDENTIFIER())
        param_type = self.visit_type(ctx.type_()) 
        if (ctx.expression()):
            param_value = self.visit_expression(ctx.expression()) 
            return f"{param_name}: {param_type} = {param_value}"
        return f"{param_name}: {param_type}"


    def visit_class_body(self, ctx: KotlinParser.ClassBodyContext):
        """
        Handles the body of a Kotlin class, converting its statements into Swift code.

        This method processes the body of a Kotlin class, iterating over its statements (such as 
        variable declarations, function declarations, assignment statements, and comments), 
        converting them into their Swift equivalents. Unrecognized statements are logged as errors.

        Args:
            ctx (KotlinParser.ClassBodyContext): The context object representing the body of the Kotlin class 
                                                 in the AST.

        Returns:
            str: A string containing the converted Swift code for the class body, with each 
            statement separated by newlines.

        Raises:
            ValueError: If an invalid statement is encountered in the class body.

        Prints:
            A message indicating the class body being visited.
        """
        print(f"    🔍 Visiting class body: {ctx.getText()}")
        statements = []
        if ctx.children:
            for stmt in ctx.children:
                match stmt:
                    case KotlinParser.VarDeclarationContext():
                        statements.append(self.visit_var_declaration(stmt))
                    case KotlinParser.FunctionDeclarationContext():
                        statements.append(self.visit_function_declaration(stmt))
                    case KotlinParser.AssignmentStatementContext():
                        statements.append(self.visit_assignment_statement(stmt))
                    case KotlinParser.CommentStatementContext():
                        statements.append(self.visit_comment_statement(stmt))
                    case _:
                        print(f"    ❌ Unrecognized statement: {stmt.getText()}")
                        return ""
            # Join and return the non-empty statements
            return "\n".join(filter(None, statements))
        else:
            raise ValueError(f"    ❌ Invalid statement in class body.")


    def visit_var_declaration(self, ctx: KotlinParser.VarDeclarationContext):
        """
        Converts a Kotlin 'var' declaration to Swift, including type and optional initialization.

        This method processes a Kotlin variable declaration, converting it into the equivalent 
        Swift declaration. It handles both mutable and immutable variables, checks for type 
        mismatches and unsupported types, and validates initialization expressions. The resulting 
        Swift declaration is returned as a string, or None is returned if errors are encountered.

        Args:
            ctx (KotlinParser.VarDeclarationContext): The context object representing the variable declaration
                                                      in the Kotlin AST.

        Returns:
            str: A string containing the converted Swift variable declaration, including the 
            type and value (if applicable). Returns None if the declaration is invalid.

        Raises:
            None: This method does not raise exceptions directly, but may invoke the semantic error 
            listener in case of type mismatches.

        Side Effects:
            - Logs a message indicating the variable declaration being visited.
            - Invokes the semantic error listener if a type mismatch or unsupported type is detected.
            - Adds the variable to the symbol table if the declaration is valid.
        """
        print(f"    🔍 Visiting variable declaration: {ctx.getText()}")
        
        var_name = self.visit_identifier(ctx.IDENTIFIER())        
        mutable, keyword = (False, "let") if ctx.VAL() else (True, "var")

        # Check if the variable is already declared
        if self.check_variable_already_declared_in_current_scope(ctx = ctx, var_name = var_name):
            return None
        else:
            # Check unsupported type            
            kotlin_type = ctx.type_().getText() if ctx.type_() else self.check_expression_type(ctx.expression())

            if not self.check_supported_type(ctx = ctx, type=kotlin_type):
                return None

            # Check type mismatch, if variable is assigned            
            if ctx.expression():
                # Check type mismatch
                if not self.validate_value(ctx=ctx, type=kotlin_type):
                    return None
                var_value = self.visit_expression(ctx.expression()) 
            elif ctx.readStatement():
                # Check type is String 
                if kotlin_type != KotlinTypes.STRING.value:
                    self.semantic_error_listener.semantic_error(
                        msg = f"Type mismatch: Variable declared as '{kotlin_type}' but assigned a value of type 'String'.", 
                        line = ctx.start.line, 
                        column = ctx.start.column
                    )
                    return None
                var_value = self.visit_read_statement(ctx.readStatement())
            else:
                var_value = None
            
            # Add the variable to the symbol table
            self.add_variable_to_symbol_table(var_name=var_name, type=kotlin_type, mutable=mutable, value=var_value)
            
            swift_type = self.visit_type(ctx.type_()) if ctx.type_() else None
            
            swift_var_declaration = f"{keyword} {var_name}"
                        
            if swift_type:
                swift_var_declaration += f" : {swift_type}"

            if var_value:
                swift_var_declaration += f" = {var_value}"
            
            return swift_var_declaration     


    def visit_type(self, ctx: KotlinParser.TypeContext): 
        """
        Converts Kotlin types to Swift types.

        This method processes a Kotlin type and converts it into the corresponding Swift type 
        based on a predefined mapping. If the Kotlin type is not supported, it returns None.

        Args:
            ctx (KotlinParser.TypeContext): The context object representing the Kotlin type 
                                            in the Kotlin AST.

        Returns:
            str: The corresponding Swift type as a string, or None if the Kotlin type is unsupported.

        Raises:
            None: This method does not raise exceptions directly, but returns None if the type 
            cannot be converted.

        Side Effects:
            - Logs a message indicating the Kotlin type being visited.
        """
        print(f"    🔍 Visiting type: {ctx.getText()}")
        
        kotlin_type = ctx.getText()  
        swift_type = self.kotlin_2_swift_types.get(KotlinTypes[kotlin_type.upper()], None)  
        if not swift_type:
            return None
        return swift_type.value   
    

    def visit_assignment_statement(self, ctx: KotlinParser.AssignmentStatementContext):
        """
        Converts Kotlin variable assignment to Swift.

        This method handles the conversion of Kotlin variable assignments to Swift syntax. 
        It checks whether the assignment is a regular variable assignment or a function call, 
        handling both scenarios accordingly. It also checks for mutability, variable declarations, 
        and type mismatches. If the assignment involves a read statement, it ensures that the 
        correct type (String) is assigned.

        Args:
            ctx (KotlinParser.AssignmentStatementContext): The context object representing the assignment statement 
                                                           in the Kotlin AST.

        Returns:
            str: The Swift equivalent of the Kotlin assignment statement.

        Raises:
            None: This method returns None if there is an error, such as an undeclared variable, 
            a mutability issue, or a type mismatch.

        Side Effects:
            - Logs a message indicating the assignment statement being visited.
            - Updates the variable value in the symbol table.
            - Logs semantic errors when type mismatches occur.

        Notes:
            - If the assignment is a function call, the method processes it as such.
            - If the variable is a read statement, it ensures the type is String.
        """
        print(f"    🔍 Visiting assignment statement: {ctx.getText()}")
        
        # Workaround for handling both assignments and function calls in the same rule.
        # If the assignment is a function call (e.g., test()), the callExpression is visited.
        # Otherwise, it processes the regular variable assignment.
        if ctx.callExpression():
            return self.visit_call_expression(ctx.callExpression()) 
        else:        
            var_name = self.visit_identifier(ctx.IDENTIFIER())

            # Check if variable is declared
            if not self.check_variable_already_declared(ctx=ctx, var_name=var_name):        
                return None
            else:
                var_type, is_mutable = self.symbol_table.get_variable_info(var_name) 

                # Check mutability
                if not self.check_mutability(ctx=ctx, var_name=var_name, is_mutable=is_mutable):
                    return None
                
                if ctx.readStatement():
                    # Check type is String 
                    if var_type != KotlinTypes.STRING.value:
                        self.semantic_error_listener.semantic_error(
                            msg = f"Type mismatch: Variable declared as '{var_type}' but assigned a value of type 'String'.", 
                            line = ctx.start.line, 
                            column = ctx.start.column
                        )
                        return None
                
                    var_value = self.visit_read_statement(ctx=ctx.readStatement())
                    self.symbol_table.update_variable(name=var_name, new_value=var_value) 
                    return f"{var_name} = {var_value}"
                else:
                    # Check type mismatch            
                    if not self.validate_value(ctx=ctx, type=var_type):
                        return None
                
                    var_value = self.visit_expression(ctx=ctx.expression())
                    self.symbol_table.update_variable(name=var_name, new_value=var_value) 
                    return f"{var_name} = {var_value}"


    def visit_function_declaration(self, ctx: KotlinParser.FunctionDeclarationContext):
        """
        Transforms a Kotlin function declaration into a Swift function declaration.

        This method converts a Kotlin function declaration into the corresponding Swift syntax. 
        It handles parameter type checking, return type checking, scope management, and ensures 
        there are no duplicate parameters. Additionally, it verifies the presence of a return 
        statement in the function body and checks if the return value matches the expected return 
        type. It also adds the function and its parameters to the symbol table, and creates the 
        Swift function declaration based on the provided information.

        Args:
            ctx (KotlinParser.FunctionDeclarationContext): The context object representing the function declaration 
                                                           in the Kotlin AST.

        Returns:
            str: The Swift equivalent of the Kotlin function declaration.

        Raises:
            None: Returns None if the function is already declared or if there are errors 
            such as unsupported types, duplicate parameters, or missing return types.

        Side Effects:
            - Adds function and parameter information to the symbol table.
            - Creates and returns a Swift function declaration.
            - Logs semantic errors if issues such as unsupported types or duplicate parameters occur.

        Notes:
            - Handles both functions with and without return types.
            - Parameters are checked for duplication and added to the symbol table.
            - The function body is processed, and return type consistency is checked.
        """
        print(f"    🔍 Visiting function declaration: {ctx.getText()}")

        fun_name = self.visit_identifier(ctx.IDENTIFIER())   
        kotlin_param_types = self.check_parameter_type_list(ctx.parameterList()) if ctx.parameterList() else None

        # Check if the variable is already declared
        if self.check_function_already_declared_in_current_scope(ctx = ctx, fun_name = fun_name, kotlin_param_types=kotlin_param_types):        
            return None
        else:
            param_names = self.check_parameter_name_list(ctx.parameterList()) if ctx.parameterList() else None
            param_names_values = self.check_parameter_name_value_list(ctx.parameterList()) if ctx.parameterList() else None
            param_names_values_dict = {
                item.split(": ")[0]: item.split(": ")[1] if item.split(": ")[1] != "None" else None
                for item in param_names_values.split(", ")
            }

            if ctx.type_():
                kotlin_return_type = ctx.type_().getText()
                # Check unsupported return type
                if not self.check_supported_type(ctx = ctx, type=kotlin_return_type):
                    return None
            else:
                kotlin_return_type = None
        
            self.symbol_table.add_function(fun_name, kotlin_param_types, param_names, kotlin_return_type)
            self.symbol_table.add_scope() 

            if ctx.parameterList():
                for param_type, param_name in zip(kotlin_param_types.split(", "), param_names.split(", ")):
                    if self.check_variable_already_declared_in_current_scope(ctx = ctx, var_name = param_name):
                        continue
                    
                    # Get value form param_names_values_dict
                    param_value = param_names_values_dict.get(param_name, None)

                    # Add the variable to the symbol table
                    self.add_variable_to_symbol_table(var_name=param_name, type=param_type, mutable=False, value=param_value) 

                # Check if the function declaration contains duplicated parameters
                if not self.check_duplicate_parameters(ctx = ctx.parameterList(), fun_name=fun_name): 
                    return None

            parameters = self.visit_parameter_list(ctx.parameterList()) if ctx.parameterList() else ""

            body = self.visit_block(ctx.block())        

            # Check if the function body contains a return statement and that the return value matches the return type
            if not self.check_return_statement(ctx = ctx.block(), fun_name = fun_name, fun_return_type = kotlin_return_type):
                return None

            if ctx.type_():
                return_type = self.visit_type(ctx.type_()) 
                swift_function = f"func {fun_name}({parameters}) -> {return_type} {{ {body} }}"
            else:
                swift_function = f"func {fun_name}({parameters}) {{ {body} }}"

            self.symbol_table.remove_scope()

            return swift_function


    def visit_block(self, ctx: KotlinParser.BlockContext):
        """
        Visits a block of statements and joins them with newlines.

        This method processes a block of Kotlin statements and generates the corresponding Swift code. 
        It visits each statement within the block, invoking the appropriate visit method for each statement, 
        and then joins the results with newlines to form a properly structured Swift code block.

        Args:
            ctx (KotlinParser.BlockContext): The context object representing the block of statements 
                                             in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin block, with each statement 
            joined by a newline.

        Raises:
            None: Returns None for any unrecognized or empty statements.

        Side Effects:
            - Visits each statement within the block and converts them to Swift.
            - Joins the converted statements with newlines to form a complete Swift block.

        Notes:
            - Handles a sequence of statements in a Kotlin block and converts them in order to Swift.
            - Filters out any empty or unrecognized statements before joining them.
        """
        print(f"    🔍 Visiting block: {ctx.getText()}")        
        
        statements = [self.visit_statement(stmt) for stmt in ctx.statement()]
        return "\n".join(filter(None, statements))


    def visit_statement(self, ctx: KotlinParser.StatementContext):
        """
        Handles various types of statements like read, print, if, for, etc., and converts them to Swift.

        This method processes different types of Kotlin statements, such as variable declarations, assignments, 
        control flow (if, for), and expressions (read, print), by delegating the work to specific visit methods 
        based on the type of the statement. The corresponding Swift code for each statement is generated and 
        returned.

        Args:
            ctx (KotlinParser.StatementContext): The context object representing the statement 
                                                 in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin statement. If the statement is 
            unrecognized, an empty string is returned.

        Raises:
            None: Returns an empty string for unrecognized or invalid statements.

        Side Effects:
            - Invokes the appropriate visit method for each type of Kotlin statement, converting them to Swift.
            - Prints diagnostic messages for recognized and unrecognized statements.

        Notes:
            - The method distinguishes between different types of Kotlin statements (read, print, if, for, etc.) 
              and calls the corresponding visit methods for each.
            - If the statement type is unrecognized, a diagnostic message is printed, and an empty string is returned.
        """
        print(f"    🔍 Visiting statement: {ctx.getText()}")
        if ctx.readStatement():
            return self.visit_read_statement(ctx.readStatement())
        elif ctx.printStatement():
            return self.visit_print_statement(ctx.printStatement())
        elif ctx.ifElseStatement():
            return self.visit_if_else_statement(ctx.ifElseStatement())
        elif ctx.forStatement():
            return self.visit_for_statement(ctx.forStatement())
        elif ctx.assignmentStatement():
            return self.visit_assignment_statement(ctx.assignmentStatement())
        elif ctx.varDeclaration(): 
            return self.visit_var_declaration(ctx.varDeclaration())
        elif ctx.returnStatement():
            return self.visit_return_statement(ctx.returnStatement())
        elif ctx.commentStatement():
            return self.visit_comment_statement(ctx.commentStatement())        
        else: 
            print(f"    ❌ Unrecognized statement: {ctx.getText()}")
            return ""
        

    def visit_read_statement(self, ctx: KotlinParser.ReadStatementContext):
        """
        Converts a Kotlin readLine statement to Swift, handling the conversion to the appropriate Swift syntax.

        This method specifically handles Kotlin's `readLine()` function, converting it to the corresponding 
        Swift syntax for reading input from the user. The function does not consider the mutability (var/val) 
        of the variable, as it only processes the statement itself.

        Args:
            ctx (KotlinParser.ReadStatementContext): The context object representing the `readLine` statement 
                                                     in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin `readLine()` statement.

        Raises:
            None: No exceptions are raised.

        Side Effects:
            - Prints a diagnostic message for the `readLine()` statement.

        Notes:
            - The function converts Kotlin's `readLine()` directly to Swift's `readLine()` function without 
              considering any variable declarations.
        """        
        print(f"    🔍 Visiting read statement: {ctx.getText()}")
        return f"readLine()"
    

    def visit_print_statement(self, ctx: KotlinParser.PrintStatementContext):
        """
        Converts a Kotlin print statement to a Swift print statement.

        This method converts Kotlin's `println()` or `print()` function to Swift's `print()` function.
        It handles the conversion by extracting the expression inside the Kotlin print statement and
        formatting it to Swift's print function syntax.

        Args:
            ctx (KotlinParser.PrintStatementContext): The context object representing the Kotlin print statement 
                                                      in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin print statement, e.g., `print(expression)`.

        Raises:
            None: No exceptions are raised.

        Side Effects:
            - Prints a diagnostic message for the print statement.

        Notes:
            - This method assumes the expression inside the print statement is handled by the `visit_expression()` method.
        """
        print(f"    🔍 Visiting print statement: {ctx.getText()}")
        
        expression = self.visit_expression(ctx.expression())
        return f"print({expression})"
    

    def visit_if_else_statement(self, ctx: KotlinParser.IfElseStatementContext):
        """
        Converts a Kotlin if-else statement into a Swift if-else statement.

        This method processes the Kotlin `if`-`else` construct, converting it to the Swift equivalent. 
        It handles both the `if` block and the optional `else` block, including the condition expression and bodies of the statements.

        Args:
            ctx (KotlinParser.IfElseStatementContext): The context object representing the Kotlin `if`-`else` statement
                                                       in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin `if`-`else` statement, formatted as `if {condition} {if_body} else {else_body}`.

        Raises:
            None: No exceptions are raised.

        Side Effects:
            - Prints a diagnostic message for the if statement.

        Notes:
            - This method calls `visit_expression()` to process the condition expression.
            - If there is no `else` block, the method generates a Swift `if` statement without the `else` part.
            - The method relies on `validate_if_condition()` to ensure the condition is valid.
        """
        print(f"    🔍 Visiting if statement: {ctx.getText()}")
        
        condition = self.visit_expression(ctx.expression())
        
        if not self.validate_if_condition(ctx):
            return None

        if_body = self.visit_if_body(ctx.ifBody())

        if ctx.ELSE():
            else_body = self.visit_else_body(ctx.elseBody())

            return f"if {condition} {{ {if_body} }} else {{ {else_body} }}"

        return f"if {condition} {{ {if_body} }}"

    
    def visit_if_body(self, ctx: KotlinParser.IfBodyContext):
        """
        Converts the body of a Kotlin `if` statement to its Swift equivalent.

        This method processes the body of the `if` block in a Kotlin `if-else` statement. If the body is a block of statements, 
        it recursively visits the block; otherwise, it processes the single statement in the body.

        Args:
            ctx (KotlinParser.IfBodyContext): The context object representing the body of the `if` statement in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin `if` body, either a block of statements or a single statement.

        Raises:
            None: No exceptions are raised.

        Side Effects:
            - Prints a diagnostic message for the `if` body.

        Notes:
            - This method calls `visit_block()` to process the block of statements and `visit_statement()` for individual statements.
        """
        print(f"    🔍 Visiting if-else statement: {ctx.getText()}")
        
        return self.visit_block(ctx.block()) if ctx.block() else self.visit_statement(ctx.statement())


    def visit_else_body(self, ctx: KotlinParser.ElseBodyContext):
        """
        Converts the body of a Kotlin `else` block in an `if-else` statement to its Swift equivalent.

        This method processes the body of the `else` block in a Kotlin `if-else` statement. If the body is a block of statements, 
        it recursively visits the block; otherwise, it processes the single statement in the body.

        Args:
            ctx (KotlinParser.ElseBodyContext): The context object representing the body of the `else` block in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin `else` body, either a block of statements or a single statement.

        Raises:
            None: No exceptions are raised.

        Side Effects:
            - Prints a diagnostic message for the `else` body.

        Notes:
            - This method calls `visit_block()` to process the block of statements and `visit_statement()` for individual statements.
        """
        print(f"    🔍 Visiting if-else statement: {ctx.getText()}")
        
        return self.visit_block(ctx.block()) if ctx.block() else self.visit_statement(ctx.statement())


    def visit_for_statement(self, ctx: KotlinParser.ForStatementContext):
        """
        Converts a Kotlin `for` loop with a range into a Swift-compatible `for` loop.

        This method processes a Kotlin `for` loop that iterates over a range (e.g., `for i in 1..10`) and converts it into its
        Swift equivalent. It handles the membership expression, checks for valid types, and processes the body of the loop.

        Args:
            ctx (KotlinParser.ForStatementContext): The context object representing the `for` loop in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin `for` loop, with the appropriate expression and body.

        Raises:
            None: No exceptions are raised, but other validation methods may raise exceptions for invalid expressions or statements.

        Side Effects:
            - Prints a diagnostic message for the `for` loop statement.

        Notes:
            - The method calls `check_membership_expression_type()` to ensure the expression is valid and `visit_memebership_expression()` to process the expression.
            - If the loop body is a block, it uses `visit_block()`, otherwise, it processes a single statement using `visit_statement()`.
        """
        print(f"    🔍 Visiting for statement: {ctx.getText()}")
        
        self.check_membership_expression_type(ctx.membershipExpression())
        expression = self.visit_memebership_expression(ctx.membershipExpression())
        if ctx.block(): 
            body = self.visit_block(ctx.block())
        else:  
            body = self.visit_statement(ctx.statement())
        return f"for {expression} {{ {body} }}"


    def visit_return_statement(self, ctx: KotlinParser.ReturnStatementContext):
        """
        Converts a Kotlin `return` statement to its Swift equivalent.

        This method processes a Kotlin `return` statement, converting it into a Swift `return` statement. If there is an 
        expression in the return statement, it processes the expression and returns the Swift syntax for returning a value. 
        If no expression is present, it returns a simple `return` statement.

        Args:
            ctx (KotlinParser.ReturnStatementContext): The context object representing the `return` statement 
                                                       in the Kotlin AST.

        Returns:
            str: A string representing the Swift equivalent of the Kotlin `return` statement, either with or without an expression.

        Raises:
            None: No exceptions are raised in this method, but any issues in expression handling may be raised by the `visit_expression()` method.

        Side Effects:
            - Prints a diagnostic message for the `return` statement.

        Notes:
            - The method checks if the return statement contains an expression by inspecting `ctx.expression()`.
            - If an expression is found, the method processes it and returns the corresponding Swift code.
            - If no expression is present, a simple `return` statement is generated.
        """
        print(f"    🔍 Visiting return statement: {ctx.getText()}")            
        if ctx.expression():
            expression = self.visit_expression(ctx.expression())
            return f"return {expression}"
        return "return"   


    def visit_expression(self, ctx: KotlinParser.ExpressionContext):
        """
        Transforms a Kotlin expression into its Swift equivalent.

        This method is the entry point for visiting a variety of Kotlin expressions, including literals, 
        identifiers, and operators. It processes the expression in the context of logical OR expressions by 
        delegating the visit to `visit_logical_or_expression`. It can be extended to handle more specific 
        types of expressions as the transpiler evolves.

        Args:
            ctx (KotlinParser.ExpressionContext): The context object representing the expression 
                                                  in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the given Kotlin expression.

        Raises:
            None: No exceptions are raised, but any issues in expression handling are deferred to more specific methods like 
                  `visit_logical_or_expression()`.

        Side Effects:
            - Prints a diagnostic message for the visited expression.

        Notes:
            - The method currently delegates to `visit_logical_or_expression()` to handle logical OR expressions.
            - More specific handling for different types of expressions can be added as needed.
        """
        print(f"    🔍 Visiting expression: {ctx.getText()}")
        
        return self.visit_logical_or_expression(ctx.logicalOrExpression())  


    def visit_logical_or_expression(self, ctx: KotlinParser.LogicalOrExpressionContext):
        """
        Transforms a Kotlin logical OR expression into its Swift equivalent.

        This method handles the transformation of Kotlin logical OR expressions (i.e., `a || b`) into Swift. 
        It processes the left and right operands of the logical OR and recursively delegates to handle logical 
        AND expressions, as they are part of the logical OR's operand expressions.

        Args:
            ctx (KotlinParser.LogicalOrExpressionContext): The context object representing the logical OR expression 
                                                           in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the logical OR expression.

        Raises:
            None: No exceptions are raised, but any issues in operand processing are handled by the recursive calls.

        Side Effects:
            - Prints a diagnostic message for the visited logical OR expression.

        Notes:
            - The method assumes that logical AND expressions are the building blocks of the logical OR expression.
            - Operators (i.e., `||`) are placed between operands in the resulting Swift expression.
            - The handling of the logical AND expressions is delegated to `visit_logical_and_expression()`.
        """
        print(f"    🔍 Visiting logical OR expression: {ctx.getText()}")
        
        left = self.visit_logical_and_expression(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_logical_and_expression(ctx.logicalAndExpression(i))
            left = f"{left} {operator} {right}" if right is not None else f"{left}" 
        return f"{left}"
    

    def visit_logical_and_expression(self, ctx: KotlinParser.LogicalAndExpressionContext):
        """
        Transforms a Kotlin logical AND expression into its Swift equivalent.

        This method handles the transformation of Kotlin logical AND expressions (i.e., `a && b`) into Swift. 
        It processes the left and right operands of the logical AND and recursively delegates to handle equality 
        expressions, as they are part of the logical AND's operand expressions.

        Args:
            ctx (KotlinParser.LogicalAndExpressionContext): The context object representing the logical AND expression 
                                                            in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the logical AND expression.

        Raises:
            None: No exceptions are raised, but any issues in operand processing are handled by the recursive calls.

        Side Effects:
            - Prints a diagnostic message for the visited logical AND expression.

        Notes:
            - The method assumes that equality expressions are the building blocks of the logical AND expression.
            - Operators (i.e., `&&`) are placed between operands in the resulting Swift expression.
            - The handling of the equality expressions is delegated to `visit_equality_expression()`.
        """
        print(f"    🔍 Visiting logical AND expression: {ctx.getText()}")
        
        left = self.visit_equality_expression(ctx.equalityExpression(0))  
        for i in range(1, len(ctx.equalityExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_equality_expression(ctx.equalityExpression(i)) 
            left = f"{left} {operator} {right}"
        return f"{left}"


    def visit_equality_expression(self, ctx: KotlinParser.EqualityExpressionContext):
        """
        Transforms a Kotlin equality expression into its Swift equivalent.

        This method handles the transformation of Kotlin equality expressions (i.e., `a == b` or `a != b`) into Swift.
        It processes the left and right operands of the equality expression and recursively delegates to handle relational 
        expressions, as they are the building blocks of the equality expression.

        Args:
            ctx (KotlinParser.EqualityExpressionContext): The context object representing the equality expression 
                                                          in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the equality expression.

        Raises:
            None: No exceptions are raised, but any issues in operand processing are handled by the recursive calls.

        Side Effects:
            - Prints a diagnostic message for the visited equality expression.

        Notes:
            - The method assumes that relational expressions are the building blocks of the equality expression.
            - Operators (i.e., `==` or `!=`) are placed between operands in the resulting Swift expression.
            - The handling of the relational expressions is delegated to `visit_relational_expression()`.
        """
        print(f"    🔍 Visiting equality expression: {ctx.getText()}")
        
        left = self.visit_relational_expression(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_relational_expression(ctx.relationalExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}"


    def visit_relational_expression(self, ctx: KotlinParser.RelationalExpressionContext):
        """
        Transforms a Kotlin relational expression into its Swift equivalent.

        This method handles the transformation of Kotlin relational expressions (e.g., `a < b`, `a > b`, `a <= b`, `a >= b`) 
        into their Swift equivalents. It processes the left and right operands of the relational expression and delegates 
        the handling of additive expressions (e.g., `a + b`, `a - b`) to another method.

        Args:
            ctx (KotlinParser.RelationalExpressionContext): The context object representing the relational expression 
                                                            in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the relational expression.

        Raises:
            None: No exceptions are raised, but any issues in operand processing are handled by the recursive calls.

        Side Effects:
            - Prints a diagnostic message for the visited relational expression.

        Notes:
            - The method assumes that additive expressions are the building blocks of relational expressions.
            - Operators (e.g., `<`, `>`, `<=`, `>=`) are placed between operands in the resulting Swift expression.
            - The handling of additive expressions is delegated to `visit_additive_expression()`.
        """
        print(f"    🔍 Visiting relational expression: {ctx.getText()}")
        
        left = self.visit_additive_expression(ctx.additiveExpression(0))
        if len(ctx.additiveExpression()) > 1:
            operator = ctx.getChild(1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_additive_expression(ctx.additiveExpression(1))
            return f"{left} {operator} {right}" 
        return f"{left}"


    def visit_additive_expression(self, ctx: KotlinParser.AdditiveExpressionContext):
        """
        Transforms a Kotlin additive expression into its Swift equivalent.

        This method handles the transformation of Kotlin additive expressions (e.g., `a + b`, `a - b`) 
        into their Swift equivalents. It processes the left and right operands of the additive expression and 
        delegates the handling of multiplicative expressions (e.g., `a * b`, `a / b`) to another method.

        Args:
            ctx (KotlinParser.AdditiveExpressionContext): The context object representing the additive expression 
                                                          in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the additive expression.

        Raises:
            None: No exceptions are raised, but any issues in operand processing are handled by the recursive calls.

        Side Effects:
            - Prints a diagnostic message for the visited additive expression.

        Notes:
            - The method assumes that multiplicative expressions are the building blocks of additive expressions.
            - Operators (e.g., `+`, `-`) are placed between operands in the resulting Swift expression.
            - The handling of multiplicative expressions is delegated to `visit_multiplicative_expression()`.
        """
        print(f"    🔍 Visiting additive expression: {ctx.getText()}")
        
        left = self.visit_multiplicative_expression(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_multiplicative_expression(ctx.multiplicativeExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}"  


    def visit_multiplicative_expression(self, ctx: KotlinParser.MultiplicativeExpressionContext):
        """
        Transforms a Kotlin multiplicative expression into its Swift equivalent.

        This method handles the transformation of Kotlin multiplicative expressions (e.g., `a * b`, `a / b`, 
        `a % b`) into their Swift equivalents. It processes the left and right operands of the multiplicative 
        expression and delegates the handling of unary expressions (e.g., `-a`, `+a`) to another method.

        Args:
            ctx (KotlinParser.MultiplicativeExpressionContext): The context object representing the multiplicative expression 
                                                                in the Kotlin AST.

        Returns:
            str: A string representing the transformed Swift code for the multiplicative expression.

        Raises:
            None: No exceptions are raised, but any issues in operand processing are handled by the recursive calls.

        Side Effects:
            - Prints a diagnostic message for the visited multiplicative expression.

        Notes:
            - The method assumes that unary expressions are the building blocks of multiplicative expressions.
            - Operators (e.g., `*`, `/`, `%`) are placed between operands in the resulting Swift expression.
            - The handling of unary expressions is delegated to `visit_unary_expression()`.
        """
        print(f"    🔍 Visiting multiplicative expression: {ctx.getText()}")
        
        left = self.visit_unary_expression(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_unary_expression(ctx.unaryExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}" 


    def visit_unary_expression(self, ctx: KotlinParser.UnaryExpressionContext):
        """
        Transforms a Kotlin unary expression into its Swift equivalent.

        This method handles the transformation of Kotlin unary expressions, such as logical negation (`!a`) 
        and negation (`-a`), into their Swift equivalents. It processes the primary expression that follows 
        the unary operator and applies the corresponding Swift unary operator.

        Args:
            ctx (KotlinParser.UnaryExpressionContext): The context object representing the unary expression 
                                                       in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift code for the unary expression.

        Raises:
            None: No exceptions are raised, but invalid or unrecognized unary operators are handled implicitly 
                  by the method's structure.

        Side Effects:
            - Prints a diagnostic message for the visited unary expression.

        Notes:
            - The method distinguishes between logical negation (`!`) and arithmetic negation (`-`) 
              based on the presence of the `NOT` or `MINUS` token in the context.
            - If the unary expression is neither `!` nor `-`, it delegates the processing of membership 
              expressions to `visit_memebership_expression()`.
        """
        print(f"    🔍 Visiting unary expression: {ctx.getText()}")
        
        if ctx.NOT(): 
            return f"!{self.visit_primary_expression(ctx.primaryExpression())}"
        elif ctx.MINUS():
            return f"-{self.visit_primary_expression(ctx.primaryExpression())}"
        else:
            return f"{self.visit_memebership_expression(ctx.membershipExpression())}"


    def visit_memebership_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        """
        Transforms a Kotlin membership expression into its Swift equivalent.

        This method handles the transformation of Kotlin membership expressions, such as checking if a value 
        is in a range or collection (e.g., `a in b` or `a !in b`), into their Swift equivalents. It processes 
        both the left and right sides of the membership expression and applies the appropriate Swift operators.

        Args:
            ctx (KotlinParser.PrimaryExpressionContext): The context object representing the membership expression 
                                                         in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift code for the membership expression.

        Raises:
            None: No exceptions are raised, but invalid or unrecognized membership expressions are handled 
                  implicitly by the method's structure.

        Side Effects:
            - Prints a diagnostic message for the visited membership expression.

        Notes:
            - The method checks if the membership expression involves the `in` or `!in` operator and transforms 
              it accordingly.
            - If the `rangeExpression` is present, it is processed and included in the final expression string.
        """
        print(f"    🔍 Visiting membership expression: {ctx.getText()}")
        
        left = self.visit_primary_expression(ctx.primaryExpression())
        if ctx.rangeExpression():
            right = self.visit_range_expression(ctx.rangeExpression())
            if right:   
                if ctx.NOT() and ctx.IN():
                    return f"{left} !in {right}"
                elif ctx.IN():
                    return f"{left} in {right}"
        return f"{left}"
    

    def visit_primary_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        """
        Transforms a Kotlin primary expression into its Swift equivalent.

        This method handles primary expressions in Kotlin, which can include literals, 
        identifiers, or function call expressions. It processes the context accordingly 
        and generates the appropriate Swift representation.

        Args:
            ctx (KotlinParser.PrimaryExpressionContext): The context object representing the primary expression 
                                                         in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift code for the primary expression.

        Raises:
            None: No exceptions are raised, but certain issues like unassigned variables might trigger checks.

        Side Effects:
            - Prints a diagnostic message for the visited primary expression.
            - Checks whether the variable has already been assigned when processing an identifier.

        Notes:
            - If the primary expression is an identifier, the method checks if the variable has been assigned 
              before and then returns the identifier name.
            - If the primary expression is a literal or a function call, it recursively processes and transforms 
              those components.
            - Parenthesized expressions are also handled by recursively visiting the enclosed expression.
        """
        print(f"    🔍 Visiting primary expression: {ctx.getText()}")
        
        if ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER().getText()  
            self.check_variable_already_assigned(ctx, identifier) 
            return identifier # return identifier anyway
        elif ctx.LEFT_ROUND_BRACKET() and ctx.RIGHT_ROUND_BRACKET():
            return f"({self.visit_expression(ctx.expression())})"  
        elif ctx.callExpression():
            return self.visit_call_expression(ctx.callExpression())
        elif ctx.literal():
            return self.visit_literal(ctx.literal())


    def visit_range_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        """
        Transforms a Kotlin range expression into its Swift equivalent.

        This method handles range expressions in Kotlin, such as `a..b`, and converts them to 
        the corresponding Swift range syntax.

        Args:
            ctx (KotlinParser.PrimaryExpressionContext): The context object representing the range expression 
                                                         in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift code for the range expression.

        Raises:
            None: If an invalid range is encountered (i.e., one of the range bounds is missing), 
                  a semantic error is reported.

        Side Effects:
            - Prints a diagnostic message for the visited range expression.
            - Triggers a semantic error if the range expression is invalid (i.e., lacks a second operand).

        Notes:
            - The method expects a valid range expression with two operands (e.g., `a..b`).
            - In Swift, the range expression is represented as `a ... b`, with three dots for the range.
        """
        print(f"    🔍 Visiting range expression: {ctx.getText()}")
        
        left = self.visit_additive_expression(ctx.additiveExpression(0))
        if not ctx.additiveExpression(1):
            self.semantic_error_listener.semantic_error(
                msg = f"Invalid range found.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return None
        right = self.visit_additive_expression(ctx.additiveExpression(1))        
        return f"{left} ... {right}"


    def visit_call_expression(self, ctx: KotlinParser.CallExpressionContext):
        """
        Transforms a Kotlin function call expression into its Swift equivalent.

        This method handles function calls in Kotlin and converts them into the corresponding
        Swift function call syntax.

        Args:
            ctx (KotlinParser.CallExpressionContext): The context object representing the 
                                                      function call expression in the Kotlin 
                                                      Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift function call.

        Raises:
            None: If the arguments for the function call are invalid, a semantic error is reported.

        Side Effects:
            - Prints a diagnostic message for the visited function call expression.
            - Triggers a semantic error if the arguments do not match the expected format.

        Notes:
            - If the function call includes arguments, they are transformed into the appropriate
              Swift call format.
            - If no arguments are provided, the function call will be represented with empty parentheses.
        """
        print(f"    🔍 Visiting call expression: {ctx.getText()}")
        
        fun_name = self.visit_identifier(ctx.IDENTIFIER())

        if ctx.argumentList():    
            if not self.check_arguments(ctx, fun_name): 
                return None
            arguments = self.visit_argument_list(ctx.argumentList()) 
            return f"{fun_name}({arguments})"
        
        return f"{fun_name}()"
    

    def visit_argument_list(self, ctx: KotlinParser.ArgumentListContext):
        """
        Transforms a list of Kotlin function arguments into Swift-compatible arguments.

        This method processes a list of arguments in a Kotlin function call and converts them 
        into the corresponding Swift syntax, ensuring each argument is properly formatted.

        Args:
            ctx (KotlinParser.ArgumentListContext): The context object representing the 
                                                    list of function arguments in the Kotlin 
                                                    Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift arguments, separated by commas.

        Side Effects:
            - Prints a diagnostic message for the visited argument list.

        Notes:
            - The function assumes that all arguments in the list are properly formatted and 
              only performs the transformation.
            - The resulting string will contain all arguments joined by commas, as required by Swift function calls.
        """
        print(f"    🔍 Visiting argument list: {ctx.getText()}")
        
        return ", ".join([self.visit_argument(argument) for argument in ctx.argument()])
    

    def visit_argument(self, ctx: KotlinParser.ArgumentContext):
        """
        Converts a Kotlin argument into a Swift argument.

        This method processes an individual argument in a Kotlin function call and transforms it 
        into the corresponding Swift argument format, taking into account both named and unnamed arguments.

        Args:
            ctx (KotlinParser.ArgumentContext): The context object representing a single argument 
                                                in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: A string representing the transformed Swift argument, either as a named argument 
                 (e.g., `name: value`) or just the argument value (e.g., `value`).

        Side Effects:
            - Prints a diagnostic message for the visited argument.

        Notes:
            - If the argument has an identifier (name), the Swift argument will be in the format 
              `name: value`.
            - If the argument has no name, the Swift argument will just be the value.
            - The function assumes that the argument expression is correctly formatted in Kotlin.
        """
        print(f"    🔍 Visiting argument: {ctx.getText()}")
        
        argument_value = self.visit_expression(ctx.expression()) 
        if (ctx.IDENTIFIER()):
            argument_name = self.visit_identifier(ctx.IDENTIFIER())
            return f"{argument_name}: {argument_value}"
        return f"{argument_value}"


    def visit_literal(self, ctx: KotlinParser.LiteralContext):
        """
        Handles literal expressions in Kotlin, such as string, integer, or boolean literals.

        This method processes a literal expression in Kotlin and directly returns its string representation.
        The literal can be of various types, including numbers, booleans, or strings.

        Args:
            ctx (KotlinParser.LiteralContext): The context object representing a literal expression 
                                               in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: The string representation of the literal value in Kotlin, which is directly returned
                 as-is for use in Swift code.

        Side Effects:
            - Prints a diagnostic message for the visited literal.

        Notes:
            - This function does not modify or interpret the literal value but simply returns it as 
              it appears in the Kotlin source code.
        """
        print(f"    🔍 Visiting literal: {ctx.getText()}")
        
        return ctx.getText()


    def visit_comment_statement(self, ctx: KotlinParser.CommentStatementContext):
        """
        Converts Kotlin comments to Swift comments.

        This method processes comment statements in Kotlin and transforms them into their 
        equivalent Swift comment formats. It handles both single-line and block comments.

        Args:
            ctx (KotlinParser.CommentStatementContext): The context object representing a comment
                                                        statement in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: The transformed comment in Swift syntax, either a single-line or block comment.

        Side Effects:
            - Prints a diagnostic message for the visited comment statement.

        Notes:
            - Single-line comments in Kotlin (//) are converted to Swift's single-line comment syntax (//).
            - Block comments in Kotlin (/* */) are converted to Swift's block comment syntax (/* */).
        """
        print(f"    🔍 Visiting comment: {ctx.getText()}")
        if ctx.LINE_COMMENT():
            return self.visit_line_comment(ctx.LINE_COMMENT())
        elif ctx.BLOCK_COMMENT():
            return self.visit_block_comment(ctx.BLOCK_COMMENT())
        else:
            return None
        

    def visit_line_comment(self, ctx: KotlinParser):
        """
        Converts Kotlin inline comments to Swift single-line comments.

        This method processes Kotlin single-line comments (which start with '//' in Kotlin)
        and converts them to Swift single-line comments (which start with '#').

        Args:
            ctx (KotlinParser): The context object representing a single-line comment
                                in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: The transformed comment in Swift syntax, prefixed with '#'.

        Side Effects:
            - Prints a diagnostic message for the visited comment.

        Notes:
            - This method trims the "//" prefix and any leading or trailing whitespace 
              before converting the comment to Swift format.
        """
        print(f"    🔍 Visiting inline comment: {ctx.getText()}")
        comment = ctx.getText()[2:].strip() 
        return f"# {comment}"


    def visit_block_comment(self, ctx: KotlinParser):
        """
        Converts Kotlin block comments to Swift block comments.

        This method processes Kotlin block comments (which start with '/*' and end with '*/' in Kotlin)
        and converts them to Swift block comments (which are also enclosed in '/*' and '*/').

        Args:
            ctx (KotlinParser): The context object representing a block comment
                                in the Kotlin Abstract Syntax Tree (AST).

        Returns:
            str: The transformed comment in Swift syntax, enclosed in '/*' and '*/'.

        Side Effects:
            - Prints a diagnostic message for the visited block comment.

        Notes:
            - This method removes the '/*' and '*/' delimiters and any leading/trailing whitespace 
              before converting the comment to Swift format.
        """
        print(f"    🔍 Visiting block comment: {ctx.getText()}")
        comment = ctx.getText()[2:-2].strip() 
        return f"/* {comment} */" 
    

    ##### SEMANTIC CHECKS #####


    def add_variable_to_symbol_table(self, var_name, type, mutable, value = None):
        """Adds a variable to the symbol table."""
        print(f"    🔍 Adding variable {var_name} to the symbol table.")
        
        symbol = Symbol(name=var_name, type=type, mutable=mutable, value = value)
        self.symbol_table.add_variable(var_name, symbol)


    def check_variable_already_declared(self, ctx, var_name):
        """Checks if the variable is already declared in any scope."""
        print(f"    🔍 Checking if variable {var_name} is already declared.")
        
        if not self.symbol_table.lookup_variable(var_name):
            self.semantic_error_listener.semantic_error(
                msg = f"Trying to access or assign variable '{var_name}' before its declaration.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return False
        return True


    def check_variable_already_declared_in_current_scope(self, ctx, var_name):
        """Checks if the variable is already declared in the current scope."""
        print(f"    🔍 Checking if variable {var_name} is already declared in the current scope.")
        
        if self.symbol_table.lookup_variable_in_current_scope(var_name):
            self.semantic_error_listener.semantic_error(
                msg=f"Variable '{var_name}' is already declared in the current scope.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return True
        return False


    def check_variable_already_assigned(self, ctx, var_name):
        """Checks if the variable is already (declared and) assigned."""        
        print(f"    🔍 Checking if the variable {ctx.getText()} is already assigned.")
        
        if not self.check_variable_already_declared(ctx, var_name): 
            return False
    
        if not self.symbol_table.get_variable_assigned(var_name):
            self.semantic_error_listener.semantic_error(
                msg=f"Variable '{var_name}' is not assigned yet.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return False
        
        return True
        
    
    def check_supported_type(self, ctx, type):
        """Checks if the Kotlin type is supported."""
        print(f"    🔍 Checking if type {type} is supported.")
        
        if type not in [item.value for item in KotlinTypes]:
            self.semantic_error_listener.semantic_error(
                f"Unsupported type '{type}'.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return False
        return True


    def validate_value(self, ctx, type):
        """Validates the value assigned to the variable and checks for type mismatch."""        
        print(f"    🔍 Checking if the variable {ctx.getText()} has a valid type.")
        
        value_type = self.check_expression_type(ctx.expression())
        if value_type and type != value_type:
            self.semantic_error_listener.semantic_error(
                f"Type mismatch: Variable declared as '{type}' but assigned a value of type '{value_type}'.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return False
        return True
    
    
    def check_mutability(self, ctx, var_name, is_mutable):
        """Checks if the variable being assigned is mutable."""
        print(f"    🔍 Checking if the variable {var_name} is mutable.")
        
        if not is_mutable:               
            self.semantic_error_listener.semantic_error(
                msg = f"Trying to update immutable variable '{var_name}'.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return False
        return True
    

    def validate_if_condition(self, ctx):
        print(f"    🔍 Validating if statement condition.")
        
        condition_type = self.check_expression_type(ctx=ctx.expression())
        if condition_type != KotlinTypes.BOOLEAN.value:
            self.semantic_error_listener.semantic_error(
                msg = f"Invalid expression type in 'if' condition: expected Boolean, found '{condition_type}'.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return False
        return True


    def check_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the expression {ctx.getText()}.")
        
        return self.check_logical_or_expression_type(ctx.logicalOrExpression())
    

    def check_logical_or_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the logical or expression {ctx.getText()}.")
        
        left_type = self.check_logical_and_expression_type(ctx.logicalAndExpression(0))

        for i in range(1, len(ctx.logicalAndExpression())):
            right_type = self.check_logical_and_expression_type(ctx.logicalAndExpression(i))
            if right_type != left_type:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply logical or operator to operands of type '{left_type}' and '{right_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return KotlinTypes.BOOLEAN.value            
        return left_type
    

    def check_logical_and_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the logical and expression {ctx.getText()}.")
        
        left_type = self.check_equality_expression_type(ctx.equalityExpression(0))

        for i in range(1, len(ctx.equalityExpression())):
            right_type = self.check_equality_expression_type(ctx.equalityExpression(i))
            if right_type != left_type:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply logical and operator to operands of type '{left_type}' and '{right_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return KotlinTypes.BOOLEAN.value                       
        return left_type
    
    
    def check_equality_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the equality expression {ctx.getText()}.")
        
        left_type = self.check_relational_expression_type(ctx.relationalExpression(0))
        
        for i in range(1, len(ctx.relationalExpression())):
            right_type = self.check_relational_expression_type(ctx.relationalExpression(i))
            if right_type != left_type:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply equality operator to operands of type '{left_type}' and '{right_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return KotlinTypes.BOOLEAN.value            
        return left_type
    

    def check_relational_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the relational expression {ctx.getText()}.")
        
        left_type = self.check_additive_expression_type(ctx.additiveExpression(0))  
                
        if len(ctx.additiveExpression()) > 1:
            right_type = self.check_additive_expression_type(ctx.additiveExpression(1)) 
            if right_type != left_type:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply relational operator to operands of type '{left_type}' and '{right_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return KotlinTypes.BOOLEAN.value                     
        return left_type


    def check_additive_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the additive expression {ctx.getText()}.")
        
        left_type = self.check_multiplicative_expression_type(ctx.multiplicativeExpression(0))
        
        for i in range(1, len(ctx.multiplicativeExpression())):
            right_type = self.check_multiplicative_expression_type(ctx.multiplicativeExpression(i))
            if right_type != left_type:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply additive operator to operands of type '{left_type}' and '{right_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return KotlinTypes.INT.value            
        return left_type

    
    def check_multiplicative_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the multiplicative expression {ctx.getText()}.")
        
        left_type = self.check_unary_expression_type(ctx.unaryExpression(0))
        
        for i in range(1, len(ctx.unaryExpression())):
            right_type = self.check_unary_expression_type(ctx.unaryExpression(i))
            if right_type != left_type:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply multiplicative operator to operands of type '{left_type}' and '{right_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return KotlinTypes.INT.value                  
        return left_type


    def check_unary_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the unary expression {ctx.getText()}.")
        
        if ctx.NOT(): 
            expr_type = self.check_primary_expression_type(ctx.primaryExpression())  
            if expr_type != KotlinTypes.BOOLEAN.value:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply operator '{ctx.NOT().getText()}' to operands of type '{expr_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return expr_type
        elif ctx.MINUS():  
            expr_type = self.check_primary_expression_type(ctx.primaryExpression())  
            if expr_type != KotlinTypes.INT.value:
                self.semantic_error_listener.semantic_error(
                    msg = f"Cannot apply operator '{ctx.MINUS().getText()}' to operands of type '{expr_type}' in expression '{ctx.getText()}'", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return "None"
            return expr_type
        else:
            return self.check_membership_expression_type(ctx.membershipExpression())


    def check_membership_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the membership expression {ctx.getText()}.")
        
        if ctx.rangeExpression():
            if ctx.primaryExpression().IDENTIFIER():
                identifier = ctx.primaryExpression().IDENTIFIER()
                var_name = self.visit_identifier(identifier)
            
                if not self.check_variable_already_declared(ctx, var_name): 
                    return "None"
                else:
                    left_type = self.check_primary_expression_type(ctx.primaryExpression())
                    var_type, is_mutable = self.symbol_table.get_variable_info(var_name)
                    if var_type != KotlinTypes.INT.value:
                        self.semantic_error_listener.semantic_error(
                            msg = f"The left-hand side of the 'in' operator must be Int, found {left_type} instead.", 
                            line = ctx.start.line, 
                            column = ctx.start.column
                        )
                        return left_type
                    if is_mutable == False:
                        self.semantic_error_listener.semantic_error(
                            msg = f"The left-hand side of the 'in' operator must be mutable.", 
                            line = ctx.start.line, 
                            column = ctx.start.column
                        )
                        return left_type
                    self.check_range_expression(ctx.rangeExpression())
                    return KotlinTypes.BOOLEAN.value 
            else:
                left_type = self.check_primary_expression_type(ctx.primaryExpression())
                self.semantic_error_listener.semantic_error(
                    msg = f"The left-hand side of the 'in' operator must be a variable.", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return left_type
        else:
            left_type = self.check_primary_expression_type(ctx.primaryExpression())
            return left_type
    

    def check_range_expression(self, ctx):
        print(f"    🔍 Checking the type of the range expression {ctx.getText()}.")
        
        left_type = self.check_additive_expression_type(ctx.additiveExpression(0))
        
        if not ctx.additiveExpression(1):
            self.semantic_error_listener.semantic_error(
                msg = f"The for loop requires a range in the iteration condition, but found {left_type}.",
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return "None"

        right_type = self.check_additive_expression_type(ctx.additiveExpression(1))
        
        if left_type != KotlinTypes.INT.value or right_type != KotlinTypes.INT.value:
            self.semantic_error_listener.semantic_error(
                msg = f"The range operator '..' is only supported for Int types, found {left_type} and {right_type} instead.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
        return "None"


    def check_primary_expression_type(self, ctx):
        print(f"    🔍 Checking the type of the primary expression {ctx.getText()}.")
        
        if ctx.IDENTIFIER():
            identifier = self.visit_identifier(ctx.IDENTIFIER())        
            if not self.check_variable_already_declared(ctx=ctx, var_name=identifier):        
                return "None"
            var_type, _ = self.symbol_table.get_variable_info(identifier)
            return var_type
        elif ctx.LEFT_ROUND_BRACKET() and ctx.RIGHT_ROUND_BRACKET():
            return self.check_expression_type(ctx=ctx.expression())
        elif ctx.literal():
            return self.check_literal_type(ctx=ctx.literal())
        elif ctx.callExpression():
            return self.check_call_expression(ctx.callExpression())
        else:
            self.semantic_error_listener.semantic_error(
                msg = f"Unsupported expression type for expression '{ctx.getText()}'.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return "None"


    def check_literal_type(self, ctx):
        print(f"    🔍 Checking the type of the literal expression {ctx.getText()}.")
        
        literal = ctx.getText()
        if literal.isdigit():
            return KotlinTypes.INT.value
        elif literal.startswith('"') and literal.endswith('"'): 
            return KotlinTypes.STRING.value
        elif literal == 'true' or literal == 'false':
            return KotlinTypes.BOOLEAN.value
        else:
            self.semantic_error_listener.semantic_error(
                msg = f"Unsupported expression type for variable '{literal}'.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return "None"


    def check_parameter_type_list(self, ctx):
        print(f"    🔍 Checking the type of the parameters list {ctx.getText()}.")
        
        return ", ".join([self.check_parameter_type(param) for param in ctx.parameter() if self.check_parameter_type(param) is not None])


    def check_parameter_type(self, ctx):      
        print(f"    🔍 Checking the type of the parameter {ctx.getText()}.")  
        
        kotlin_param_type = ctx.type_().getText()
        if not self.check_supported_type(ctx=ctx, type=kotlin_param_type):
            return None
        return kotlin_param_type
    
    
    def check_duplicate_parameters(self, ctx, fun_name):
        print(f"    🔍 Checking for duplicate parameters in function {fun_name}.")
        
        parameter_list = [param.strip() for param in self.check_parameter_name_list(ctx).split(", ")]
        params_seen = set() # non-duplicated params
        duplicate_params = []

        for param in parameter_list:
            if param in params_seen:
                duplicate_params.append(param)
            else:
                params_seen.add(param)
        if duplicate_params:
            duplicates = ", ".join(duplicate_params)
            self.semantic_error_listener.semantic_error(
                msg=f"Function '{fun_name}' has duplicate parameters: {duplicates}.",
                line=ctx.start.line,
                column=ctx.start.column,
            )
            return False

        return True


    def check_parameter_name_list(self, ctx):
        print(f"    🔍 Checking the name of the parameters list {ctx.getText()}.")
        
        return ", ".join([self.check_parameter_name(param) for param in ctx.parameter()])


    def check_parameter_name(self, ctx):    
        print(f"    🔍 Checking the name of the parameter {ctx.getText()}.")
        
        param_name = self.visit_identifier(ctx.IDENTIFIER())
        return param_name
    

    def check_parameter_name_value_list(self, ctx):
        print(f"    🔍 Checking the value of the parameters list {ctx.getText()}.")
        
        return ", ".join([self.check_parameter_name_value(param) for param in ctx.parameter() if self.check_parameter_name_value(param) is not None])


    def check_parameter_name_value(self, ctx):   
        print(f"    🔍 Checking the value of the parameter {ctx.getText()}.")    
        
        param_name = self.visit_identifier(ctx.IDENTIFIER())
        param_value = self.visit_expression(ctx.expression()) if (ctx.expression()) else None 
        return f"{param_name}: {param_value}"
    

    def check_function_not_declared_in_current_scope(self, ctx, fun_name, argument_types):
        print(f"    🔍 Checking if function {fun_name} is not declared in currrent scope.")
        
        if not self.symbol_table.lookup_function(fun_name, argument_types):
            self.semantic_error_listener.semantic_error(
                msg = f"Trying to call function '{fun_name}' with signature '{argument_types}' before its declaration." if argument_types 
                        else f"Trying to call function '{fun_name}' before its declaration.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return True
        return False


    def check_function_already_declared_in_current_scope(self, ctx, fun_name, kotlin_param_types):
        print(f"    🔍 Checking if function {fun_name} is already declared in currrent scope.")
        
        if self.symbol_table.lookup_function(fun_name, kotlin_param_types):
            self.semantic_error_listener.semantic_error(
                msg = f"Function '{fun_name}' with signature '{kotlin_param_types}' is already declared in the current scope." if kotlin_param_types
                        else f"Function '{fun_name}' is already declared in the current scope.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return True
        return False
        

    def check_call_expression(self, ctx):
        print(f"    🔍 Checking call expression {ctx.getText()}.")
        
        fun_name = ctx.IDENTIFIER().getText()
        argument_types = self.check_argument_type_list(ctx.argumentList()) if ctx.argumentList() else None

        if self.check_function_not_declared_in_current_scope(ctx, fun_name, argument_types):
            return "None"
        
        return_type = self.symbol_table.get_function_return_type(fun_name, argument_types)        
        if not return_type:
            self.semantic_error_listener.semantic_error(
                msg = f"Trying to assign the result of function '{fun_name}', which does not return any value.",
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return "None"
        
        return return_type
    
    
    def check_argument_type_list(self, ctx):
        print(f"    🔍 Checking the type of the arguments list {ctx.getText()}.")
        
        return ", ".join([self.check_argument_type(argument) for argument in ctx.argument()])       
    

    def check_argument_type(self, ctx):
        print(f"    🔍 Checking the type of the argument {ctx.getText()}.")
        
        return self.check_expression_type(ctx.expression())


    def check_argument_name_list(self, ctx):
        print(f"    🔍 Checking the name of the arguments list {ctx.getText()}.")
        
        return ", ".join([self.check_argument_name(argument) for argument in ctx.argument()])       
    

    def check_argument_name(self, ctx):
        print(f"    🔍 Checking the name of the argument {ctx.getText()}.")
        
        argument_name = self.visit_identifier(ctx.IDENTIFIER()) if (ctx.IDENTIFIER()) else "None"
        return argument_name


    def check_return_statement(self, ctx, fun_name, fun_return_type):
        print(f"    🔍 Checking the return statement of the function {fun_name}.")
        
        # Iterate over all statements in the function body and check for return statements
        if fun_return_type:
            if not ctx.statement():
                # If no return statement is found and a return type is expected
                self.semantic_error_listener.semantic_error(
                    msg = f"Function '{fun_name}' must have a return statement.", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return False
            else:            
                for stmt in ctx.statement():
                    if stmt.returnStatement():
                        return_stmt = stmt.returnStatement()
                        return self.validate_return_statement(return_stmt, fun_name, fun_return_type) 
                for stmt in ctx.statement():
                    if stmt.forStatement():
                        for_stmt = stmt.forStatement()
                        return self.check_return_statement_in_for_statement(for_stmt, fun_name, fun_return_type) 
                for stmt in ctx.statement():
                    if stmt.ifElseStatement():
                        if_stmt = stmt.ifElseStatement()
                        return self.check_return_statement_in_if_else_statement(if_stmt, fun_name, fun_return_type) 
                # Return statement not found
                self.semantic_error_listener.semantic_error(
                    msg = f"Function '{fun_name}' must have a return statement.", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return False
        else:
            for stmt in ctx.statement():
                if stmt.returnStatement():
                    self.semantic_error_listener.semantic_error(
                        msg = f"Function '{fun_name}' has no return type, but includes a return statement.", 
                        line = ctx.start.line,  
                        column = ctx.start.column
                    )
                    return False
            for stmt in ctx.statement():
                if stmt.forStatement():
                    for_stmt = stmt.forStatement()
                    return self.check_no_return_statement_in_for_statement(for_stmt, fun_name)
            for stmt in ctx.statement():
                if stmt.ifElseStatement():
                    if_stmt = stmt.ifElseStatement()
                    return self.check_no_return_statement_in_if_else_statement(if_stmt, fun_name)
        return True    
    

    def check_return_statement_in_for_statement(self, ctx, fun_name, fun_return_type):
        print(f"    🔍 Checking the return statement of the function {fun_name} in for statement.")
        
        if ctx.block(): 
            block = ctx.block()
            for stmt in block.statement():
                if stmt.returnStatement():
                    return_stmt = stmt.returnStatement()
                    return self.validate_return_statement(return_stmt, fun_name, fun_return_type) 
        else:  
            stmt = ctx.statement()
            if stmt.returnStatement():
                return_stmt = stmt.returnStatement()
                return self.validate_return_statement(return_stmt, fun_name, fun_return_type) 
            
    
    def check_return_statement_in_if_else_statement(self, ctx, fun_name, fun_return_type):
        print(f"    🔍 Checking the return statement of the function {fun_name} in if-else statement.")
        
        if_body = ctx.ifBody()
        check_if = self.check_return_statement_in_if_else_body(if_body, fun_name, fun_return_type)

        if ctx.ELSE():
            else_body = ctx.elseBody()
            check_else = self.check_return_statement_in_if_else_body(else_body, fun_name, fun_return_type)
            return check_if and check_else
        
        return check_if


    def check_return_statement_in_if_else_body(self, ctx, fun_name, fun_return_type):
        print(f"    🔍 Checking the return statement of the function {fun_name} in if-else body.")
        
        if ctx.block(): 
            block = ctx.block()
            for stmt in block.statement():
                if stmt.returnStatement():
                    return_stmt = stmt.returnStatement()
                    return self.validate_return_statement(return_stmt, fun_name, fun_return_type)
        else:  
            stmt = ctx.statement()
            if stmt.returnStatement():
                return_stmt = stmt.returnStatement()
                return self.validate_return_statement(return_stmt, fun_name, fun_return_type) 
        self.semantic_error_listener.semantic_error(
            msg = f"Function '{fun_name}' must have a return statement.", 
            line = ctx.start.line,  
            column = ctx.start.column
        )
        return False


    def check_no_return_statement_in_for_statement(self, ctx, fun_name):
        print(f"    🔍 Checking missing return statement of the function {fun_name} in for statement.")
        
        if ctx.block(): 
            block = ctx.block()
            for stmt in block.statement():
                if stmt.returnStatement():
                    self.semantic_error_listener.semantic_error(
                        msg = f"Function '{fun_name}' has no return type, but includes a return statement.", 
                        line = ctx.start.line,  
                        column = ctx.start.column
                    )
                    return False
        else:  
            stmt = ctx.statement()
            if stmt.returnStatement():
                    self.semantic_error_listener.semantic_error(
                        msg = f"Function '{fun_name}' has no return type, but includes a return statement.", 
                        line = ctx.start.line,  
                        column = ctx.start.column
                    )
                    return False
        return True  


    def check_no_return_statement_in_if_else_statement(self, ctx, fun_name): 
        print(f"    🔍 Checking missing return statement of the function {fun_name} in if-else statement.")
        
        if_body = ctx.ifBody()
        check_if = self.check_no_return_statement_in_if_else_body(if_body, fun_name)

        if ctx.ELSE():
            else_body = ctx.elseBody()
            check_else = self.check_no_return_statement_in_if_else_body(else_body, fun_name)
            return check_if and check_else
        
        return check_if 


    def check_no_return_statement_in_if_else_body(self, ctx, fun_name):
        print(f"    🔍 Checking missing return statement of the function {fun_name} in if-else body.")
        
        if ctx.block(): 
            block = ctx.block()
            for stmt in block.statement():
                if stmt.returnStatement():
                    self.semantic_error_listener.semantic_error(
                        msg = f"Function '{fun_name}' has no return type, but includes a return statement.", 
                        line = ctx.start.line,  
                        column = ctx.start.column
                    )
                    return False
        else:  
            stmt = ctx.statement()
            if stmt.returnStatement():
                self.semantic_error_listener.semantic_error(
                    msg = f"Function '{fun_name}' has no return type, but includes a return statement.", 
                    line = ctx.start.line,  
                    column = ctx.start.column
                )
                return False
        return True  


    def validate_return_statement(self, ctx, fun_name, fun_return_type):
        print(f"    🔍 Validating return statement of the function {fun_name}.")
        
        return_expression = ctx.expression()
        if return_expression:
            if not self.validate_value(ctx=ctx, type=fun_return_type):
                actual_return_type = self.check_expression_type(return_expression)
                self.semantic_error_listener.semantic_error(
                    msg = f"Return type mismatch: Function '{fun_name}' is declared to return type '{fun_return_type}', but the actual return type is '{actual_return_type}'.", 
                    line = ctx.start.line, 
                    column = ctx.start.column
                )
                return False
        else:
            # Found a return statement without any expression
            self.semantic_error_listener.semantic_error(
                msg = f"Function '{fun_name}' must have a return statement of type {fun_return_type}.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return False
        return True  
    

    def check_arguments(self, ctx, fun_name):
        print(f"    🔍 Checking arguments of function {fun_name}.")
        
        return (self.check_argument_types(ctx, fun_name) and self.check_argument_names(ctx, fun_name))


    def check_argument_types(self, ctx, fun_name):
        print(f"    🔍 Checking types of arguments of the function {fun_name}.")
        
        argument_types = self.check_argument_type_list(ctx.argumentList()) 
        
        if self.check_function_not_declared_in_current_scope(ctx = ctx, fun_name = fun_name, argument_types=argument_types):        
            return False
        function_versions = self.symbol_table.get_function_params(fun_name)
        
        if not function_versions:
            self.semantic_error_listener.semantic_error(
                msg=f"Function '{fun_name}' with argument types {argument_types} is not declared in any scope.",
                line=ctx.start.line,
                column=ctx.start.column,
            )
            return False            
        
        # Check if there is a version of the function that matches the provided arguments
        for fun in function_versions:
            param_types = fun["param_types"]
            
            # Check if the number of parameters matches
            if len(param_types) != len(argument_types):
                continue  # They don't match, try the next version of the function

            # Check if the parameter types match
            match = True
            for param_type, arg_type in zip(param_types, argument_types):
                if param_type != arg_type:
                    match = False
                    break
            
            if match:
                return True  # Found a match

        # If no matches are found
        self.semantic_error_listener.semantic_error(
            msg=f"Function '{fun_name}' with argument types {argument_types} does not match any signature in the current scope.",
            line=ctx.start.line,
            column=ctx.start.column,
        )
        return False 
 

    def check_argument_names(self, ctx, fun_name):
        print(f"    🔍 Checking names of arguments of the function {fun_name}.")
        
        argument_names = self.check_argument_name_list(ctx.argumentList())
        argument_names_list = argument_names.split(", ")

        function_versions = self.symbol_table.get_function_params(fun_name)    

        if not function_versions:
            self.semantic_error_listener.semantic_error(
                msg=f"Function '{fun_name}' with argument names {argument_names} is not declared in any scope.",
                line=ctx.start.line,
                column=ctx.start.column,
            )
            return False            

        # Check if there is a version of the function that matches the provided argument names
        for fun in function_versions:

            param_names = fun["param_names"]  # Assuming you have stored parameter names in the function definitions
            param_names_list = param_names.split(", ")

            # Check if the number of parameters matches
            if len(param_names_list) != len(argument_names_list):
                continue  # They don't match, try the next version of the function
            
            # Check if the parameter names match
            match = True

            for param_name, arg_name in zip(param_names_list, argument_names_list):
                if arg_name != "None" and param_name != arg_name:
                    match = False
                    break
            
            if match:
                return True  # Found a match
        
        # If no matches are found
        self.semantic_error_listener.semantic_error(
            msg=f"Function '{fun_name}' with argument names {argument_names} does not match any signature in the current scope.",
            line=ctx.start.line,
            column=ctx.start.column,
        )
        return False


    def check_class_already_declared_in_current_scope(self, ctx, class_name):
        print(f"    🔍 Checking if class {class_name} is already declared in the current scope.")
        
        if self.symbol_table.lookup_class(class_name):
            self.semantic_error_listener.semantic_error(
                msg = f"Class '{class_name}' is already declared in the current scope.",
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return True
        return False