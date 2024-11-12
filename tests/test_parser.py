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
    def test_variable_string_declarations(self):
        kotlin_code = 'var s: String = true'
        expected_swift = 'var s: String = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_variable_int_declarations(self):
        kotlin_code = 'var i: Int = true'
        expected_swift = 'var i: Int = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_variable_boolean_declarations(self):
        kotlin_code = 'var b: Boolean = true'
        expected_swift = 'var b: Bool = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_constant_string_declarations(self):
        kotlin_code = 'val s: String = true'
        expected_swift = 'let s: String = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
        
    def test_constant_int_declarations(self):
        kotlin_code = 'var i: Int = true'
        expected_swift = 'var i: Int = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_constant_boolean_declarations(self):
        kotlin_code = 'val b: Boolean = true'
        expected_swift = 'let b: Bool = true'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_input_statement(self):
        kotlin_code = 'line = readLine()'
        expected_swift = 'line = readLine()'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_output_statement(self):
        kotlin_code = 'println("Hello, world!")'
        expected_swift = 'print("Hello, world!")'
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_if_statement(self):
        kotlin_code = """
        if (1 > 2) { println("if instruction") }
        """
        expected_swift = """
        if 1 > 2 { print("if instruction") }
        """.strip()
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)
    
    def test_if_statement(self):
        kotlin_code = """
        if (true) { println("if instruction") }
        """
        expected_swift = """
        if true { print("if instruction") }
        """.strip()
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_if_else_statement(self):
        kotlin_code = """
        if (1 <= 2) { println("if instruction") } else { println("else instruction") }
        """
        expected_swift = """
        if 1 <= 2 { print("if instruction") } else { print("else instruction") }
        """.strip()
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_for_statement(self):
        kotlin_code = """
        for (i in 1..5) { println("for instruction") }
        """
        expected_swift = """
        for i in 1...5 { print("for instruction") }
        """.strip()
        self.assertEqual(generate_swift_from_kotlin(kotlin_code), expected_swift)

    def test_class_declaration(self):
        kotlin_code = """
        class Example {
            var a: Int = 10
            var b: Int = 100

            fun isAGreaterThanB(): Boolean {
                if (a > b) {
                    return true
                } else {
                    return false
                }
            }
        }
        """
        expected_swift = """
        class Example {
            var a: Int = 0
            var b: Int = 0

            func isAGreaterThanB() -> Bool {
                if a > b {
                    return true
                } else {
                    return false
                }
            }
        }
        """
        
    def test_class_with_params_declaration(self):
        kotlin_code = """
        class Person(val name: String, var age: Int) {
            fun greet() {
                println("Hello!")
            }
        }"""
        expected_swift = """
        class Person {
            var name: String
            var age: Int

            init(name: String, age: Int) {
                self.name = name
                self.age = age
            }
            
            func greet() {
                print("Hello!")
            }
        }
        """


if __name__ == "__main__":
    unittest.main()
