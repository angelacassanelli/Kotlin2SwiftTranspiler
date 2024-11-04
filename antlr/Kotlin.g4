// Grammar definition
grammar Kotlin;

// Parser Rules 
program 
    : statement* EOF 
    ;

statement
    : varDeclaration
    | valDeclaration
    | ifStatement
    | forStatement
    | printStatement
    | readStatement
    | classDeclaration
    ;

varDeclaration
    : 'var' IDENTIFIER (':' type)? ('=' expression)? ';'?
    ;

valDeclaration
    : 'val' IDENTIFIER (':' type)? ('=' expression)? ';'?
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
    : ('var' | 'val')? IDENTIFIER '=' 'readLine' '(' ')' ';'?
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : IDENTIFIER ':' type
    ;

functionDeclaration
    : 'fun' IDENTIFIER '(' parameterList? ')' block
    ;

classBody
    : (varDeclaration | functionDeclaration)*
    ;

classDeclaration
    : 'class' IDENTIFIER '(' parameterList? ')' '{' classBody '}'
    ;

block
    : '{' statement* '}'
    ;

// Expressions 
expression
    : literal                                        
    | IDENTIFIER     
    | expression ('+' | '-' | '*' | '/' | '==') expression
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
