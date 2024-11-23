// Grammar definition
grammar Kotlin;

// Parser Rules 

// Entry point: the program consists of zero or more statements followed by EOF
program
    : topLevelStatement* EOF 
    ;

topLevelStatement
    : classDeclaration
    | commentStatement
    ;

// Statement rule: different types of statements like variable declarations, functions, etc.
statement
    : readStatement
    | printStatement
    | ifStatement
    | forStatement
    | assignmentStatement
    | varDeclaration
    | valDeclaration
    | functionDeclaration
    | returnStatement
    | commentStatement
    ;

// Code block, which can contain multiple statements.
block
    : LEFT_CURLY_BRACKET (statement)* RIGHT_CURLY_BRACKET
    ;

// Read statement: reads input, optionally assigning it to a variable.
readStatement
    : (VAR | VAL)? IDENTIFIER EQ READLINE LEFT_ROUND_BRACKET RIGHT_ROUND_BRACKET
    ;

// Print statement that prints an expression to the output.
printStatement
    : PRINTLN LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET
    ;

// Conditional 'if' statement with an optional 'else' block.
ifStatement
    : IF LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET (block | statement) ( ELSE (block | statement) )? 
    ;

// 'for' loop with a specified range.
forStatement
    : FOR LEFT_ROUND_BRACKET membershipExpression RIGHT_ROUND_BRACKET (block | statement)
    ;

// Assignment statement: variable assignment using '='.
assignmentStatement
    : IDENTIFIER EQ expression
    ;

// Variable declarations using 'var' with an optional type and initial value.
varDeclaration        
    : VAR IDENTIFIER (COLON type)? EQ expression
    ;

// Constant declarations using 'val' with an optional type and initial value.
valDeclaration
    : VAL IDENTIFIER (COLON type)? EQ expression
    ;

// Function declarations, including parameters and a block of code.
functionDeclaration
    : FUN IDENTIFIER LEFT_ROUND_BRACKET parameterList? RIGHT_ROUND_BRACKET (COLON type)? block
    ;

// Return statement: 'return' followed by an optional expression.
returnStatement
    : RETURN expression
    ;

// Class declarations with an optional constructor and a class body.
classDeclaration
    : CLASS IDENTIFIER (LEFT_ROUND_BRACKET parameterList? RIGHT_ROUND_BRACKET)? LEFT_CURLY_BRACKET classBody RIGHT_CURLY_BRACKET
    ;

// Class body, can contain variable declarations or functions.
classBody
    : (varDeclaration | valDeclaration | assignmentStatement | functionDeclaration | commentStatement)*
    ;

// Parameter list, used in function declarations.
parameterList
    : parameter (COMMA parameter)*
    ;

// Single parameter with an identifier, type, and an optional initial value.
parameter
    : IDENTIFIER COLON type (EQ expression)?
    ;

argumentList
    : argument (COMMA argument)*
    ;

// Single parameter with an identifier, type, and an optional initial value.
argument
    : (IDENTIFIER EQ)? expression
    ;

// Espressione di livello più alto (precedenza più bassa)
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
    : relationalExpression (EQEQ relationalExpression | NEQ relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((GT | GTE | LT | LTE ) additiveExpression)?
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
    : primaryExpression (IN rangeExpression | NOT IN rangeExpression)?
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

// Literal values, which can be integers, booleans, or strings.
literal
    : INT_LITERAL
    | STRING_LITERAL
    | booleanLiteral
    ;

// Boolean literals: 'true' or 'false'.
booleanLiteral
    : BOOLEAN_TRUE 
    | BOOLEAN_FALSE
    ;

commentStatement
    : LINE_COMMENT 
    | BLOCK_COMMENT
    ;

// Defines recognized types.
type
    : TYPE_INT
    | TYPE_STRING
    | TYPE_BOOLEAN
    ;

// Lexer Rules: Token definitions

VAR: 'var';
VAL: 'val';

TYPE_INT: 'Int';
TYPE_STRING: 'String';
TYPE_BOOLEAN: 'Boolean';

BOOLEAN_TRUE: 'true';
BOOLEAN_FALSE: 'false';

CLASS: 'class';
FUN: 'fun';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
FOR: 'for';
IN: 'in';
PRINTLN: 'println';
READLINE: 'readLine';

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

// Identifiers: letters or underscores followed by alphanumeric characters.
IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]* 
    ;

// Integer literals: sequences of digits.
INT_LITERAL
    : [0-9]+
    ;

// String literals: enclosed in double quotes, with escape characters allowed.
STRING_LITERAL
    : QUOTE (~["\\] | '\\' .)* QUOTE
    ;

// Ignores inline comments.
LINE_COMMENT
    : '//' ~[\r\n]* 
    ;

// Ignores block comments.
BLOCK_COMMENT
    : '/*' .*? '*/' 
    ;

// Skip whitespace characters (spaces, tabs, newlines).
WS
    : [ \t\r\n]+ -> skip
    ;
