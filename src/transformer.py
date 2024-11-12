from antlr4 import *

class KotlinToSwiftTransformer(ParseTreeVisitor):
    """Transforms Kotlin code into Swift code: this class extends the ParseTreeVisitor class 
    to traverse the parse tree generated by the Kotlin parser, containing methods to handle various types 
    of statements and expressions, converting them into their corresponding Swift representations."""

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
        elif ctx.ifStatement():
            return self.visitIfStatement(ctx.ifStatement())
        elif ctx.forStatement():
            return self.visitForStatement(ctx.forStatement())
        elif ctx.printStatement():
            return self.visitPrintStatement(ctx.printStatement())
        elif ctx.readStatement():
            return self.visitReadStatement(ctx.readStatement())
        elif ctx.classDeclaration():
            return self.visitClassDeclaration(ctx.classDeclaration())
        else: 
            print(f"Unrecognized statement: {ctx.getText()}")
            return ""

    def visitVarDeclaration(self, ctx):
        """Converts a Kotlin 'var' declaration to Swift, handling type and optional initialization."""
        print(f"Visiting var declaration: {ctx.getText()}")
        var_name = ctx.IDENTIFIER().getText()
        var_type = self.visitType(ctx.type_()) if ctx.type_() else "Any"
        var_value = self.visitExpression(ctx.expression()) if ctx.expression() else "nil"
        return f"var {var_name}: {var_type} = {var_value}"

    def visitValDeclaration(self, ctx):
        """Converts a Kotlin 'val' declaration to Swift, handling type and optional initialization."""
        print(f"Visiting val declaration: {ctx.getText()}")
        val_name = ctx.IDENTIFIER().getText()
        val_type = self.visitType(ctx.type_()) if ctx.type_() else "Any"
        val_value = self.visitExpression(ctx.expression()) if ctx.expression() else "nil"
        return f"let {val_name}: {val_type} = {val_value}"

    def visitType(self, ctx): 
        """Maps a Kotlin type to its Swift equivalent, defaulting to the original type if unmapped."""
        kotlin_type = ctx.getText()  
        swift_type = self.kotlin2swiftTypes.get(kotlin_type, kotlin_type)  
        return swift_type

    def visitIfStatement(self, ctx):
        """Converts a Kotlin if-else-if statement to Swift, with else and else-if being optional."""
        # This checks if the 'if' statement has an 'else' block.
        # First, it ensures that the number of children in the 'if' statement is greater than 4, which indicates the presence of an 'else' block.
        # Then, it checks if the second-to-last child is the 'else' keyword by comparing its text value.
        # If both conditions are true, it means an 'else' block exists, and we can process it.
        print(f"Visiting if statement: {ctx.getText()}")
        condition = self.visitExpression(ctx.expression())
        body = self.visitBlock(ctx.block()[0]) 
        if len(ctx.children) > 4 and ctx.children[-2].getText() == 'else':
            else_body = self.visitBlock(ctx.block()[-1])            
            return f"if {condition} {{ {body} }} else {{ {else_body} }}"
        return f"if {condition} {{ {body} }}"

    def visitForStatement(self, ctx):
        """Converts a Kotlin for loop with a range to a Swift-compatible loop."""
        print(f"Visiting for statement: {ctx.getText()}")
        identifier = ctx.IDENTIFIER().getText()
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
        identifier = ctx.IDENTIFIER().getText()
        return f"{identifier} = readLine()"

    def visitClassDeclaration(self, ctx):
        """Transforms a Kotlin class declaration to Swift, handling class name and body."""
        print(f"Visiting declaration: {ctx.getText()}")
        class_name = ctx.IDENTIFIER().getText()
        constructor_params = ctx.parameterList()
        if constructor_params:
            params = [self.visitParameter(param) for param in constructor_params.parameter()]
            constructor_params = ", ".join(params)
            attributes_declarations = "\n".join([f"var {param.split(':')[0].strip()}: {param.split(':')[1].strip()}" for param in params])
            attributes_assignments = "\n".join([f"self.{param.split(':')[0].strip()} = {param.split(':')[0].strip()}" for param in params])
            constructor = f"init({constructor_params}) {{\n{attributes_assignments}\n}}"
        else:
            attributes_declarations = ""
            constructor = "init()"
        body = self.visitClassBody(ctx.classBody())        
        return f"class {class_name} {{\n{attributes_declarations}\n{constructor}\n{body}\n}}"
    
    def visitClassBody(self, ctx):
        """Visits the body of a class, converting variables and fuctions."""
        print(f"Visiting class body: {ctx.getText()}")
        statements = []
        
        for stmt in ctx.getChildren():
            if stmt.getText().startswith("fun"):
                statements.append(self.visitFunctionDeclaration(stmt))
            else:
                statements.append(self.visitStatement(stmt))
        
        return "\n".join(statements)

    def visitFunctionDeclaration(self, ctx):
        """Visits and transforms a Kotlin function declaration into a Swift function declaration."""
        print(f"Visiting function declaration: {ctx.getText()}")
        func_name = ctx.IDENTIFIER().getText()
        parameters = self.visitParameterList(ctx.parameterList()) if ctx.parameterList() else ""
        return_type = self.visitType(ctx.type_()) if ctx.type_() else "Any"
        body = self.visitBlock(ctx.block())
        return f"func {func_name}({parameters}): {return_type} {{ {body} }}"
    
    def visitParameterList(self, ctx):
        """Visits and converts a list of Kotlin parameters into a list of Swift parameters."""
        return ", ".join([self.visitParameter(param) for param in ctx.parameter()])
    
    def visitParameter(self, ctx):
        """Visits a parameter and converts it to Swift."""
        param_name = ctx.IDENTIFIER().getText()
        param_type = self.visitType(ctx.type_()) if ctx.type_() else "Any"
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
            return ctx.IDENTIFIER().getText()
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