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
    var str: String = "stringa"
    var num: Int = 1
    
    val str: String = "stringa"
    val num: Int = 1
    
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
