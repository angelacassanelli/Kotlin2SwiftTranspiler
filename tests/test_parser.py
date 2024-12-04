import unittest
from src.Transpiler import parse_kotlin_code
from src.KotlinToSwiftVisitor import KotlinToSwiftVisitor
from src.SemanticErrorListener import SemanticErrorListener
from src.SymbolTable import SymbolTable

def generate_swift_from_kotlin(kotlin_code):
    """
    Generates Swift code from Kotlin code by:
    - Parsing the Kotlin code to produce a parse tree.
    - Transforming the parse tree into Swift code using KotlinToSwiftTransformer.
    Returns the Swift code or an error message if parsing fails.
    """

    # Step 1: Parse the Kotlin code to generate the parse tree
    tree = parse_kotlin_code(kotlin_code)
    
    # If parsing fails (i.e., the tree is None), return an error message
    if tree is None:
        return "Parsing failed"

    # Step 2: Transform the parse tree into Swift code using the KotlinToSwiftVisitor
    
    symbol_table = SymbolTable()  
    semantic_error_listener = SemanticErrorListener()  
    visitor = KotlinToSwiftVisitor(
        symbol_table=symbol_table, 
        semantic_error_listener = semantic_error_listener
    )
    
    # Generate the Swift code by visiting the parse tree
    swift_code = visitor.visit_program(tree)

    # Step 3: Return the Swift code; 
    # if no Swift code is generated, return a message indicating this.
    if semantic_error_listener.has_errors():
        raise Exception("\n".join(semantic_error_listener.get_errors())) 
    elif swift_code is None or swift_code.strip() == "":
        print("❌ Oops! No Swift code generated.")
        return None
    else:
        print(f"✅ Swift code generated succesfully.")
        return swift_code

