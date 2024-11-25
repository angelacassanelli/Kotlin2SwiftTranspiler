from antlr4 import *
from generated.antlr.KotlinLexer import KotlinLexer
from generated.antlr.KotlinParser import KotlinParser
from SyntaxErrorListener import SyntaxErrorListener

def parseKotlinCode(kotlin_code):
    """
    Parses the provided Kotlin code and returns the parse tree:
    This function takes in input a string containing Kotlin code, 
    processes it using the Kotlin lexer and parser, 
    attempts to create the parse tree, and finally,
    if successful, it returns the tree; else, it returns None.
    """

    # Convert the Kotlin code string into an input stream that the lexer can process
    input_stream = InputStream(kotlin_code)

    # Instantiate the lexer to tokenize the Kotlin code
    lexer = KotlinLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)

    # Instantiate the parser using the token stream
    parser = KotlinParser(token_stream)

    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners() 
    parser.addErrorListener(error_listener)

    try:
        # Attempt to parse the program using the 'program' rule of the Kotlin parser
        tree = parser.program()
        
        if error_listener.has_errors():
            raise Exception("\n".join(error_listener.get_errors()))
        else:
            print(f"✅ Tree generated successfully:\n{tree.toStringTree(recog=parser)}")        
            return tree  # Return the parse tree if successful
    
    except Exception as ex:
        # If an error occurs during parsing, print the error message
        print(f"❌ Oops! Error while parsing code.\n{ex}")
        return None  # Return None in case of an error
