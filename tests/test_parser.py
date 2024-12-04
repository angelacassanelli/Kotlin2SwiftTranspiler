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

    def test_for_statement(self):
        kotlin_code = """class Example() {\nfun test() { var i = 1\nfor (i in 1 .. 5) { println("for instruction") } }\n}"""
        expected_swift = """class Example() {\nfunc test() { var i = 1\nfor i in 1 ... 5 { print("for instruction") } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_for_statement_without_brackets(self):
        kotlin_code = """class Example() {\nfun test() { var i = 1\nfor (i in 1 .. 5) println("for instruction") }\n}"""
        expected_swift = """class Example() {\nfunc test() { var i = 1\nfor i in 1 ... 5 { print("for instruction") } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    ### Object Oriented Programming ###

    # Logical expressions

    def test_function_logical_expression_1(self):
        kotlin_code = """class Example() {\nval age : Int = 18\nval hasID : Boolean =  true\nval isAdult : Boolean = age >= 18 && hasID\n}"""
        expected_swift = """class Example() {\nlet age : Int = 18\nlet hasID : Bool = true\nlet isAdult : Bool = age >= 18 && hasID\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_logical_expression_2(self):
        kotlin_code = """class Example() {\nval isCitizen = true\nval age = 18\nval hasPermanentResidency = false\nval canVote : Boolean = isCitizen || (age >= 18 && hasPermanentResidency)\n}"""
        expected_swift = """class Example() {\nlet isCitizen = true\nlet age = 18\nlet hasPermanentResidency = false\nlet canVote : Bool = isCitizen || (age >= 18 && hasPermanentResidency)\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_logical_expression_3(self):
        kotlin_code = """class Example() {\nval input = 10\nval isFallbackEnabled = true\nval isValid : Boolean = input > 5 || isFallbackEnabled\n}"""
        expected_swift = """class Example() {\nlet input = 10\nlet isFallbackEnabled = true\nlet isValid : Bool = input > 5 || isFallbackEnabled\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_logical_expression_4(self):
        kotlin_code = """class Example() {\nval isDisabled = false\nval isEnabled = false\nval hasPermissions = true\nval shouldRun : Boolean = !isDisabled && (isEnabled || hasPermissions)\n}"""
        expected_swift = """class Example() {\nlet isDisabled = false\nlet isEnabled = false\nlet hasPermissions = true\nlet shouldRun : Bool = !isDisabled && (isEnabled || hasPermissions)\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Arithmetic expressions

    def test_function_arithmetic_expression_1(self):
        kotlin_code = """class Example() {\nval result : Int = (10 + 20) * 3 - 4 / 2\n}"""
        expected_swift = """class Example() {\nlet result : Int = (10 + 20) * 3 - 4 / 2\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_arithmetic_expression_2(self):
        kotlin_code = """class Example() {\nval length = 10\nval width = 10\nval border = 5\nval area : Int = (length * width) - (border * 2)\n}"""
        expected_swift = """class Example() {\nlet length = 10\nlet width = 10\nlet border = 5\nlet area : Int = (length * width) - (border * 2)\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_arithmetic_expression_3(self):
        kotlin_code = """class Example() {\nval basePrice = 10\nval taxRate = 10\nval price : Int = basePrice + (taxRate * basePrice / 100)\n}"""
        expected_swift = """class Example() {\nlet basePrice = 10\nlet taxRate = 10\nlet price : Int = basePrice + (taxRate * basePrice / 100)\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_arithmetic_expression_4(self):
        kotlin_code = """class Example() {\nvar pointsEarned = 5\nvar totalPoints = 25\nval score : Int = (pointsEarned / totalPoints) * 100\n}"""
        expected_swift = """class Example() {\nvar pointsEarned = 5\nvar totalPoints = 25\nlet score : Int = (pointsEarned / totalPoints) * 100\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Relational expressions

    def test_function_relational_expression_1(self):
        kotlin_code = """class Example() {\nvar x = 1\nvar y = 2\nvar z = 3\nval isGreater : Boolean = x > y && y >= z\n}"""
        expected_swift = """class Example() {\nvar x = 1\nvar y = 2\nvar z = 3\nlet isGreater : Bool = x > y && y >= z\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_relational_expression_2(self):
        kotlin_code = """class Example() {\nvar a = 10\nvar b = 20\nvar c = 30\nval isEqual : Boolean = (a + b) == c\n}"""
        expected_swift = """class Example() {\nvar a = 10\nvar b = 20\nvar c = 30\nlet isEqual : Bool = (a + b) == c\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_relational_expression_3(self):
        kotlin_code = """class Example() {\nvar value = 100\nval lowerBound = 0\nval upperBound = 100\nval isInRange : Boolean = value >= lowerBound && value <= upperBound\n}"""
        expected_swift = """class Example() {\nvar value = 100\nlet lowerBound = 0\nlet upperBound = 100\nlet isInRange : Bool = value >= lowerBound && value <= upperBound\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_relational_expression_4(self):
        kotlin_code = """class Example() {\nvar input1 = 10\nvar input2 = 50\nval isNotMatching : Boolean = input1 != input2\n}"""
        expected_swift = """class Example() {\nvar input1 = 10\nvar input2 = 50\nlet isNotMatching : Bool = input1 != input2\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Logic - arithmetic expressions

    def test_function_logic_arithmetic_expression_1(self):
        kotlin_code = """class Example() {\nvar score = 10\nvar bonus = 5\nval isPenalty = false\n\nval isValidScore : Boolean = ((score + bonus) > 50) && !isPenalty\n}"""
        expected_swift = """class Example() {\nvar score = 10\nvar bonus = 5\nlet isPenalty = false\nlet isValidScore : Bool = ((score + bonus) > 50) && !isPenalty\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_logic_arithmetic_expression_2(self):
        kotlin_code = """class Example() {\nvar examScore = 18\nval attendanceRate = 1\nval canPass : Boolean = (examScore >= 50) && (attendanceRate > 75)\n}"""
        expected_swift = """class Example() {\nvar examScore = 18\nlet attendanceRate = 1\nlet canPass : Bool = (examScore >= 50) && (attendanceRate > 75)\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_logic_arithmetic_expression_3(self):
        kotlin_code = """class Example() {\nvar experience = 5\nvar skillLevel = 3\nvar hasCertification = false\nval isQualified : Boolean = ((experience * skillLevel) >= 100) || hasCertification\n}"""
        expected_swift = """class Example() {\nvar experience = 5\nvar skillLevel = 3\nvar hasCertification = false\nlet isQualified : Bool = ((experience * skillLevel) >= 100) || hasCertification\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_logic_arithmetic_expression_4(self):
        kotlin_code = """class Example() {\nvar income = 1000\nvar expenses = 800\nvar hasDebts = false\nval isBalanced : Boolean = (income - expenses) >= 0 && !hasDebts\n}"""
        expected_swift = """class Example() {\nvar income = 1000\nvar expenses = 800\nvar hasDebts = false\nlet isBalanced : Bool = (income - expenses) >= 0 && !hasDebts\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)


    # Expressions with parenthesis

    def test_function_expression_with_peranthesis_1(self):
        kotlin_code = """class Example() {\nval result : Int = (((10 + 2) * 5) / 3) - 1\n}"""
        expected_swift = """class Example() {\nlet result : Int = (((10 + 2) * 5) / 3) - 1\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_expression_with_peranthesis_2(self):
        kotlin_code = """class Example() {\nvar a = true\nvar b = true\nvar c = true\nvar d = false\nval isTrue : Boolean = (((a && b) || c) && !d)\n}"""
        expected_swift = """class Example() {\nvar a = true\nvar b = true\nvar c = true\nvar d = false\nlet isTrue : Bool = (((a && b) || c) && !d)\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_expression_with_peranthesis_3(self):
        kotlin_code = """class Example() {\nvar x = 10\nvar y = 20\nvar z = 30\nvar w = 40\nvar threshold = 50\nval complex : Boolean = ((x * y) - (z / w)) > threshold\n}"""
        expected_swift = """class Example() {\nvar x = 10\nvar y = 20\nvar z = 30\nvar w = 40\nvar threshold = 50\nlet complex : Bool = ((x * y) - (z / w)) > threshold\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

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
  
    def test_function_with_params_and_return_declaration(self):
        kotlin_code = """class Example() {\nfun exampleFunction(x: Int, y: Int, b: Boolean): Boolean { if (x > y) { return b } else { return false } }\n}"""
        expected_swift = """class Example() {\nfunc exampleFunction(x: Int, y: Int, b: Bool) -> Bool { if x > y { return b } else { return false } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Class Declaration

    def test_class_without_brackets_declaration(self):
        kotlin_code = """class Example {\n\n}"""
        expected_swift = """class Example {\n\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_class_with_empty_body_declaration(self):
        kotlin_code = """class Example() {\n\n}"""
        expected_swift = """class Example() {\n\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_class_with_function_declaration(self):
        kotlin_code = """class Example() {\nvar a : Int = 10\nvar b : Int = 100\nfun isAGreaterThanB(): Boolean { if (a > b) { return true } else { return false } }\n}"""
        expected_swift = """class Example() {\nvar a : Int = 10\nvar b : Int = 100\nfunc isAGreaterThanB() -> Bool { if a > b { return true } else { return false } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_class_with_params_declaration(self):
        kotlin_code = """class Person(val name: String, var age: Int) {\nfun greet() { println("Hello!") }\n}"""
        expected_swift = """class Person() {\nlet name: String\nvar age: Int\ninit(name: String, age: Int) {\nself.name = name\nself.age = age\n}\nfunc greet() { print("Hello!") }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

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
