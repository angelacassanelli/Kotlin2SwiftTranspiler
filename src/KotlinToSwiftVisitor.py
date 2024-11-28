from antlr4 import ParseTreeVisitor
from generated.antlr.KotlinParser import KotlinParser
from Symbol import Symbol
from Types import SwiftTypes, KotlinTypes
from Utils import KOTLIN_2_SWIFT_TYPES, RESERVED_KEYWORDS


class KotlinToSwiftVisitor(ParseTreeVisitor):
    """Transforms Kotlin code into Swift code. This class extends ParseTreeVisitor 
    to traverse the parse tree generated by the Kotlin parser and converts 
    Kotlin statements into their Swift equivalents."""
    
    def __init__(self, symbol_table, semantic_error_listener):        
        self.symbol_table = symbol_table
        self.semantic_error_listener = semantic_error_listener        
        self.kotlin_2_swift_types = KOTLIN_2_SWIFT_TYPES
        self.reserved_keywords = RESERVED_KEYWORDS


    def visit_program(self, ctx):
        # Visits the program node, iterating over top-level statements and joining them into a single Swift program.
        print(f"Visiting program: {ctx.getText()}")
        statements = [self.visit_top_level_statement(stmt) for stmt in ctx.topLevelStatement()]
        return "\n".join(filter(None, statements))
    

    def visit_top_level_statement(self, ctx):
        # Handles different types of top-level statements and directs to specific visit methods.
        print(f"Visiting top level statement: {ctx.getText()}")
        if ctx.classDeclaration():
            return self.visit_class_declaration(ctx.classDeclaration())
        elif ctx.commentStatement():
            return self.visit_comment_statement(ctx.commentStatement())     
        else: 
            print(f"Unrecognized statement: {ctx.getText()}")
            return ""


    def visit_statement(self, ctx):
        # Handles various types of statements like read, print, if, for, etc.
        print(f"Visiting statement: {ctx.getText()}")
        if ctx.readStatement():
            return self.visit_read_statement(ctx.readStatement())
        elif ctx.printStatement():
            return self.visit_print_statement(ctx.printStatement())
        elif ctx.ifStatement():
            return self.visit_if_statement(ctx.ifStatement())
        elif ctx.forStatement():
            return self.visit_for_statement(ctx.forStatement())
        elif ctx.assignmentStatement():
            return self.visit_assignment_statement(ctx.assignmentStatement())
        elif ctx.varDeclaration(): 
            return self.visit_var_declaration(ctx.varDeclaration())
        elif ctx.returnStatement():
            return self.visit_return_statement(ctx.returnStatement())
        elif ctx.commentStatement():
            return self.visitComment(ctx.commentStatement())        
        else: 
            print(f"Unrecognized statement: {ctx.getText()}")
            return ""


    def visit_block(self, ctx):
        # Visits a block of statements and joins them with newlines.
        print(f"Visiting block: {ctx.getText()}")        
        for stmt in ctx.statement():
            print(stmt.getText()) 
        statements = [self.visit_statement(stmt) for stmt in ctx.statement()]
        return "\n".join(filter(None, statements))
        

    def visit_read_statement(self, ctx):
        # Converts a Kotlin readLine statement to Swift, handling optional var/val keyword.
        print(f"Visiting read statement: {ctx.getText()}")
        identifier = self.visit_identifier(ctx.IDENTIFIER())
        return f"{identifier} = readLine()"
    

    def visit_print_statement(self, ctx):
        # Converts a Kotlin print statement to a Swift print statement.
        print(f"Visiting print statement: {ctx.getText()}")
        expression = self.visit_expression(ctx.expression())
        return f"print({expression})"
    

    def visit_if_statement(self, ctx):
        # Converts a Kotlin if-else statement to Swift. The else block is optional.
        print(f"Visiting if statement: {ctx.getText()}")
        condition = self.visit_expression(ctx.expression())
        if ctx.block(0): 
            body = self.visit_block(ctx.block(0))
        else:  
            body = self.visit_statement(ctx.statement(0))
        if ctx.ELSE():
            if ctx.block(1): 
                else_body = self.visit_block(ctx.block(1))
            else:
                else_body = self.visit_statement(ctx.statement(1))
            return f"if {condition} {{ {body} }} else {{ {else_body} }}"

        return f"if {condition} {{ {body} }}"


    def visit_for_statement(self, ctx):
        # Converts a Kotlin for loop with a range to a Swift-compatible loop.
        print(f"Visiting for statement: {ctx.getText()}")
        expression = self.visit_memebership_expression(ctx.membershipExpression())
        if ctx.block(): 
            body = self.visit_block(ctx.block())
        else:  
            body = self.visit_statement(ctx.statement())
        return f"for {expression} {{ {body} }}"


    def visit_assignment_statement(self, ctx):
        # Converts Kotlin variable assignment to Swift.
        print(f"Visiting assignment statement: {ctx.getText()}")
        var_name = self.visit_identifier(ctx.IDENTIFIER())

        # Check if variable is declared
        symbol = self.symbol_table.lookup_symbol(var_name)
        if symbol is None:
            self.semantic_error_listener.semantic_error(
                msg = f"Variable '{var_name}' is not declared in any scope.", 
                line = ctx.start.line, 
                column = ctx.start.column
            )
            return
        else:
            var_value = self.visit_expression(ctx.expression())
            self.symbol_table.update_symbol(name=var_name, new_value=var_value)

            return f"{var_name} = {var_value}"
        

    def visit_var_declaration(self, ctx):
        # Converts a Kotlin 'var' declaration to Swift, including type and optional initialization.
        print(f"Visiting var declaration: {ctx.getText()}")
        
        var_name = self.visit_identifier(ctx.IDENTIFIER())        
        mutable, keyword = (False, "let") if ctx.VAL() else (True, "var")

        # Check if the variable is already declared
        if self.check_variable_already_declared(ctx = ctx, var_name = var_name):
            return
        else:
            # Unsupported type check
            kotlin_type = ctx.type_().getText()
            if not self.check_supported_type(ctx = ctx, type=kotlin_type):
                return

            # Mismatch type check, if variable is assigned            
            var_value = self.visit_expression(ctx.expression()) if ctx.expression() else None            
            if not self.validate_value(ctx=ctx, value=var_value, type=kotlin_type):
                return
            
            # Add the variable to the symbol table
            self.add_variable_to_symbol_table(var_name=var_name, type=kotlin_type, mutable=mutable)
            
            swift_type = self.visit_type(ctx.type_()) 
            swift_var_declaration = f"{keyword} {var_name}: {swift_type}"
            if var_value:
                swift_var_declaration += f" = {var_value}"
            return swift_var_declaration        


    def visit_function_declaration(self, ctx):
        # Transforms a Kotlin function declaration into a Swift function declaration.
        print(f"Visiting function declaration: {ctx.getText()}")
        self.symbol_table.add_scope()

        func_name = self.visit_identifier(ctx.IDENTIFIER())
        parameters = self.visit_parameter_list(ctx.parameterList()) if ctx.parameterList() else ""
        body = self.visit_block(ctx.block())
        if ctx.type_():
            return_type = self.visit_type(ctx.type_()) 
            return f"func {func_name}({parameters}) -> {return_type} {{ {body} }}"
        
        self.symbol_table.remove_scope()
        return f"func {func_name}({parameters}) {{ {body} }}"


    def visit_return_statement(self, ctx):
        # Handles 'return' statements in Kotlin.
        print(f"Visiting return statement: {ctx.getText()}")            
        if ctx.expression():
            expression = self.visit_expression(ctx.expression())
            return f"return {expression}"
        return "return"


    def visit_class_declaration(self, ctx):
        # Converts a Kotlin class declaration into a Swift class declaration.
        print(f"Visiting class declaration: {ctx.getText()}")
        self.symbol_table.add_scope()

        class_name = self.visit_identifier(ctx.IDENTIFIER())
        body = self.visit_class_body(ctx.classBody()) if ctx.classBody() else ""
        has_parentheses = ctx.LEFT_ROUND_BRACKET() is not None and ctx.RIGHT_ROUND_BRACKET() is not None                    
        if ctx.propertyList():        
            propertyList = self.visit_property_list(ctx.propertyList())
            properties_declarations = "\n".join([
                f"{property['keyword']} {property['name']}: {property['type']}"
                for property in propertyList
            ])
            properties_assignments = "\n".join([
                f"self.{property["name"]} = {property["name"]}"
                for property in propertyList
            ])
            constructor_params = ", ".join([
                f"{property['name']}: {property['type']}" +
                (f" = {property['value']}" if property['value'] is not None else "")
                for property in propertyList
            ])
            constructor = f"init({constructor_params}) {{\n{properties_assignments}\n}}"
            class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
            return f"{class_declaration} {{\n{properties_declarations}\n{constructor}\n{body}\n}}"
        elif ctx.parameterList():
            constructor_params = self.visit_parameter_list(ctx.parameterList())
            constructor = f"init({constructor_params}) {{}}"
            class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
            return f"{class_declaration} {{\n{constructor}\n{body}\n}}"
        class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
        
        self.symbol_table.remove_scope()
        return f"{class_declaration} {{\n{body}\n}}"
    

    def visit_class_body(self, ctx):
        # Handles the body of a Kotlin class, converting its statements.
        print(f"Visiting class body: {ctx.getText()}")
        statements = []
        if ctx.children:
            for stmt in ctx.children:
                if isinstance(stmt, KotlinParser.VarDeclarationContext):
                    statements.append(self.visit_var_declaration(stmt))
                elif isinstance(stmt, KotlinParser.AssignmentStatementContext):
                    statements.append(self.visit_assignment_statement(stmt))
                elif isinstance(stmt, KotlinParser.FunctionDeclarationContext):
                    statements.append(self.visit_function_declaration(stmt))
                elif isinstance(stmt, KotlinParser.CommentStatementContext):
                    statements.append(self.visit_comment_statement(stmt))
        return "\n".join(filter(None, statements))


    def visit_property_list(self, ctx):
        # Converts a list of Kotlin properties into Swift properties.
        print(f"Visiting property list: {ctx.getText()}")
        return [self.visit_property(property) for property in ctx.property_()]


    def visit_property(self, ctx):
        # Converts a Kotlin property into a Swift property.
        print(f"Visiting property: {ctx.getText()}")
        return self.visit_var_declaration(ctx.varDeclaration())
    

    def visit_parameter_list(self, ctx):
        # Converts a list of Kotlin parameters into Swift parameters.
        print(f"Visiting parameter list: {ctx.getText()}")
        return ", ".join([self.visit_parameter(param) for param in ctx.parameter()])
    

    def visit_parameter(self, ctx):
        # Converts a Kotlin parameter into a Swift parameter.
        print(f"Visiting parameter: {ctx.getText()}")
        param_name = self.visit_identifier(ctx.IDENTIFIER())
        param_type = self.visit_type(ctx.type_()) 
        if (ctx.expression()):
            param_value = self.visit_expression(ctx.expression()) 
            return f"{param_name}: {param_type} = {param_value}"
        return f"{param_name}: {param_type}"


    def visit_argument_list(self, ctx):
        # Converts a list of Kotlin arguments into Swift arguments.
        print(f"Visiting argument list: {ctx.getText()}")
        return ", ".join([self.visit_argument(argument) for argument in ctx.argument()])
    

    def visit_argument(self, ctx):
        # Converts a Kotlin argument into a Swift argument.
        print(f"Visiting argument: {ctx.getText()}")
        argument_value = self.visit_expression(ctx.expression()) 
        if (ctx.IDENTIFIER()):
            argument_name = self.visit_identifier(ctx.IDENTIFIER())
            return f"{argument_name}: {argument_value}"
        return f"{argument_value}"


    def visit_expression(self, ctx: KotlinParser.ExpressionContext):
        # Handles the transformation of expressions such as literals, identifiers, and operators.
        print(f"Visiting expression: {ctx.getText()}")
        return self.visit_logical_or_expression(ctx.logicalOrExpression())  


    def visit_logical_or_expression(self, ctx: KotlinParser.LogicalOrExpressionContext):
        # Handles logical OR expressions in Kotlin (i.e., a || b).
        print(f"Visiting logical OR expression: {ctx.getText()}")
        left = self.visit_logical_and_expression(ctx.logicalAndExpression(0))
        for i in range(1, len(ctx.logicalAndExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_logical_and_expression(ctx.logicalAndExpression(i))
            left = f"{left} {operator} {right}" if right is not None else f"{left}"
        return f"{left}"
    

    def visit_logical_and_expression(self, ctx: KotlinParser.LogicalAndExpressionContext):
        # Handles logical AND expressions in Kotlin (i.e., a && b).
        print(f"Visiting logical AND expression: {ctx.getText()}")
        left = self.visit_equality_expression(ctx.equalityExpression(0))  
        for i in range(1, len(ctx.equalityExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_equality_expression(ctx.equalityExpression(i)) 
            left = f"{left} {operator} {right}"
        return f"{left}"


    def visit_equality_expression(self, ctx: KotlinParser.EqualityExpressionContext):
        # Handles equality expressions in Kotlin (i.e., a == b or a != b).
        print(f"Visiting equality expression: {ctx.getText()}")
        left = self.visit_relational_expression(ctx.relationalExpression(0))
        for i in range(1, len(ctx.relationalExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_relational_expression(ctx.relationalExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}"


    def visit_relational_expression(self, ctx: KotlinParser.RelationalExpressionContext):
        # Handles relational expressions in Kotlin (e.g., a < b, a > b, etc.).
        print(f"Visiting relational expression: {ctx.getText()}")
        left = self.visit_additive_expression(ctx.additiveExpression(0))
        if len(ctx.additiveExpression()) > 1:
            operator = ctx.getChild(1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_additive_expression(ctx.additiveExpression(1))
            return f"{left} {operator} {right}" 
        return f"{left}"


    def visit_additive_expression(self, ctx: KotlinParser.AdditiveExpressionContext):
        # Handles additive expressions in Kotlin (i.e., a + b or a - b).
        print(f"Visiting additive expression: {ctx.getText()}")
        left = self.visit_multiplicative_expression(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_multiplicative_expression(ctx.multiplicativeExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}"  


    def visit_multiplicative_expression(self, ctx: KotlinParser.MultiplicativeExpressionContext):
        # Handles multiplicative expressions in Kotlin (i.e., a * b, a / b, or a % b).
        print(f"Visiting multiplicative expression: {ctx.getText()}")
        left = self.visit_unary_expression(ctx.unaryExpression(0))
        for i in range(1, len(ctx.unaryExpression())):
            operator = ctx.getChild(2 * i - 1).getText()  # Gli operatori sono al posto 2*i-1 (MULT, DIV, MOD)
            right = self.visit_unary_expression(ctx.unaryExpression(i))  # Visita il prossimo unary expression
            left = f"{left} {operator} {right}"  # Combina il risultato precedente con l'operatore corrente
        return f"{left}" 


    def visit_unary_expression(self, ctx: KotlinParser.UnaryExpressionContext):
        # Handles unary expressions in Kotlin (i.e., !a or -a).
        print(f"Visiting unary expression: {ctx.getText()}")
        if ctx.NOT(): 
            return f"!{self.visit_primary_expression(ctx.primaryExpression())}"
        elif ctx.MINUS():
            return f"-{self.visit_primary_expression(ctx.primaryExpression())}"
        else:
            return f"{self.visit_memebership_expression(ctx.membershipExpression())}"


    def visit_memebership_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        # Handles membership expressions in Kotlin (i.e., a in b or a !in b).
        print(f"Visiting membership expression: {ctx.getText()}")
        left = self.visit_primary_expression(ctx.primaryExpression())
        if ctx.rangeExpression():
            right = self.visit_range_expression(ctx.rangeExpression()) 
            if ctx.NOT() and ctx.IN():
                return f"{left} !in {right}"
            elif ctx.IN():
                return f"{left} in {right}"
        return f"{left}"
    

    def visit_primary_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        # Handles primary expressions in Kotlin (e.g., literals, identifiers, or call expressions).
        print(f"Visiting primary expression: {ctx.getText()}")
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()  
        elif ctx.LEFT_ROUND_BRACKET() and ctx.RIGHT_ROUND_BRACKET():
            return f"({self.visit_expression(ctx.expression())})"  
        elif ctx.callExpression():
            return self.visit_call_expression(ctx.callExpression())
        elif ctx.literal():
            return self.visit_literal(ctx.literal())


    def visit_range_expression(self, ctx: KotlinParser.PrimaryExpressionContext):
        # Handles range expressions in Kotlin (e.g., a..b).
        print(f"Visiting range expression: {ctx.getText()}")
        left = self.visit_additive_expression(ctx.additiveExpression(0))
        right = self.visit_additive_expression(ctx.additiveExpression(1))        
        return f"{left} ... {right}"


    def visit_call_expression(self, ctx):
        # Handles function call expressions in Kotlin.
        print(f"Visiting call expression: {ctx.getText()}")
        func_name = self.visit_identifier(ctx.IDENTIFIER())
        arguments = self.visit_argument_list(ctx.argumentList()) if ctx.argumentList() else ""
        return f"{func_name}({arguments})"


    def visit_literal(self, ctx):
        # Handles literal expressions in Kotlin (e.g., string, integer, boolean).
        print(f"Visiting literal: {ctx.getText()}")
        return ctx.getText()


    def visit_comment_statement(self, ctx):
        # Converts Kotlin comments to Swift comments.
        print(f"Visiting comment: {ctx.getText()}")
        if ctx.LINE_COMMENT():
            return self.visit_line_comment(ctx.LINE_COMMENT())
        elif ctx.BLOCK_COMMENT():
            return self.visit_block_comment(ctx.BLOCK_COMMENT())
        else:
            return ""
    

    def visit_line_comment(self, ctx):
        # Converts Kotlin inline comments to Swift comments.
        print(f"Visiting inline comment: {ctx.getText()}")
        comment = ctx.getText()[2:].strip() 
        return f"# {comment}"


    def visit_block_comment(self, ctx):
        # Converts Kotlin block comments to Swift comments.
        print(f"Visiting block comment: {ctx.getText()}")
        comment = ctx.getText()[2:-2].strip() 
        return f"/* {comment} */"    


    def visit_type(self, ctx): 
        # Converts Kotlin types to Swift types.
        print(f"Visiting type: {ctx.getText()}")
        kotlin_type = ctx.getText()  
        swift_type = self.kotlin_2_swift_types.get(KotlinTypes[kotlin_type.upper()], kotlin_type)  
        return swift_type.value


    def visit_identifier(self, ctx):
        # Handles identifiers, checking if they are reserved keywords.
        print(f"Visiting identifier: {ctx.getText()}")
        identifier_name = ctx.getText()
        if identifier_name in self.reserved_keywords:
            raise ValueError(f"❌ Error: '{identifier_name}' is a reserved keyword and cannot be used as an identifier.")
        return identifier_name


    ##### SEMANTIC CHECKS #####

    def add_variable_to_symbol_table(self, var_name, type, mutable):
        """Adds a variable to the symbol table."""
        symbol = Symbol(name=var_name, type=type, mutable=mutable)
        self.symbol_table.add_symbol(var_name, symbol)


    def infer_value_type(self, value):
        if value.isdigit():
            return KotlinTypes.INT.value
        elif value.startswith('"') and value.endswith('"'): 
            return KotlinTypes.STRING.value
        elif value == 'true' or value == 'false':
            return KotlinTypes.BOOLEAN.value
        else:
            raise ValueError("❌ Unsupported expression type")
        
        
    def check_variable_already_declared(self, ctx, var_name):
        """Checks if the variable is already declared in the current scope."""
        if self.symbol_table.lookup_symbol_in_current_scope(var_name):
            self.semantic_error_listener.semantic_error(
                msg=f"Variable '{var_name}' is already declared in the current scope.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return True
        return False
    
    def check_supported_type(self, ctx, type):
        """Checks if the Kotlin type is supported."""
        if type not in KotlinTypes:
            self.semantic_error_listener.semantic_error(
                f"Unsupported type '{type}' for variable.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return False
        return True

    def validate_value(self, ctx, value, type):
        """Validates the value assigned to the variable and checks for type mismatch."""        
        value_type = self.infer_value_type(value)
        if type != value_type:
            self.semantic_error_listener.semantic_error(
                f"Type mismatch: Variable declared as '{type}' but assigned a value of type '{value_type}'.",
                line=ctx.start.line,
                column=ctx.start.column
            )
            return False
        return True
    