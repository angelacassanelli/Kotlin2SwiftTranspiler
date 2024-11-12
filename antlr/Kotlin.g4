// Grammar definition
grammar Kotlin;

// Parser Rules 

// Defines the entry point for the program, allowing zero or more statements 
// until the end of the file (EOF).
program
    : statement* EOF 
    ;

// Specifies different types of statements, including variable and constant declarations, 
// conditional statements, loops, print and read statements, and class declarations.
statement
    : varDeclaration
    | valDeclaration
    | ifStatement
    | forStatement
    | printStatement
    | readStatement
    | classDeclaration
    ;

// Parses variable declarations using 'var' with an optional type and initial value.
varDeclaration
    : 'var' IDENTIFIER (':' type)? ('=' expression)? ';'?
    ;

// Parses constant declarations using 'val' with an optional type and initial value.
valDeclaration
    : 'val' IDENTIFIER (':' type)? ('=' expression)? ';'?
    ;

// Parses conditional 'if' statements with an optional 'else' block.
ifStatement
    : 'if' '(' expression ')' block ( 'else' block )? 
    ;

// Parses 'for' loops with a specified range, from start to end expression.
forStatement
    : 'for' '(' IDENTIFIER 'in' expression '..' expression ')' block
    ;

// Parses print statements that print an expression to the output.
printStatement
    : 'println' '(' expression ')' ';'?
    ;

// Parses statements for reading input, optionally assigning it to a variable.
readStatement
    : ('var' | 'val')? IDENTIFIER '=' 'readLine' '(' ')' ';'?
    ;

// Parses a list of parameters separated by commas, for use in functions.
parameterList
    : parameter (',' parameter)*
    ;

// Parses a single parameter with an identifier and type.
parameter
    : IDENTIFIER ':' type
    ;

// Parses function declarations, including an optional parameter list and function body.
functionDeclaration
    : 'fun' IDENTIFIER '(' parameterList? ')' block
    ;

// Parses the body of a class, which may contain variable declarations or functions.
classBody
    : (varDeclaration | functionDeclaration)*
    ;

// Parses class declarations, with optional constructor parameters and a class body.
classDeclaration
    : 'class' IDENTIFIER '(' parameterList? ')' '{' classBody '}'
    ;

// Parses a code block, which can contain multiple statements enclosed in curly braces.
block
    : '{' statement* '}'
    ;

// Parses expressions, including literals, identifiers, binary operations, and nested expressions.
expression
    : literal                                        
    | IDENTIFIER     
    | expression ('+' | '-' | '*' | '/' | '==' | '>' | '>=' | '<' | '<=') expression
    | '(' expression ')'
    ;

// Parses literal values, which can be integers, booleans, or strings.
literal
    : INT_LITERAL
    | BOOLEAN_LITERAL
    | STRING_LITERAL
    ;

// Defines recognized data types, including Int, Boolean, and String.
type
    : 'Int'
    | 'Boolean'
    | 'String'
    ;

// Defines identifiers, which can start with a letter or underscore, followed by alphanumeric characters.
IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// Defines integer literals, which are sequences of digits.
INT_LITERAL
    : [0-9]+
    ;

// Defines boolean literals with the values true or false.
BOOLEAN_LITERAL
    : 'true' | 'false'
    ;

// Defines string literals, which are enclosed in double quotes and allow escaped characters.
STRING_LITERAL
    : '"' (~["\\] | '\\' .)* '"'
    ;

// Ignored Tokens: ignores whitespace, including spaces, tabs, and newline characters, by skipping them in parsing.
WS
    : [ \t\r\n]+ -> skip
    ;
