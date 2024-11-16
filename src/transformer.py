from antlr4 import *
from generated.antlr.KotlinParser import KotlinParser

reserved_keywords = {
    "Boolean", "Int", "String", "class", "else", "for", "fun", "if", "return", "val", "var",
    "true", "false", "println", "readLine", 
    ",", ";", ":", ".", "(", ")", "{", "}", "[", "]", 
    "+", "-", "*", "/", "%", "=", "==", "!=", ">", ">=", "<", "<=",
    "&&", "||", "!", "..", "\"", "\'"
}

class KotlinToSwiftTransformer(ParseTreeVisitor):
    """Transforms Kotlin code into Swift code: this class extends the ParseTreeVisitor class 
    to traverse the parse tree generated by the Kotlin parser, containing methods to handle various types 
    of statements and expressions, converting them into their corresponding Swift representations."""

    def __init__(self):
        self.reserved_keywords = reserved_keywords

    kotlin2swiftTypes = {
        "String": "String",
        "Int": "Int",
        "Boolean": "Bool"
    }

    def visitProgram(self, ctx):
        """
        Visits the program node, iterating over statements 
        and joining them into a single Swift program.
        """
        print(f"Visiting program: {ctx.getText()}")
        statements = [self.visitStatement(stmt) for stmt in ctx.statement()]
        return "\n".join(filter(None, statements))

    def visitStatement(self, ctx):
        """Determines the type of statement and directs to the appropriate visit method."""
        print(f"Visiting statement: {ctx.getText()}")
        if ctx.varDeclaration(): 
            return self.visitVarDeclaration(ctx.varDeclaration())
        elif ctx.valDeclaration(): 
            return self.visitValDeclaration(ctx.valDeclaration())
        elif ctx.assignmentStatement():
            return self.visitAssignment(ctx.assignmentStatement())
        elif ctx.printStatement():
            return self.visitPrintStatement(ctx.printStatement())
        elif ctx.readStatement():
            return self.visitReadStatement(ctx.readStatement())
        elif ctx.returnStatement():
            return self.visitReturnStatement(ctx.returnStatement())
        elif ctx.ifStatement():
            return self.visitIfStatement(ctx.ifStatement())
        elif ctx.forStatement():
            return self.visitForStatement(ctx.forStatement())
        elif ctx.functionDeclaration():
            return self.visitFunctionDeclaration(ctx.functionDeclaration())
        elif ctx.classDeclaration():
            return self.visitClassDeclaration(ctx.classDeclaration())
        elif ctx.commentStatement():
            return self.visitComment(ctx.commentStatement())        
        else: 
            print(f"Unrecognized statement: {ctx.getText()}")
            return ""
        
    def visitAssignment(self, ctx):
        """Converts Kotlin variable assignment to Swift"""
        var_name = self.visitIdentifier(ctx.IDENTIFIER())
        var_value = self.visitExpression(ctx.expression())
        return f"{var_name} = {var_value}"

    def visitReturnStatement(self, ctx):
        """Visits a 'return' statement."""
        print(f"Visiting return statement: {ctx.getText()}")            
        if ctx.expression():
            expression = self.visitExpression(ctx.expression())
            return f"return {expression}"
        return "return"

    def visitIdentifier(self, ctx):
        """Checks if the identifier is a reserved keyword and raises an error if so."""
        print(f"Visiting identifier: {ctx.getText()}")
        identifier_name = ctx.getText()
        if identifier_name in self.reserved_keywords:
            raise ValueError(f"Error: '{identifier_name}' is a reserved keyword and cannot be used as an identifier.")
        return identifier_name
    
    def visitVarDeclaration(self, ctx):
        """Converts a Kotlin 'var' declaration to Swift, handling type and optional initialization."""
        print(f"Visiting var declaration: {ctx.getText()}")
        var_name = self.visitIdentifier(ctx.IDENTIFIER())
        var_type = self.visitType(ctx.type_()) if ctx.type_() else None
        var_value = self.visitExpression(ctx.expression()) if ctx.expression() else None
        declaration = f"var {var_name}"
        if var_type:
            declaration += f": {var_type}"
        if var_value:
            declaration += f" = {var_value}"
        return declaration

    def visitValDeclaration(self, ctx):
        """Converts a Kotlin 'val' declaration to Swift, handling type and optional initialization."""
        print(f"Visiting val declaration: {ctx.getText()}")
        val_name = self.visitIdentifier(ctx.IDENTIFIER())
        val_type = self.visitType(ctx.type_()) if ctx.type_() else None
        val_value = self.visitExpression(ctx.expression()) if ctx.expression() else None
        declaration = f"let {val_name}"
        if val_type:
            declaration += f": {val_type}"
        if val_value:
            declaration += f" = {val_value}"
        return declaration

    def visitType(self, ctx): 
        """Maps a Kotlin type to its Swift equivalent, defaulting to the original type if unmapped."""
        kotlin_type = ctx.getText()  
        swift_type = self.kotlin2swiftTypes.get(kotlin_type, kotlin_type)  
        return swift_type

    def visitIfStatement(self, ctx):
        """Converts a Kotlin if-else-if statement to Swift, with else and else-if being optional."""
        print(f"Visiting if statement: {ctx.getText()}")
        condition = self.visitExpression(ctx.expression())
        if ctx.block(0): 
            body = self.visitBlock(ctx.block(0))
        else:  
            body = self.visitStatement(ctx.statement(0))
        if ctx.ELSE():
            if ctx.block(1): 
                else_body = self.visitBlock(ctx.block(1))
            else:
                else_body = self.visitStatement(ctx.statement(1))
            return f"if {condition} {{ {body} }} else {{ {else_body} }}"

        return f"if {condition} {{ {body} }}"

    def visitForStatement(self, ctx):
        """Converts a Kotlin for loop with a range to a Swift-compatible loop."""
        print(f"Visiting for statement: {ctx.getText()}")
        identifier = self.visitIdentifier(ctx.IDENTIFIER())
        start = self.visitExpression(ctx.expression(0))  # start expression
        end = self.visitExpression(ctx.expression(1))    # end expression
        body = self.visitBlock(ctx.block())
        return f"for {identifier} in {start}...{end} {{ {body} }}"

    def visitPrintStatement(self, ctx):
        """Transforms a Kotlin print statement to a Swift print statement."""
        print(f"Visiting print statement: {ctx.getText()}")
        expression = self.visitExpression(ctx.expression())
        return f"print({expression})"

    def visitReadStatement(self, ctx):
        """Converts a Kotlin readLine statement to Swift, supporting optional var/val keyword."""
        print(f"Visiting read statement: {ctx.getText()}")
        identifier = self.visitIdentifier(ctx.IDENTIFIER())
        return f"{identifier} = readLine()"

    def visitClassDeclaration(self, ctx):
        """Transforms a Kotlin class declaration to Swift, handling class name and body."""
        print(f"Visiting declaration: {ctx.getText()}")
        class_name = self.visitIdentifier(ctx.IDENTIFIER())
        body = self.visitClassBody(ctx.classBody())
        has_parentheses = ctx.LEFT_ROUND_BRACKET() is not None and ctx.RIGHT_ROUND_BRACKET() is not None                    
        if ctx.parameterList():
            constructor_params = self.visitParameterList(ctx.parameterList())
            attributes_declarations = "\n".join([
                f"var {param.split(':')[0].strip()}: {param.split(':')[1].strip().split('=')[0]}"
                for param in constructor_params.split(", ")
            ])
            attributes_assignments = "\n".join([
                f"self.{param.split(':')[0].strip()} = {param.split(':')[0].strip()}"
                for param in constructor_params.split(", ")
            ])
            constructor = f"init({constructor_params}) {{\n{attributes_assignments}\n}}"
            class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
            return f"{class_declaration} {{\n{attributes_declarations}\n{constructor}\n{body}\n}}"
        class_declaration = f"class {class_name}()" if has_parentheses else f"class {class_name}"
        return f"{class_declaration} {{\n{body}\n}}"
    
    def visitClassBody(self, ctx):
        """Visits the body of a class and processes each statement."""
        print(f"Visiting class body: {ctx.getText()}")
        statements = []
        if ctx.children:
            for stmt in ctx.children:
                if isinstance(stmt, KotlinParser.VarDeclarationContext):
                    statements.append(self.visitVarDeclaration(stmt))
                elif isinstance(stmt, KotlinParser.FunctionDeclarationContext):
                    statements.append(self.visitFunctionDeclaration(stmt))
                else:
                    statements.append(self.visitStatement(stmt))
        return "\n".join(filter(None, statements))

    def visitFunctionDeclaration(self, ctx):
        """Visits and transforms a Kotlin function declaration into a Swift function declaration."""
        print(f"Visiting function declaration: {ctx.getText()}")
        func_name = self.visitIdentifier(ctx.IDENTIFIER())
        parameters = self.visitParameterList(ctx.parameterList()) if ctx.parameterList() else ""
        body = self.visitBlock(ctx.block())
        if ctx.type_():
            return_type = self.visitType(ctx.type_()) 
            return f"func {func_name}({parameters}) -> {return_type} {{ {body} }}"
        return f"func {func_name}({parameters}) {{ {body} }}"
    
    def visitParameterList(self, ctx):
        """Visits and converts a list of Kotlin parameters into a list of Swift parameters."""
        return ", ".join([self.visitParameter(param) for param in ctx.parameter()])
    
    def visitParameter(self, ctx):
        """Visits a parameter and converts it to Swift."""
        param_name = self.visitIdentifier(ctx.IDENTIFIER())
        param_type = self.visitType(ctx.type_()) 
        if (ctx.literal()):
            param_value = self.visitLiteral(ctx.literal()) 
            return f"{param_name}: {param_type} = {param_value}"
        return f"{param_name}: {param_type}"

    def visitBlock(self, ctx):
        """Visits a block of statements, joining them with newlines."""
        print(f"Visiting block: {ctx.getText()}")        
        for stmt in ctx.statement():
            print(stmt.getText()) 
        statements = [self.visitStatement(stmt) for stmt in ctx.statement()]
        return "\n".join(filter(None, statements))

    def visitExpression(self, ctx):
        """Evaluates expressions, including literals, identifiers, and binary operations."""
        print(f"Visiting expression: {ctx.getText()}")
        if ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.IDENTIFIER():
            return self.visitIdentifier(ctx.IDENTIFIER())
        elif len(ctx.children) == 3:  # Binary operation
            left = self.visitExpression(ctx.expression(0))
            op = ctx.children[1].getText()  # Operator
            right = self.visitExpression(ctx.expression(1))
            return f"{left} {op} {right}"
        else:
            print(f"Unrecognized expression format: {ctx.getText()}")
            return ""

    def visitLiteral(self, ctx):
        """Returns the literal value as text for Swift conversion."""
        print(f"Visiting literal: {ctx.getText()}")
        return ctx.getText()
    
    def visitComment(self, ctx):
        """Trannsforms inline and blockc comments."""
        if ctx.LINE_COMMENT():
            return self.visitLineComment(ctx.LINE_COMMENT())
        elif ctx.BLOCK_COMMENT():
            return self.visitBlockComment(ctx.BLOCK_COMMENT())
        else:
            return ""
    
    def visitLineComment(self, ctx):
        """Transforms inline comments."""
        comment = ctx.getText()[2:].strip() 
        return f"# {comment}"

    def visitBlockComment(self, ctx):
        """Transforms block comments."""
        comment = ctx.getText()[2:-2].strip() 
        return f"/* {comment} */"
