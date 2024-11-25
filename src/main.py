from parser import parseKotlinCode
from KotlinToSwiftVisitor import KotlinToSwiftVisitor

def main():
    """
    Entry point of the program:
    - Defines a sample Kotlin code snippet.
    - Parses the Kotlin code snippet by calling the parseKotlinCode function to generate a parse tree.
    - Instantiates the KotlinToSwiftTransformer class to traverse the parse tree.
    - Generates the corresponding Swift code by visiting the parse tree.
    - Prints the generated Swift code or an error message if parsing or transformation fails.
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
        tree = parseKotlinCode(kotlin_code)
        
        # Check if the parsing was successful (i.e., the tree is not None)
        if tree is None:
            print("❌ Oops! Failed to parse Kotlin code.")
            return
        else:
            # Instantiate the KotlinToSwiftVisitor class, which will visit the parse tree and transform it to Swift
            visitor = KotlinToSwiftVisitor()
            
            # Visit the root of the parse tree to generate Swift code
            swift_code = visitor.visitProgram(tree)
            
            # Check if the generated Swift code is empty or None, and handle that case
            if swift_code is None or swift_code.strip() == "":
                print("No Swift code generated.")
            else:
                # Print the generated Swift code
                print(f"Swift code generated:\n{swift_code}")

    except Exception as e:
        print(f"❌ Oops! Error transpiling code: {e}")
        return


# Ensure the script runs only when executed directly (not imported as a module)
if __name__ == "__main__":
    main()
