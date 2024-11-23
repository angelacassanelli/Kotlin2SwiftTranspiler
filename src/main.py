from parser import parseKotlinCode
from transformer import KotlinToSwiftVisitor

def main():
    """
    Entry point of the program: 
    - Defines a sample Kotlin code snippet.
    - Parses the Kotlin code snippet by calling the parseKotlinCode function to generate a parse tree.
    - Instantiates the KotlinToSwiftTransformer class to traverse the parse tree.
    - Generates the corresponding Swift code by visiting the parse tree.
    - Prints the generated Swift code or an error message if parsing or transformation fails.
    """

    kotlin_code_file = "tests/test_case_3"

    try:
        # Open and read the contents of the file
        with open(kotlin_code_file, 'r') as file:
            kotlin_code = file.read()
        
    except FileNotFoundError:
        print(f"Error: The file {kotlin_code_file} was not found.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
    
    tree = parseKotlinCode(kotlin_code)
    
    if tree is None:
        print("Oops! Failed to parse Kotlin code.")
        return
    
    transformer = KotlinToSwiftVisitor()
    
    swift_code = transformer.visitProgram(tree)
    
    if swift_code is None or swift_code.strip() == "":
        print("\nOops! No Swift code generated.")
    else:
        print(f"\nSwift code generated:\n{swift_code}")


if __name__ == "__main__":
    main()
