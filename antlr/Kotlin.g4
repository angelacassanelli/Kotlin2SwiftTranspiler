// Grammar definition for a restricted version of Kotlin
grammar Kotlin;

// ------------------- Parser Rules -------------------

// Entry point: a program consists of zero or more top-level statements followed by EOF
program
    : topLevelStatement* EOF 
    ;

// Top-level statements: statements that can appear directly in a program
topLevelStatement
    : classDeclaration      // Declaration of a class
    | commentStatement      // Inline or block comment
    ;

// Statements: various executable constructs within functions or blocks
statement
    : readStatement         // Reads input from the user
    | printStatement        // Prints output to the console
    | ifStatement           // Conditional "if" statement
    | forStatement          // "For" loop with a range
    | assignmentStatement   // Variable assignment
    | varDeclaration        // Declaration of a variable
    | returnStatement       // Return statement for functions
    | commentStatement      // Inline or block comment
    ;

// Block of code: a series of statements enclosed in curly braces
block
    : LEFT_CURLY_BRACKET (statement)* RIGHT_CURLY_BRACKET
    ;

// Input statement: reads a line of input and optionally assigns it to a variable 
readStatement
    : (VAR | VAL)? IDENTIFIER EQ READLINE LEFT_ROUND_BRACKET RIGHT_ROUND_BRACKET
    ;

// Output statement: prints an expression to the console
printStatement
    : PRINTLN LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET
    ;

// Conditional "if" statement, with an optional "else" block
ifStatement
    : IF LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET (block | statement) 
      ( ELSE (block | statement) )?
    ;

// "For" loop: iterates over a range
forStatement
    : FOR LEFT_ROUND_BRACKET membershipExpression RIGHT_ROUND_BRACKET (block | statement)
    ;

// Assignment statement: assigns a value to a variable
// By including callExpression inside assignmentStatement, we resolve the conflict 
// where IDENTIFIER could be interpreted as either an assignment (IDENTIFIER = expression) 
// or a function call (IDENTIFIER(...)). 
assignmentStatement
    : IDENTIFIER EQ expression
    | callExpression    // Workaround for ambiguity between assignmentStatement and callExpression:
    ;

// Variable declaration: declares a mutable or immutable variable with an optional type and initial value
varDeclaration        
    : (VAR | VAL) IDENTIFIER COLON type
    | (VAR | VAL) IDENTIFIER EQ expression
    | (VAR | VAL) IDENTIFIER COLON type EQ expression
    ;

// Function declaration: defines a function with parameters, an optional return type, and a body
functionDeclaration
    : FUN IDENTIFIER LEFT_ROUND_BRACKET parameterList? RIGHT_ROUND_BRACKET 
      (COLON type)? block
    ;

// Return statement: exits a function, optionally returning an expression
returnStatement
    : RETURN expression?
    ;

// Class declaration: defines a class with an optional constructor and a body
classDeclaration
    : CLASS IDENTIFIER 
      (LEFT_ROUND_BRACKET (propertyList | parameterList)? RIGHT_ROUND_BRACKET)? 
      LEFT_CURLY_BRACKET classBody? RIGHT_CURLY_BRACKET
    ;

// Class body: contains declarations of variables, functions, or comments
classBody
    : (varDeclaration | assignmentStatement | functionDeclaration | commentStatement)*
    ;

// Parameter list: used in function or class constructors
propertyList
    : property (COMMA property)*
    ;

// Parameter: a single parameter with an identifier, type, and optional initial value
property
    : varDeclaration
    ;

// Parameter list: used in function or class constructors
parameterList
    : parameter (COMMA parameter)*
    ;

// Parameter: a single parameter with an identifier, type, and optional initial value
parameter
    : IDENTIFIER COLON type (EQ expression)?
    ;

// Argument list: passed to functions or constructors
argumentList
    : argument (COMMA argument)*
    ;

// Argument: a single value or named value passed to a function
argument
    : (IDENTIFIER EQ)? expression
    ;

// Expressions: describe computations or values
expression
    : logicalOrExpression
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression 
      (EQEQ relationalExpression | NEQ relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((GT | GTE | LT | LTE) additiveExpression)?
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((MULT | DIV | MOD) unaryExpression)*
    ;

unaryExpression
    : NOT primaryExpression
    | MINUS primaryExpression
    | membershipExpression
    ;

membershipExpression
    : primaryExpression 
      (IN rangeExpression | NOT IN rangeExpression)?
    ;

primaryExpression
    : IDENTIFIER
    | LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET    
    | callExpression
    | literal
    ;

rangeExpression
    : additiveExpression RANGE additiveExpression
    ;

callExpression
    : IDENTIFIER LEFT_ROUND_BRACKET argumentList? RIGHT_ROUND_BRACKET
    ;

// Literal values: integers, strings, or booleans
literal
    : INT_LITERAL
    | STRING_LITERAL
    | booleanLiteral
    ;

// Boolean literals: true or false
booleanLiteral
    : BOOLEAN_TRUE 
    | BOOLEAN_FALSE
    ;

// Comment statements: inline or block comments
commentStatement
    : LINE_COMMENT 
    | BLOCK_COMMENT
    ;

// Type definitions: specify variable or parameter types
type
    : TYPE_INT
    | TYPE_STRING
    | TYPE_BOOLEAN
    ;

// ------------------- Lexer Rules -------------------

// Variable keywords
VAR: 'var';
VAL: 'val';

// Type keywords
TYPE_BOOLEAN: 'Boolean';
TYPE_CHAR: 'Char';
TYPE_STRING: 'String';
TYPE_SHORT: 'Short';
TYPE_INT: 'Int';
TYPE_LONG: 'Long';
TYPE_FLOAT: 'Float';
TYPE_DOUBLE: 'Double';

// Boolean values
BOOLEAN_TRUE: 'true';
BOOLEAN_FALSE: 'false';

// Keywords for control flow and other constructs
CLASS: 'class';
FUN: 'fun';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
FOR: 'for';
IN: 'in';
PRINTLN: 'println';
READLINE: 'readLine';

// Punctuation and operators
COMMA: ',';  
SEMICOLON: ';';  
COLON: ':';  
DOT: '.';  
LEFT_ROUND_BRACKET: '(';
RIGHT_ROUND_BRACKET: ')';
LEFT_CURLY_BRACKET: '{';
RIGHT_CURLY_BRACKET: '}';
LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQ: '=';
EQEQ: '==';
NEQ: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
AND: '&&';
OR: '||';
NOT: '!';
RANGE: '..';
QUOTE: '"';
APEX: '\'';

// Identifiers: variable or function names
IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]* 
    ;

// Integer literals: numeric values
INT_LITERAL
    : [0-9]+
    ;

// String literals: text enclosed in double quotes
STRING_LITERAL
    : QUOTE (~["\\] | '\\' .)* QUOTE
    ;

// Comments: inline or block
LINE_COMMENT
    : '//' ~[\r\n]* 
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' 
    ;

// Whitespace: ignored during parsing
WS
    : [ \t\r\n]+ -> skip
    ;
