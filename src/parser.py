from antlr4 import *
from generated.antlr.KotlinLexer import KotlinLexer
from generated.antlr.KotlinParser import KotlinParser

def parseKotlinCode(kotlin_code):
    """
    Parses the provided Kotlin code and returns the parse tree:
    this function takes in input a string containing Kotlin code, 
    processes it using the Kotlin lexer and parser, 
    attempts to create the parse tree and, finally,
    if successful it returns the tree, else it returns None.
    """
    input_stream = InputStream(kotlin_code)
    lexer = KotlinLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = KotlinParser(token_stream)
  
    try:
        tree = parser.program()  
        print(f"Tree generated successfully:\n{tree.toStringTree(recog=parser)}")        
        return tree
    except Exception as ex:
        print(f"Oops! An error occured while parsing code.\n{ex}")
        return None
