// Grammar definition
grammar Kotlin;

// Parser Rules 
program 
    : statement* EOF 
    ;

statement
    : ifStatement
    | forStatement
    | printStatement
    | readStatement
    | classDeclaration
    ;

ifStatement
    : 'if' '(' expression ')' block ('else' block)?
    ;

forStatement
    : 'for' '(' IDENTIFIER 'in' expression '..' expression ')' block
    ;

printStatement
    : 'println' '(' expression ')' ';'?
    ;

readStatement
    : IDENTIFIER '=' 'readline' '(' ')' ';'?
    ;

classDeclaration
    : 'class' IDENTIFIER '(' parameterList? ')' '{' classBody '}'
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : 'val' IDENTIFIER ':' type
    ;

classBody
    : (varDeclaration | functionDeclaration)*
    ;

varDeclaration
    : 'var' IDENTIFIER ':' type
    ;

functionDeclaration
    : 'fun' IDENTIFIER '(' parameterList? ')' block
    ;

block
    : '{' statement* '}'
    ;

// Expressions 
expression
    : literal                                        
    | IDENTIFIER     
    | expression ('+' | '-' | '*' | '/') expression
    | '(' expression ')'
    ;

// Literals 
literal
    : INT_LITERAL
    | BOOLEAN_LITERAL
    | STRING_LITERAL
    ;

// Lexical Rules 
type
    : 'Int'
    | 'Boolean'
    | 'String'
    ;

IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

INT_LITERAL
    : [0-9]+
    ;

BOOLEAN_LITERAL
    : 'true' | 'false'
    ;

STRING_LITERAL
    : '"' (~["\\] | '\\' .)* '"'
    ;

// Ignored Tokens 
WS
    : [ \t\r\n]+ -> skip
    ;
