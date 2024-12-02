import os
from antlr4 import *
from generated.antlr.KotlinLexer import KotlinLexer
from generated.antlr.KotlinParser import KotlinParser
from SyntaxErrorListener import SyntaxErrorListener
from LexicalErrorListener import LexicalErrorListener
from KotlinToSwiftVisitor import KotlinToSwiftVisitor
from SemanticErrorListener import SemanticErrorListener
from SymbolTable import SymbolTable


def transpiler():
    """
    Entry point of the program to transpile Kotlin code to Swift.

    This function performs the following steps:
    1. Reads a sample Kotlin code file.
    2. Parses the Kotlin code using the `parseKotlinCode` function to generate the abstract syntax tree (AST).
    3. Initializes the `KotlinToSwiftVisitor` to traverse the parse tree and transform it into Swift code.
    4. Generates the corresponding Swift code.
    5. Prints the generated Swift code, or an error message if parsing or transformation fails.

    Workflow:
        - Read Kotlin code from a file.
        - Parse the code into a parse tree.
        - Transform the parse tree to Swift code using the visitor pattern.
        - Handle errors during reading, parsing, and transformation.

    Raises:
        Exception: If an error occurs at any point in reading, parsing, or transpiling the code.
    """
    
    # Define the path to the Kotlin code file for the test case
    kotlin_code_path = "tests/test_case_0"

    try:
        kotlin_code = read_kotlin_code(kotlin_code_path)
        swift_code = transpile_kotlin_to_swift(kotlin_code)

        # Check if the generated Swift code is empty or None, and handle that case
        if swift_code is None or swift_code.strip() == "":
            print("❌ Oops! No Swift code generated.")
            return
        else:
            # Print the generated Swift code
            write_swift_code(swift_code)                

    except Exception as ex:
        # Handle any exceptions that occur during the parsing or transpiling process
        print(f"❌ Oops! Transpiling failed: no swift code generated: {ex}")
        return


def transpile_kotlin_to_swift(kotlin_code):
    print("🚀 Transpiling Kotlin code...")

    # Parse the Kotlin code using the parseKotlinCode function to generate the abstract syntax tree (AST)
    tree = parse_kotlin_code(kotlin_code)
        
    # Check if the parsing was successful (i.e., the tree is not None)
    if tree is None:
        print(f"❌ Oops! Parsing failed: no parse tree generated.")
        return
        
    # Create a new symbol table
    symbol_table = SymbolTable()  
    # Create a listener for semantic errors
    semantic_error_listener = SemanticErrorListener()  
    # Instantiate the KotlinToSwiftVisitor class, which will visit the parse tree and transform it to Swift
    visitor = KotlinToSwiftVisitor(
        symbol_table=symbol_table, 
        semantic_error_listener = semantic_error_listener
    )
            
    # Visit the root of the parse tree to generate Swift code
    swift_code = visitor.visit_program(tree)
            
    # Check for semantic errors            
    if semantic_error_listener.has_errors():
        errors = "\n".join(semantic_error_listener.get_errors())
        raise Exception(f"❌ Oops! Semantic errors found:\n{errors}") # Raise if semantic errors are found            
        
    return swift_code


def parse_kotlin_code(kotlin_code):
    """
    Parses the provided Kotlin code and returns the parse tree.

    This function takes a string containing Kotlin code, processes it through
    the lexical analysis and parsing stages, and generates a parse tree. If any 
    lexical or syntax errors are encountered, an exception is raised with details 
    of the errors. If parsing is successful, the parse tree is returned.

    Args:
        kotlin_code (str): The Kotlin source code to be parsed.

    Returns:
        tree (ParseTree or None): The parse tree if parsing is successful, 
                                   otherwise None in case of an error.

    Raises:
        Exception: If there are any lexical or syntax errors encountered 
                   during the parsing process, an exception with the error details is raised.
    """
    
    print("🚀 Parsing Kotlin code...")

    # Convert the Kotlin code string into an input stream that the lexer can process
    input_stream = InputStream(kotlin_code)

    # Instantiate the lexer to tokenize the Kotlin code
    lexer = KotlinLexer(input_stream)

    # Add the lexical error listener
    lexical_error_listener = LexicalErrorListener()
    lexer.removeErrorListeners()  # Remove default error listeners
    lexer.addErrorListener(lexical_error_listener)  # Add custom lexical error listener

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)

    # Instantiate the parser using the token stream
    parser = KotlinParser(token_stream)

    # Add the syntax error listener
    syntax_error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()  # Remove default error listeners
    parser.addErrorListener(syntax_error_listener)  # Add custom syntax error listener

    try:
        # Attempt to parse the program using the 'program' rule of the Kotlin parser
        tree = parser.program()

        # Check for lexical and syntax errors
        if lexical_error_listener.has_errors():
            raise Exception("\n".join(lexical_error_listener.get_errors()))  # Raise if lexical errors are found
        if syntax_error_listener.has_errors():
            raise Exception("\n".join(syntax_error_listener.get_errors()))  # Raise if syntax errors are found
        else:
            print(f"✅ Tree generated successfully:\n    {tree.toStringTree(recog=parser)}")        
            return tree  # Return the parse tree if parsing is successful
    
    except Exception as ex:
        # If an error occurs during parsing, print the error message
        print(f"❌ Oops! Parsing failed: {ex}")
        return None  # Return None in case of an error


def write_swift_code(swift_code):
    print("🚀 Writing Swift code...")

    swift_output_dir = "output"
    swift_output_file = os.path.join(swift_output_dir, "output.swift")
    os.makedirs(swift_output_dir, exist_ok=True)

    try:
        with open(swift_output_file, 'w') as file:
            file.write(swift_code)
        print(f"✅ Swift code generated and saved to {swift_output_file}:\n\n{swift_code}")
        return
    except Exception as ex:
        print(f"❌ Oops! Error writing Swift code to file {swift_output_file}: {ex}")
        return

def read_kotlin_code(file_path):
    print("🚀 Reading Kotlin code...")

    try:
        # Attempt to open and read the contents of the Kotlin code file
        with open(file_path, 'r') as file:
            return file.read()  # Read the file content into a string
        
    except FileNotFoundError:
        # Handle case where the file does not exist
        print(f"❌ Oops! File {file_path} not found.")
        return
    except Exception as ex:
        # Handle any other unexpected errors during file reading
        print(f"❌ Oops! Error reading Kotlin code from file {file_path}: {ex}")
        return
    

# Ensure the script runs only when executed directly (not imported as a module)
if __name__ == "__main__":
    transpiler()
