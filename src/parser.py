from antlr4 import *
from generated.antlr.KotlinLexer import KotlinLexer
from generated.antlr.KotlinParser import KotlinParser
from SyntaxErrorListener import SyntaxErrorListener
from LexicalErrorListener import LexicalErrorListener

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
            print(f"✅ Tree generated successfully:\n{tree.toStringTree(recog=parser)}")        
            return tree  # Return the parse tree if parsing is successful
    
    except Exception as ex:
        # If an error occurs during parsing, print the error message
        print(f"❌ Oops! Error while parsing code.\n{ex}")
        return None  # Return None in case of an error
