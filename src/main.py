from parser import parseKotlinCode
from transformer import KotlinToSwiftTransformer

def main():
    """
    Entry point of the program: 
    - Defines a sample Kotlin code snippet.
    - Parses the Kotlin code snippet by calling the parseKotlinCode function to generate a parse tree.
    - Instantiates the KotlinToSwiftTransformer class to traverse the parse tree.
    - Generates the corresponding Swift code by visiting the parse tree.
    - Prints the generated Swift code or an error message if parsing or transformation fails.
    """
        
    kotlin_code = """ 
    var str: String = "stringa"
    var num: Int = 1
    
    val str: String = "stringa"
    val num: Int = 1

    val b: Boolean = true
    val b: Boolean = true
    
    val line = readLine()
    println("Hello, world!") 

    for (i in 1..5) {
        println("for instruction") 
    }      
    
    if(1==1) {
        println("if instruction") 
    } 
    """
    
    tree = parseKotlinCode(kotlin_code)
    
    if tree is None:
        print("Oops! Failed to parse Kotlin code.")
        return
    
    transformer = KotlinToSwiftTransformer()
    
    swift_code = transformer.visitProgram(tree)
    
    if swift_code is None or swift_code.strip() == "":
        print("\nOops! No Swift code generated.")
    else:
        print(f"\nSwift code generated:\n{swift_code}")


if __name__ == "__main__":
    main()
