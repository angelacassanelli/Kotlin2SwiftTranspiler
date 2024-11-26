from parser import parse_kotlin_code
from KotlinToSwiftVisitor import KotlinToSwiftVisitor

def main():
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
    kotlin_code = "tests/test_case_0"

    try:
        # Attempt to open and read the contents of the Kotlin code file
        with open(kotlin_code, 'r') as file:
            kotlin_code = file.read()  # Read the file content into a string
        
    except FileNotFoundError:
        # Handle case where the file does not exist
        print(f"❌ Oops! File {kotlin_code} not found.")
        return
    except Exception as e:
        # Handle any other unexpected errors during file reading
        print(f"❌ Oops! Error reading the file {kotlin_code}: {e}")
        return

    try:
        # Parse the Kotlin code using the parseKotlinCode function to generate the abstract syntax tree (AST)
        tree = parse_kotlin_code(kotlin_code)
        
        # Check if the parsing was successful (i.e., the tree is not None)
        if tree is None:
            print("❌ Oops! Failed to parse Kotlin code.")
            return
        else:
            # Instantiate the KotlinToSwiftVisitor class, which will visit the parse tree and transform it to Swift
            visitor = KotlinToSwiftVisitor()
            
            # Visit the root of the parse tree to generate Swift code
            swift_code = visitor.visit_program(tree)
            
            # Check if the generated Swift code is empty or None, and handle that case
            if swift_code is None or swift_code.strip() == "":
                print("❌ Oops! No Swift code generated.")
            else:
                # Print the generated Swift code
                print(f"✅ Swift code generated:\n{swift_code}")

    except Exception as e:
        # Handle any exceptions that occur during the parsing or transpiling process
        print(f"❌ Oops! Error transpiling code: {e}")
        return


# Ensure the script runs only when executed directly (not imported as a module)
if __name__ == "__main__":
    main()
