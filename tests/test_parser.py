import unittest
from src.parser import parseKotlinCode
from src.transformer import KotlinToSwiftTransformer

def generate_swift_from_kotlin(kotlin_code):
    """
    Generates Swift code from Kotlin code by:
    - Parsing the Kotlin code to produce a parse tree.
    - Transforming the parse tree into Swift code using KotlinToSwiftTransformer.
    Returns the Swift code or an error message if parsing fails.
    """
    tree = parseKotlinCode(kotlin_code)
    if tree is None:
        return "Parsing failed"

    transformer = KotlinToSwiftTransformer()
    swift_code = transformer.visitProgram(tree)
    return swift_code.strip() if swift_code else "No Swift code generated"


class TestKotlinToSwiftTransformer(unittest.TestCase):
    
    ### Basic Statements ###
    
    # Input Statement
    
    def test_input_with_assignment_statement(self):
        kotlin_code = 'line = readLine()'
        expected_swift = 'line = readLine()'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_input_with_declaration_statement(self):
        kotlin_code = 'line = readLine()'
        expected_swift = 'line = readLine()'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Output Statement

    def test_output_statement(self):
        kotlin_code = 'println("Hello, world!")'
        expected_swift = 'print("Hello, world!")'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Variable/Constant Assignment & Declarations + Data Types
    
    def test_string_variable_declarations(self): 
        kotlin_code = 'var s: String = "s"'
        expected_swift = 'var s: String = "s"'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_int_variable_declarations(self):
        kotlin_code = 'var i: Int = 10'
        expected_swift = 'var i: Int = 10'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_variable_boolean_variable_declarations(self):
        kotlin_code = 'var b: Boolean = true'
        expected_swift = 'var b: Bool = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_string_constant_declarations(self):
        kotlin_code = 'val s: String = "s"'
        expected_swift = 'let s: String = "s"'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_int_constant_declarations(self):
        kotlin_code = 'var i: Int = 10'
        expected_swift = 'var i: Int = 10'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_boolean_constant_declarations(self):
        kotlin_code = 'val b: Boolean = true'
        expected_swift = 'let b: Bool = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # Assignment Statement

    def test_string_variable_assignment(self):
        kotlin_code = 's = "string"'
        expected_swift = 's = "string"'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_int_variable_assignment(self):
        kotlin_code = 'i = 10'
        expected_swift = 'i = 10'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_boolean_constant_assignment(self):
        kotlin_code = 'b = true'
        expected_swift = 'b = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # if Statement
    
    def test_if_arithmetic_expression_statement(self):
        kotlin_code = """if (1 > 2) { println("if instruction") }"""
        expected_swift = """if 1 > 2 { print("if instruction") }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_if_boolean_expression_statement(self):
        kotlin_code = """if (true) { println("if instruction") }"""
        expected_swift = """if true { print("if instruction") }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_if_else_statement(self):
        kotlin_code = """if (1 <= 2) { println("if instruction") } else { println("else instruction") }"""
        expected_swift = """if 1 <= 2 { print("if instruction") } else { print("else instruction") }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    # for Statement

    def test_for_statement(self):
        kotlin_code = """for (i in 1..5) { println("for instruction") }"""
        expected_swift = """for i in 1...5 { print("for instruction") }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    ### Object Oriented Programming ###

    # Function Declaration

    def test_function_declaration(self):
        kotlin_code = """fun exampleFunction() { println("Hello!") }"""
        expected_swift = """func exampleFunction() { print("Hello!") }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

        
    def test_function_with_params_declaration(self):
        kotlin_code = """fun exampleFunction(x: Int, z: Int, b: Boolean) { println("Hello!") }"""
        expected_swift = """func exampleFunction(x: Int, z: Int, b: Bool) { print("Hello!") }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_function_with_return_declaration(self):
        kotlin_code = """fun exampleFunction(): Int { return 5 }"""
        expected_swift = """func exampleFunction() -> Int { return 5 }"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
  
    def test_function_with_params_and_return_declaration(self):
        kotlin_code = """fun exampleFunction(x: Int, z: Int, b: Boolean): Boolean { if (x > y) { return b } else { return false } }"""
        expected_swift = """func exampleFunction(x: Int, z: Int, b: Bool) -> Bool { if x > y { return b } else { return false } }"""
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
        kotlin_code = """class Example() {\nvar a: Int = 10\nvar b: Int = 100\nfun isAGreaterThanB(): Boolean { if (a > b) { return true } else { return false } }\n}"""
        expected_swift = """class Example() {\nvar a: Int = 10\nvar b: Int = 100\nfunc isAGreaterThanB() -> Bool { if a > b { return true } else { return false } }\n}"""
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_class_with_params_declaration(self):
        kotlin_code = """class Person(val name: String, var age: Int) { fun greet() { println("Hello!") } }"""
        expected_swift = """class Person() {\nvar name: String\nvar age: Int\ninit(name: String, age: Int) {\nself.name = name\nself.age = age\n}\nfunc greet() { print("Hello!") }\n}"""
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
