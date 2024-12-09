import os
import argparse
from antlr4 import *
from generated.antlr.KotlinLexer import KotlinLexer
from generated.antlr.KotlinParser import KotlinParser
from SyntaxErrorListener import SyntaxErrorListener
from LexicalErrorListener import LexicalErrorListener
from KotlinToSwiftVisitor import KotlinToSwiftVisitor
from SemanticErrorListener import SemanticErrorListener
from SymbolTable import SymbolTable


def transpile_kotlin_code(kotlin_code_path):

    """
    Transpiles Kotlin code to Swift.

    This function reads Kotlin code from the given file path, parses it, transpiles it into Swift code, 
    and then writes the resulting Swift code to an output file.

    Args:
        kotlin_code_path (str): Path to the Kotlin file to transpile.

    Raises:
        Exception: If an error occurs during parsing, transpiling, or writing the Swift code.

    Returns:
        None
    """

    try:
        kotlin_code = read_kotlin_code(kotlin_code_path)
        
        # Check if the generated Swift code is empty or None, and handle that case
        if kotlin_code is None or kotlin_code.strip() == "":
            print("❌ Oops! No Kotlin code to transpile.")
            return
        
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
        print(f"❌ Oops! Transpiling failed: no swift code generated.\n{ex}")
        return


def transpile_kotlin_to_swift(kotlin_code):

    """
    Transpiles the Kotlin code to Swift.

    This function parses the Kotlin code and then uses a visitor pattern to transform the abstract syntax tree (AST) into Swift code.

    Args:
        kotlin_code (str): The Kotlin code to transpile.

    Raises:
        Exception: If parsing or semantic errors are encountered.

    Returns:
        str: The generated Swift code.
    """

    print("🚀 Transpiling Kotlin code...")

    # Parse the Kotlin code using the parseKotlinCode function to generate the abstract syntax tree (AST)
    tree = parse_kotlin_code(kotlin_code)
        
    # Check if the parsing was successful (i.e., the tree is not None)
    if tree is None:
        Exception(f"❌ Oops! Parsing failed: no parse tree generated.")
        
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
        raise Exception("\n".join(semantic_error_listener.get_errors())) # Raise if semantic errors are found        
    
    return swift_code


def parse_kotlin_code(kotlin_code):

    """
    Parses the provided Kotlin code and generates a parse tree.

    This function uses ANTLR to tokenize the Kotlin code, parse it using a custom syntax error listener, and then returns the parse tree.

    Args:
        kotlin_code (str): The Kotlin code to parse.

    Raises:
        Exception: If lexical, syntax, or parsing errors are encountered.

    Returns:
        ParseTree: The parse tree generated from the Kotlin code.
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
        print(f"❌ Oops! Parsing failed.\n{ex}")
        return None  # Return None in case of an error


def write_swift_code(swift_code):

    """
    Writes the generated Swift code to a file.

    This function writes the Swift code into an output file named `output.swift` in the `output` directory.

    Args:
        swift_code (str): The Swift code to write to the file.

    Raises:
        Exception: If an error occurs while writing the file.

    Returns:
        None
    """

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
        print(f"❌ Oops! Error writing Swift code to file {swift_output_file}.\n{ex}")
        return


def read_kotlin_code(file_path):

    """
    Reads Kotlin code from a file.

    This function attempts to open the provided Kotlin file and return its contents as a string.

    Args:
        file_path (str): The path to the Kotlin file to read.

    Raises:
        Exception: If the file is not found or an error occurs during reading.

    Returns:
        str: The contents of the Kotlin file as a string.
    """

    print("🚀 Reading Kotlin code...")

    try:
        # Attempt to open and read the contents of the Kotlin code file
        with open(file_path, 'r') as file:
            return file.read()  # Read the file content into a string
        
    except FileNotFoundError:
        # Handle case where the file does not exist
        raise Exception(f"❌ Oops! File {file_path} not found.")
    except Exception as ex:
        # Handle any other unexpected errors during file reading
        print(f"❌ Oops! Error reading Kotlin code from file {file_path}.\n{ex}")
        return None
    

# Ensure the script runs only when executed directly (not imported as a module)
if __name__ == "__main__":

    """
    Main entry point for the script.

    This block of code runs when the script is executed directly. It sets up argument parsing and calls the transpiler with the provided input file.

    Args:
        None

    Returns:
        None
    """
    
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Transpile Kotlin code to Swift.")
    parser.add_argument(
        "kotlin_file", 
        type=str, 
        help="Path to the Kotlin file to transpile."
    )
    args = parser.parse_args()

    # Call the transpiler with the provided input file
    transpile_kotlin_code(args.kotlin_file)
