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
        self.symbol_table = symbol_table
        self.semantic_error_listener = semantic_error_listener        
        self.kotlin_2_swift_types = KOTLIN_2_SWIFT_TYPES
        self.reserved_keywords = RESERVED_KEYWORDS


    def visit_program(self, ctx: KotlinParser.ProgramContext):        
        # Visits the program node, iterating over top-level statements and joining them into a single Swift program.
        print("🚀 Visiting Kotlin code...")
        print(f"    🔍 Visiting program: {ctx.getText()}")
        
        if(ctx.topLevelStatement()):
            statements = [self.visit_top_level_statement(stmt) for stmt in ctx.topLevelStatement()]
            return "\n".join(filter(None, statements)) # Joins non-empty strings with a newline separator.
        else:
            raise ValueError(f"    ❌ Invalid top level statement in program.")

    def visit_top_level_statement(self, ctx: KotlinParser.TopLevelStatementContext):
        # Handles different types of top-level statements and directs to specific visit methods.
        print(f"    🔍 Visiting top level statement: {ctx.getText()}")
        
        if ctx.classDeclaration():
            return self.visit_class_declaration(ctx.classDeclaration())
        elif ctx.commentStatement():
            return self.visit_comment_statement(ctx.commentStatement())     
        else: 
            print(f"    ❌ Unrecognized statement: {ctx.getText()}")
            return None


    def visit_class_declaration(self, ctx: KotlinParser.ClassDeclarationContext):
        # Converts a Kotlin class declaration into a Swift class declaration.
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
        # Handles identifiers, checking if they are reserved keywords.
        print(f"    🔍 Visiting identifier: {ctx.getText()}")
        
        identifier_name = ctx.getText()
        if identifier_name in self.reserved_keywords:
            raise ValueError(f"    ❌ '{identifier_name}' is a reserved keyword and cannot be used as an identifier.")
        return identifier_name
    

    def visit_property_list(self, ctx: KotlinParser.PropertyListContext):
        # Converts a list of Kotlin properties into Swift properties.
        print(f"    🔍 Visiting property list: {ctx.getText()}")
        
        return [self.visit_property(property) for property in ctx.property_()]


    def visit_property(self, ctx: KotlinParser.PropertyContext):
        # Converts a Kotlin property into a Swift property.
        print(f"    🔍 Visiting property: {ctx.getText()}")
        
        return self.visit_var_declaration(ctx.varDeclaration())
    

    def visit_parameter_list(self, ctx: KotlinParser.ParameterListContext):
        # Converts a list of Kotlin parameters into Swift parameters.
        print(f"    🔍 Visiting parameter list: {ctx.getText()}")
        
        return ", ".join([self.visit_parameter(param) for param in ctx.parameter()])


    def visit_parameter(self, ctx: KotlinParser.ParameterContext):
        # Converts a Kotlin parameter into a Swift parameter.
        print(f"    🔍 Visiting parameter: {ctx.getText()}")
        
        param_name = self.visit_identifier(ctx.IDENTIFIER())
        param_type = self.visit_type(ctx.type_()) 
        if (ctx.expression()):
            param_value = self.visit_expression(ctx.expression()) 
            return f"{param_name}: {param_type} = {param_value}"
        return f"{param_name}: {param_type}"


    def visit_class_body(self, ctx: KotlinParser.ClassBodyContext):
        # Handles the body of a Kotlin class, converting its statements.
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
        # Converts a Kotlin 'var' declaration to Swift, including type and optional initialization.
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
        # Converts Kotlin types to Swift types.
        print(f"    🔍 Visiting type: {ctx.getText()}")
        
        kotlin_type = ctx.getText()  
        swift_type = self.kotlin_2_swift_types.get(KotlinTypes[kotlin_type.upper()], None)  
        if not swift_type:
            return None
        return swift_type.value   
    

    def visit_assignment_statement(self, ctx: KotlinParser.AssignmentStatementContext):
        # Converts Kotlin variable assignment to Swift.    
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
        # Transforms a Kotlin function declaration into a Swift function declaration.
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
        # Visits a block of statements and joins them with newlines.
        print(f"    🔍 Visiting block: {ctx.getText()}")        
        
        statements = [self.visit_statement(stmt) for stmt in ctx.statement()]
        return "\n".join(filter(None, statements))


    def visit_statement(self, ctx: KotlinParser.StatementContext):
        # Handles various types of statements like read, print, if, for, etc.
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
        # Converts a Kotlin readLine statement to Swift, handling optional var/val keyword.
        
        print(f"    🔍 Visiting read statement: {ctx.getText()}")
        return f"readLine()"
    

    def visit_print_statement(self, ctx: KotlinParser.PrintStatementContext):
        # Converts a Kotlin print statement to a Swift print statement.
        print(f"    🔍 Visiting print statement: {ctx.getText()}")
        
        expression = self.visit_expression(ctx.expression())
        return f"print({expression})"
    

    def visit_if_else_statement(self, ctx: KotlinParser.IfElseStatementContext):
        # Converts the Kotlin if-else body to Swift.
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
        # Converts a Kotlin if-else statement to Swift. The else block is optional.
        print(f"    🔍 Visiting if-else statement: {ctx.getText()}")
        
        return self.visit_block(ctx.block()) if ctx.block() else self.visit_statement(ctx.statement())


    def visit_else_body(self, ctx: KotlinParser.ElseBodyContext):
        # Converts a Kotlin if-else statement to Swift. The else block is optional.
        print(f"    🔍 Visiting if-else statement: {ctx.getText()}")
        
        return self.visit_block(ctx.block()) if ctx.block() else self.visit_statement(ctx.statement())


    def visit_for_statement(self, ctx: KotlinParser.ForStatementContext):
        # Converts a Kotlin for loop with a range to a Swift-compatible loop.
        print(f"    🔍 Visiting for statement: {ctx.getText()}")
        
        self.check_membership_expression_type(ctx.membershipExpression())
        expression = self.visit_memebership_expression(ctx.membershipExpression())
        if ctx.block(): 
            body = self.visit_block(ctx.block())
        else:  
            body = self.visit_statement(ctx.statement())
        return f"for {expression} {{ {body} }}"


    def visit_return_statement(self, ctx: KotlinParser.ReturnStatementContext):
        # Handles 'return' statements in Kotlin.
        print(f"    🔍 Visiting return statement: {ctx.getText()}")            
        if ctx.expression():
            expression = self.visit_expression(ctx.expression())
            return f"return {expression}"
        return "return"   


    def visit_expression(self, ctx: KotlinParser.ExpressionContext):
        # Handles the transformation of expressions such as literals, identifiers, and operators.
        print(f"    🔍 Visiting expression: {ctx.getText()}")
        
        return self.visit_logical_or_expression(ctx.logicalOrExpression())  


    def visit_logical_or_expression(self, ctx: KotlinParser.LogicalOrExpressionContext):
        # Handles logical OR expressions in Kotlin (i.e., a || b).
        print(f"    🔍 Visiting logical OR expression: {ctx.getText()}")
        
        left = self.visit_logical_and_expression(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_logical_and_expression(ctx.logicalAndExpression(i))
            left = f"{left} {operator} {right}" if right is not None else f"{left}" 
        return f"{left}"
    

    def visit_logical_and_expression(self, ctx: KotlinParser.LogicalAndExpressionContext):
        # Handles logical AND expressions in Kotlin (i.e., a && b).
        print(f"    🔍 Visiting logical AND expression: {ctx.getText()}")
        
        left = self.visit_equality_expression(ctx.equalityExpression(0))  
        for i in range(1, len(ctx.equalityExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_equality_expression(ctx.equalityExpression(i)) 
            left = f"{left} {operator} {right}"
        return f"{left}"


    def visit_equality_expression(self, ctx: KotlinParser.EqualityExpressionContext):
        # Handles equality expressions in Kotlin (i.e., a == b or a != b).
        print(f"    🔍 Visiting equality expression: {ctx.getText()}")
        
        left = self.visit_relational_expression(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_relational_expression(ctx.relationalExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}"


    def visit_relational_expression(self, ctx: KotlinParser.RelationalExpressionContext):
        # Handles relational expressions in Kotlin (e.g., a < b, a > b, etc.).
        print(f"    🔍 Visiting relational expression: {ctx.getText()}")
        
        left = self.visit_additive_expression(ctx.additiveExpression(0))
        if len(ctx.additiveExpression()) > 1:
            operator = ctx.getChild(1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_additive_expression(ctx.additiveExpression(1))
            return f"{left} {operator} {right}" 
        return f"{left}"


    def visit_additive_expression(self, ctx: KotlinParser.AdditiveExpressionContext):
        # Handles additive expressions in Kotlin (i.e., a + b or a - b).
        print(f"    🔍 Visiting additive expression: {ctx.getText()}")
        
        left = self.visit_multiplicative_expression(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_multiplicative_expression(ctx.multiplicativeExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}"  


    def visit_multiplicative_expression(self, ctx: KotlinParser.MultiplicativeExpressionContext):
        # Handles multiplicative expressions in Kotlin (i.e., a * b, a / b, or a % b).
        print(f"    🔍 Visiting multiplicative expression: {ctx.getText()}")
        
        left = self.visit_unary_expression(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_unary_expression(ctx.unaryExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}" 


    def visit_unary_expression(self, ctx: KotlinParser.UnaryExpressionContext):
        # Handles unary expressions in Kotlin (i.e., !a or -a).
        print(f"    🔍 Visiting unary expression: {ctx.getText()}")
        
        if ctx.NOT(): 
            return f"!{self.visit_primary_expression(ctx.primaryExpression())}"
        elif ctx.MINUS():
            return f"-{self.visit_primary_expression(ctx.primaryExpression())}"
        else:
            return f"{self.visit_memebership_expression(ctx.membershipExpression())}"


    def visit_memebership_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        # Handles membership expressions in Kotlin (i.e., a in b or a !in b).
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
        # Handles primary expressions in Kotlin (e.g., literals, identifiers, or call expressions).
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
        # Handles range expressions in Kotlin (e.g., a..b).
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
        # Handles function call expressions in Kotlin.
        print(f"    🔍 Visiting call expression: {ctx.getText()}")
        
        fun_name = self.visit_identifier(ctx.IDENTIFIER())

        if ctx.argumentList():    
            if not self.check_arguments(ctx, fun_name): 
                return None
            arguments = self.visit_argument_list(ctx.argumentList()) 
            return f"{fun_name}({arguments})"
        
        return f"{fun_name}()"
    

    def visit_argument_list(self, ctx: KotlinParser.ArgumentListContext):
        # Converts a list of Kotlin arguments into Swift arguments.
        print(f"    🔍 Visiting argument list: {ctx.getText()}")
        
        return ", ".join([self.visit_argument(argument) for argument in ctx.argument()])
    

    def visit_argument(self, ctx: KotlinParser.ArgumentContext):
        # Converts a Kotlin argument into a Swift argument.
        print(f"    🔍 Visiting argument: {ctx.getText()}")
        
        argument_value = self.visit_expression(ctx.expression()) 
        if (ctx.IDENTIFIER()):
            argument_name = self.visit_identifier(ctx.IDENTIFIER())
            return f"{argument_name}: {argument_value}"
        return f"{argument_value}"


    def visit_literal(self, ctx: KotlinParser.LiteralContext):
        # Handles literal expressions in Kotlin (e.g., string, integer, boolean).
        print(f"    🔍 Visiting literal: {ctx.getText()}")
        
        return ctx.getText()


    def visit_comment_statement(self, ctx: KotlinParser.CommentStatementContext):
        # Converts Kotlin comments to Swift comments.
        print(f"    🔍 Visiting comment: {ctx.getText()}")
        if ctx.LINE_COMMENT():
            return self.visit_line_comment(ctx.LINE_COMMENT())
        elif ctx.BLOCK_COMMENT():
            return self.visit_block_comment(ctx.BLOCK_COMMENT())
        else:
            return None
        

    def visit_line_comment(self, ctx: KotlinParser):
        # Converts Kotlin inline comments to Swift comments.
        print(f"    🔍 Visiting inline comment: {ctx.getText()}")
        comment = ctx.getText()[2:].strip() 
        return f"# {comment}"


    def visit_block_comment(self, ctx: KotlinParser):
        # Converts Kotlin block comments to Swift comments.
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