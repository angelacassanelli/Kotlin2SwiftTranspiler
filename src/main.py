from parser import parseKotlinCode
from transformer import KotlinToSwiftTransformer

def main():
    """
    Entry point of the program: 
    this function defines a sample Kotlin code snippet, 
    calls the parseKotlinCode function to generate the parse tree, 
    creates an instance of the KotlinToSwiftTransformer class 
    which is used to visit the parse tree,
    then generates the corresponding Swift code and, finally, 
    prints the generated Swift code or an error message.
    """
        
    kotlin_code = """ 
    val input = readline()
    println("Hello, world!") 
    for (i in 1..5) {
        println("for instruction") 
    }      
    if(true) {
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
        print("Oops! No Swift code generated.")
    else:
        print(f"Swift code generated:\n{swift_code}")


if __name__ == "__main__":
    main()