class TestKotlinToSwiftTransformer(unittest.TestCase):
    
    ### Basic Statements ###
    
    # Input Statement
    
    def test_input_with_assignment_statement(self):
        kotlin_code = 'class Example() { \nfun test() { line = readLine() }\n}'
        expected_swift = 'class Example() {\nfunc test() { line = readLine() }\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_input_with_declaration_statement(self):
        kotlin_code = 'class Example() {\nfun test() { line = readLine() }\n}'
        expected_swift = 'class Example() {\nfunc test() { line = readLine() }\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Output Statement

    def test_output_statement(self):
        kotlin_code = 'class Example() {\nfun test() { println("Hello, world!") }\n}'
        expected_swift = 'class Example() {\nfunc test() { print("Hello, world!") }\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Variable/Constant Assignment & Declarations + Data Types
    
    def test_string_variable_declarations(self): 
        kotlin_code = 'class Example() {\nvar s : String = "s"\n}'
        expected_swift = 'class Example() {\nvar s : String = "s"\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_int_variable_declarations(self):
        kotlin_code = 'class Example() {\nvar i : Int = 10\n}'
        expected_swift = 'class Example() {\nvar i : Int = 10\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_variable_boolean_variable_declarations(self):
        kotlin_code = 'class Example() {\nvar b : Boolean = true\n}'
        expected_swift = 'class Example() {\nvar b : Bool = true\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_string_constant_declarations(self):
        kotlin_code = 'class Example() {\nval s : String = "s"\n}'
        expected_swift = 'class Example() {\nlet s : String = "s"\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_int_constant_declarations(self):
        kotlin_code = 'class Example() {\nvar i : Int = 10\n}'
        expected_swift = 'class Example() {\nvar i : Int = 10\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_boolean_constant_declarations(self):
        kotlin_code = 'class Example() {\nval b : Boolean = true\n}'
        expected_swift = 'class Example() {\nlet b : Bool = true\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Assignment Statement

    def test_string_variable_assignment(self):
        kotlin_code = 'class Example() {\nvar s : String\ns = "string"\n}'
        expected_swift = 'class Example() {\nvar s : String\ns = "string"\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_int_variable_assignment(self):
        kotlin_code = 'class Example() {\nvar i : Int\ni = 10\n}'
        expected_swift = 'class Example() {\nvar i : Int\ni = 10\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_boolean_constant_assignment(self):
        kotlin_code = 'class Example() {\nvar b : Boolean\nb = true\n}'
        expected_swift = 'class Example() {\nvar b : Bool\nb = true\n}'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # if Statement
    
    def test_if_arithmetic_expression_statement(self):
        kotlin_code = """class Example() {\nfun test() { if (1 > 2) { println("if instruction") } }\n}"""
        expected_swift = """class Example() {\nfunc test() { if 1 > 2 { print("if instruction") } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_if_boolean_expression_statement(self):
        kotlin_code = """class Example() {\nfun test() { if (true) { println("if instruction") } }\n}"""
        expected_swift = """class Example() {\nfunc test() { if true { print("if instruction") } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_if_else_statement(self):
        kotlin_code = """class Example() {\nfun test() { if (1 <= 2) { println("if instruction") } else { println("else instruction") } }\n}"""
        expected_swift = """class Example() {\nfunc test() { if 1 <= 2 { print("if instruction") } else { print("else instruction") } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_if_statement_without_brackets(self):
        kotlin_code = """class Example() {\nfun test() { if (1 < 2) println("if instruction") }\n}"""
        expected_swift = """class Example() {\nfunc test() { if 1 < 2 { print("if instruction") } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # for Statement

    # def test_for_statement(self):
    #     kotlin_code = """class Example() {\nfun test() { for (i in 1 .. 5) { println("for instruction") } }\n}"""
    #     expected_swift = """class Example() {\nfunc test() { for i in 1 ... 5 { print("for instruction") } }\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    # def test_for_statement_without_brackets(self):
    #     kotlin_code = """class Example() {\nfun test() { for (i in 1 .. 5) println("for instruction") }\n}"""
    #     expected_swift = """class Example() {\nfunc test() { for i in 1 ... 5 { print("for instruction") } }\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    ### Object Oriented Programming ###

    # Logical expressions

    # def test_function_logical_expression_1(self):
    #     kotlin_code = """class Example() {\nval isAdult: Boolean = age >= 18 && hasID\n}"""
    #     expected_swift = """class Example() {\nlet isAdult: Bool = age >= 18 && hasID\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_logical_expression_2(self):
    #     kotlin_code = """class Example() {\nval canVote: Boolean = isCitizen || (age >= 18 && hasPermanentResidency)\n}"""
    #     expected_swift = """class Example() {\nlet canVote: Bool = isCitizen || (age >= 18 && hasPermanentResidency)\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_logical_expression_3(self):
    #     kotlin_code = """class Example() {\nval isValid: Boolean = (input != null) && (input > 5) || isFallbackEnabled\n}"""
    #     expected_swift = """class Example() {\nlet isValid: Bool = (input != null) && (input > 5) || isFallbackEnabled\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_logical_expression_4(self):
    #     kotlin_code = """class Example() {\nval shouldRun: Boolean = !isDisabled && (isEnabled || hasPermissions)\n}"""
    #     expected_swift = """class Example() {\nlet shouldRun: Bool = !isDisabled && (isEnabled || hasPermissions)\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Arithmetic expressions

    # def test_function_arithmetic_expression_1(self):
    #     kotlin_code = """class Example() {\nval result: Int = (10 + 20) * 3 - 4 / 2\n}"""
    #     expected_swift = """class Example() {\nlet result: Int = (10 + 20) * 3 - 4 / 2\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_arithmetic_expression_2(self):
    #     kotlin_code = """class Example() {\nval area: Int = (length * width) - (border * 2)\n}"""
    #     expected_swift = """class Example() {\nlet area: Int = (length * width) - (border * 2)\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_arithmetic_expression_3(self):
    #     kotlin_code = """class Example() {\nval price: Int = basePrice + (taxRate * basePrice / 100)\n}"""
    #     expected_swift = """class Example() {\nlet price: Int = basePrice + (taxRate * basePrice / 100)\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_arithmetic_expression_4(self):
    #     kotlin_code = """class Example() {\nval score: Int = (pointsEarned / totalPoints) * 100\n}"""
    #     expected_swift = """class Example() {\nlet score: Int = (pointsEarned / totalPoints) * 100\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Relational expressions

    # def test_function_relational_expression_1(self):
    #     kotlin_code = """class Example() {\nval isGreater: Boolean = x > y && y >= z\n}"""
    #     expected_swift = """class Example() {\nlet isGreater: Bool = x > y && y >= z\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_relational_expression_2(self):
    #     kotlin_code = """class Example() {\nval isEqual: Boolean = (a + b) == c\n}"""
    #     expected_swift = """class Example() {\nlet isEqual: Bool = (a + b) == c\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_relational_expression_3(self):
    #     kotlin_code = """class Example() {\nval isInRange: Boolean = value >= lowerBound && value <= upperBound\n}"""
    #     expected_swift = """class Example() {\nlet isInRange: Bool = value >= lowerBound && value <= upperBound\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_relational_expression_4(self):
    #     kotlin_code = """class Example() {\nval isNotMatching: Boolean = (input1 != input2) || input3 == null\n}"""
    #     expected_swift = """class Example() {\nlet isNotMatching: Bool = (input1 != input2) || input3 == null\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Logic - arithmetic expressions

    # def test_function_logic_arithmetic_expression_1(self):
    #     kotlin_code = """class Example() {\nval isValidScore: Boolean = ((score + bonus) > 50) && !isPenalty\n}"""
    #     expected_swift = """class Example() {\nlet isValidScore: Bool = ((score + bonus) > 50) && !isPenalty\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_logic_arithmetic_expression_2(self):
    #     kotlin_code = """class Example() {\nval canPass: Boolean = (examScore >= 50) && (attendanceRate > 75)\n}"""
    #     expected_swift = """class Example() {\nlet canPass: Bool = (examScore >= 50) && (attendanceRate > 75)\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_logic_arithmetic_expression_3(self):
    #     kotlin_code = """class Example() {\nval isQualified: Boolean = ((experience * skillLevel) >= 100) || hasCertification\n}"""
    #     expected_swift = """class Example() {\nlet isQualified: Bool = ((experience * skillLevel) >= 100) || hasCertification\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_logic_arithmetic_expression_4(self):
    #     kotlin_code = """class Example() {\nval isBalanced: Boolean = (income - expenses) >= 0 && !hasDebts\n}"""
    #     expected_swift = """class Example() {\nlet isBalanced: Bool = (income - expenses) >= 0 && !hasDebts\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)


    # Expressions with parenthesis

    # def test_function_expression_with_peranthesis_1(self):
    #     kotlin_code = """class Example() {\nval result: Int = (((10 + 2) * 5) / 3) - 1\n}"""
    #     expected_swift = """class Example() {\nlet result: Int = (((10 + 2) * 5) / 3) - 1\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_expression_with_peranthesis_2(self):
    #     kotlin_code = """class Example() {\nval isTrue: Int = (((a && b) || c) && !d)\n}"""
    #     expected_swift = """class Example() {\nlet isTrue: Int = (((a && b) || c) && !d)\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_function_expression_with_peranthesis_3(self):
    #     kotlin_code = """class Example() {\nval complex: Int = ((x * y) - (z / w)) > threshold\n}"""
    #     expected_swift = """class Example() {\nlet complex: Int = ((x * y) - (z / w)) > threshold\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Function Declaration

    def test_function_declaration(self):
        kotlin_code = """class Example() {\nfun exampleFunction() { println("Hello!") }\n}"""
        expected_swift = """class Example() {\nfunc exampleFunction() { print("Hello!") }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_function_with_params_declaration(self):
        kotlin_code = """class Example() {\nfun exampleFunction(x: Int, z: Int, b: Boolean) { println("Hello!") }\n}"""
        expected_swift = """class Example() {\nfunc exampleFunction(x: Int, z: Int, b: Bool) { print("Hello!") }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_with_return_declaration(self):
        kotlin_code = """class Example() {\nfun exampleFunction(): Int { return 5 }\n}"""
        expected_swift = """class Example() {\nfunc exampleFunction() -> Int { return 5 }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
  
    # def test_function_with_params_and_return_declaration(self):
    #     kotlin_code = """class Example() {\nfun exampleFunction(x: Int, z: Int, b: Boolean): Boolean { if (x > y) { return b } else { return false } }\n}"""
    #     expected_swift = """class Example() {\nfunc exampleFunction(x: Int, z: Int, b: Bool) -> Bool { if x > y { return b } else { return false } }\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Class Declaration

    def test_class_without_brackets_declaration(self):
        kotlin_code = """class Example {\n\n}"""
        expected_swift = """class Example {\n\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_class_with_empty_body_declaration(self):
        kotlin_code = """class Example() {\n\n}"""
        expected_swift = """class Example() {\n\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # def test_class_with_function_declaration(self):
    #     kotlin_code = """class Example() {\nvar a: Int = 10\nvar b: Int = 100\nfun isAGreaterThanB(): Boolean { if (a > b) { return true } else { return false } }\n}"""
    #     expected_swift = """class Example() {\nvar a: Int = 10\nvar b: Int = 100\nfunc isAGreaterThanB() -> Bool { if a > b { return true } else { return false } }\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    # def test_class_with_params_declaration(self):
    #     kotlin_code = """class Person(val name: String, var age: Int) {\nfun greet() { println("Hello!") }\n}"""
    #     expected_swift = """class Person() {\nlet name: String\nvar age: Int\ninit(name: String, age: Int) {\nself.name = name\nself.age = age\n}\nfunc greet() { print("Hello!") }\n}"""
    #     self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Comment Statement

    def test_inline_comment_statement(self):
        kotlin_code = """// this is a comment"""
        expected_swift = """# this is a comment"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_block_comment_statement(self):
        kotlin_code = """/* this is a block comment */"""
        expected_swift = """/* this is a block comment */"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_block_multiple_lines_comment_statement(self):
        kotlin_code = """/* this is a \nmultiple line block comment */"""
        expected_swift = """/* this is a \nmultiple line block comment */"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)


if __name__ == "__main__":
    unittest.main()
