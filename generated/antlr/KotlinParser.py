# Generated from antlr/Kotlin.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,0,1,0,1,1,1,1,3,
        1,81,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,3,1,3,
        1,3,1,3,3,3,98,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,107,8,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,122,8,6,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,130,8,7,1,7,1,7,1,7,3,7,135,8,7,3,7,137,8,
        7,1,8,3,8,140,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        10,1,10,5,10,155,8,10,10,10,12,10,158,9,10,1,10,1,10,1,11,1,11,1,
        12,1,12,1,12,5,12,167,8,12,10,12,12,12,170,9,12,1,13,1,13,1,13,5,
        13,175,8,13,10,13,12,13,178,9,13,1,14,1,14,1,14,1,14,1,14,5,14,185,
        8,14,10,14,12,14,188,9,14,1,15,1,15,1,15,3,15,193,8,15,1,16,1,16,
        1,16,5,16,198,8,16,10,16,12,16,201,9,16,1,17,1,17,1,17,5,17,206,
        8,17,10,17,12,17,209,9,17,1,18,1,18,1,18,1,18,1,18,3,18,216,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,224,8,19,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,237,8,21,1,22,1,22,1,22,
        3,22,242,8,22,1,23,1,23,1,24,1,24,1,24,1,24,3,24,250,8,24,1,24,3,
        24,253,8,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,5,25,262,8,25,10,
        25,12,25,265,9,25,1,26,1,26,1,26,1,26,3,26,271,8,26,1,26,1,26,1,
        26,3,26,276,8,26,1,26,1,26,1,27,1,27,1,27,3,27,283,8,27,1,27,1,27,
        1,28,1,28,1,28,1,29,1,29,1,29,5,29,293,8,29,10,29,12,29,296,9,29,
        1,30,1,30,1,30,1,30,1,30,3,30,303,8,30,1,31,1,31,1,31,5,31,308,8,
        31,10,31,12,31,311,9,31,1,32,1,32,3,32,315,8,32,1,32,1,32,1,33,1,
        33,1,34,1,34,1,34,0,0,35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,0,7,
        1,0,1,2,1,0,35,38,1,0,27,28,1,0,29,31,1,0,3,5,1,0,6,7,1,0,48,49,
        333,0,73,1,0,0,0,2,80,1,0,0,0,4,91,1,0,0,0,6,93,1,0,0,0,8,102,1,
        0,0,0,10,111,1,0,0,0,12,115,1,0,0,0,14,123,1,0,0,0,16,139,1,0,0,
        0,18,147,1,0,0,0,20,152,1,0,0,0,22,161,1,0,0,0,24,163,1,0,0,0,26,
        171,1,0,0,0,28,179,1,0,0,0,30,189,1,0,0,0,32,194,1,0,0,0,34,202,
        1,0,0,0,36,215,1,0,0,0,38,217,1,0,0,0,40,225,1,0,0,0,42,236,1,0,
        0,0,44,241,1,0,0,0,46,243,1,0,0,0,48,245,1,0,0,0,50,263,1,0,0,0,
        52,266,1,0,0,0,54,279,1,0,0,0,56,286,1,0,0,0,58,289,1,0,0,0,60,297,
        1,0,0,0,62,304,1,0,0,0,64,314,1,0,0,0,66,318,1,0,0,0,68,320,1,0,
        0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,0,0,1,77,1,1,0,0,0,78,
        81,3,48,24,0,79,81,3,68,34,0,80,78,1,0,0,0,80,79,1,0,0,0,81,3,1,
        0,0,0,82,92,3,16,8,0,83,92,3,18,9,0,84,92,3,14,7,0,85,92,3,12,6,
        0,86,92,3,6,3,0,87,92,3,8,4,0,88,92,3,10,5,0,89,92,3,52,26,0,90,
        92,3,56,28,0,91,82,1,0,0,0,91,83,1,0,0,0,91,84,1,0,0,0,91,85,1,0,
        0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,
        1,0,0,0,92,5,1,0,0,0,93,94,5,1,0,0,94,97,5,45,0,0,95,96,5,19,0,0,
        96,98,3,46,23,0,97,95,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,
        5,32,0,0,100,101,3,22,11,0,101,7,1,0,0,0,102,103,5,2,0,0,103,106,
        5,45,0,0,104,105,5,19,0,0,105,107,3,46,23,0,106,104,1,0,0,0,106,
        107,1,0,0,0,107,108,1,0,0,0,108,109,5,32,0,0,109,110,3,22,11,0,110,
        9,1,0,0,0,111,112,5,45,0,0,112,113,5,32,0,0,113,114,3,22,11,0,114,
        11,1,0,0,0,115,116,5,13,0,0,116,117,5,21,0,0,117,118,3,38,19,0,118,
        121,5,22,0,0,119,122,3,20,10,0,120,122,3,4,2,0,121,119,1,0,0,0,121,
        120,1,0,0,0,122,13,1,0,0,0,123,124,5,11,0,0,124,125,5,21,0,0,125,
        126,3,22,11,0,126,129,5,22,0,0,127,130,3,20,10,0,128,130,3,4,2,0,
        129,127,1,0,0,0,129,128,1,0,0,0,130,136,1,0,0,0,131,134,5,12,0,0,
        132,135,3,20,10,0,133,135,3,4,2,0,134,132,1,0,0,0,134,133,1,0,0,
        0,135,137,1,0,0,0,136,131,1,0,0,0,136,137,1,0,0,0,137,15,1,0,0,0,
        138,140,7,0,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,
        141,142,5,45,0,0,142,143,5,32,0,0,143,144,5,16,0,0,144,145,5,21,
        0,0,145,146,5,22,0,0,146,17,1,0,0,0,147,148,5,15,0,0,148,149,5,21,
        0,0,149,150,3,22,11,0,150,151,5,22,0,0,151,19,1,0,0,0,152,156,5,
        23,0,0,153,155,3,4,2,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,
        0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,160,5,
        24,0,0,160,21,1,0,0,0,161,162,3,24,12,0,162,23,1,0,0,0,163,168,3,
        26,13,0,164,165,5,40,0,0,165,167,3,26,13,0,166,164,1,0,0,0,167,170,
        1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,25,1,0,0,0,170,168,1,
        0,0,0,171,176,3,28,14,0,172,173,5,39,0,0,173,175,3,28,14,0,174,172,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,27,1,
        0,0,0,178,176,1,0,0,0,179,186,3,30,15,0,180,181,5,33,0,0,181,185,
        3,30,15,0,182,183,5,34,0,0,183,185,3,30,15,0,184,180,1,0,0,0,184,
        182,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,
        29,1,0,0,0,188,186,1,0,0,0,189,192,3,32,16,0,190,191,7,1,0,0,191,
        193,3,32,16,0,192,190,1,0,0,0,192,193,1,0,0,0,193,31,1,0,0,0,194,
        199,3,34,17,0,195,196,7,2,0,0,196,198,3,34,17,0,197,195,1,0,0,0,
        198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,33,1,0,0,0,201,
        199,1,0,0,0,202,207,3,36,18,0,203,204,7,3,0,0,204,206,3,36,18,0,
        205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,
        208,35,1,0,0,0,209,207,1,0,0,0,210,211,5,41,0,0,211,216,3,42,21,
        0,212,213,5,28,0,0,213,216,3,42,21,0,214,216,3,38,19,0,215,210,1,
        0,0,0,215,212,1,0,0,0,215,214,1,0,0,0,216,37,1,0,0,0,217,223,3,42,
        21,0,218,219,5,14,0,0,219,224,3,40,20,0,220,221,5,41,0,0,221,222,
        5,14,0,0,222,224,3,40,20,0,223,218,1,0,0,0,223,220,1,0,0,0,223,224,
        1,0,0,0,224,39,1,0,0,0,225,226,3,32,16,0,226,227,5,42,0,0,227,228,
        3,32,16,0,228,41,1,0,0,0,229,237,5,45,0,0,230,231,5,21,0,0,231,232,
        3,22,11,0,232,233,5,22,0,0,233,237,1,0,0,0,234,237,3,54,27,0,235,
        237,3,44,22,0,236,229,1,0,0,0,236,230,1,0,0,0,236,234,1,0,0,0,236,
        235,1,0,0,0,237,43,1,0,0,0,238,242,5,46,0,0,239,242,5,47,0,0,240,
        242,3,66,33,0,241,238,1,0,0,0,241,239,1,0,0,0,241,240,1,0,0,0,242,
        45,1,0,0,0,243,244,7,4,0,0,244,47,1,0,0,0,245,246,5,8,0,0,246,252,
        5,45,0,0,247,249,5,21,0,0,248,250,3,58,29,0,249,248,1,0,0,0,249,
        250,1,0,0,0,250,251,1,0,0,0,251,253,5,22,0,0,252,247,1,0,0,0,252,
        253,1,0,0,0,253,254,1,0,0,0,254,255,5,23,0,0,255,256,3,50,25,0,256,
        257,5,24,0,0,257,49,1,0,0,0,258,262,3,6,3,0,259,262,3,8,4,0,260,
        262,3,52,26,0,261,258,1,0,0,0,261,259,1,0,0,0,261,260,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,51,1,0,0,0,265,263,
        1,0,0,0,266,267,5,9,0,0,267,268,5,45,0,0,268,270,5,21,0,0,269,271,
        3,58,29,0,270,269,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,275,
        5,22,0,0,273,274,5,19,0,0,274,276,3,46,23,0,275,273,1,0,0,0,275,
        276,1,0,0,0,276,277,1,0,0,0,277,278,3,20,10,0,278,53,1,0,0,0,279,
        280,5,45,0,0,280,282,5,21,0,0,281,283,3,62,31,0,282,281,1,0,0,0,
        282,283,1,0,0,0,283,284,1,0,0,0,284,285,5,22,0,0,285,55,1,0,0,0,
        286,287,5,10,0,0,287,288,3,22,11,0,288,57,1,0,0,0,289,294,3,60,30,
        0,290,291,5,17,0,0,291,293,3,60,30,0,292,290,1,0,0,0,293,296,1,0,
        0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,59,1,0,0,0,296,294,1,0,0,
        0,297,298,5,45,0,0,298,299,5,19,0,0,299,302,3,46,23,0,300,301,5,
        32,0,0,301,303,3,22,11,0,302,300,1,0,0,0,302,303,1,0,0,0,303,61,
        1,0,0,0,304,309,3,64,32,0,305,306,5,17,0,0,306,308,3,64,32,0,307,
        305,1,0,0,0,308,311,1,0,0,0,309,307,1,0,0,0,309,310,1,0,0,0,310,
        63,1,0,0,0,311,309,1,0,0,0,312,313,5,45,0,0,313,315,5,32,0,0,314,
        312,1,0,0,0,314,315,1,0,0,0,315,316,1,0,0,0,316,317,3,22,11,0,317,
        65,1,0,0,0,318,319,7,5,0,0,319,67,1,0,0,0,320,321,7,6,0,0,321,69,
        1,0,0,0,33,73,80,91,97,106,121,129,134,136,139,156,168,176,184,186,
        192,199,207,215,223,236,241,249,252,261,263,270,275,282,294,302,
        309,314
    ]

class KotlinParser ( Parser ):

    grammarFileName = "Kotlin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'val'", "'Int'", "'String'", 
                     "'Boolean'", "'true'", "'false'", "'class'", "'fun'", 
                     "'return'", "'if'", "'else'", "'for'", "'in'", "'println'", 
                     "'readLine'", "','", "';'", "':'", "'.'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'='", "'=='", "'!='", "'>'", "'>='", "'<'", 
                     "'<='", "'&&'", "'||'", "'!'", "'..'", "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>", "VAR", "VAL", "TYPE_INT", "TYPE_STRING", 
                      "TYPE_BOOLEAN", "BOOLEAN_TRUE", "BOOLEAN_FALSE", "CLASS", 
                      "FUN", "RETURN", "IF", "ELSE", "FOR", "IN", "PRINTLN", 
                      "READLINE", "COMMA", "SEMICOLON", "COLON", "DOT", 
                      "LEFT_ROUND_BRACKET", "RIGHT_ROUND_BRACKET", "LEFT_CURLY_BRACKET", 
                      "RIGHT_CURLY_BRACKET", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQ", "EQEQ", 
                      "NEQ", "GT", "GTE", "LT", "LTE", "AND", "OR", "NOT", 
                      "RANGE", "QUOTE", "APEX", "IDENTIFIER", "INT_LITERAL", 
                      "STRING_LITERAL", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_topLevelStatement = 1
    RULE_statement = 2
    RULE_varDeclaration = 3
    RULE_valDeclaration = 4
    RULE_assignmentStatement = 5
    RULE_forStatement = 6
    RULE_ifStatement = 7
    RULE_readStatement = 8
    RULE_printStatement = 9
    RULE_block = 10
    RULE_expression = 11
    RULE_logicalOrExpression = 12
    RULE_logicalAndExpression = 13
    RULE_equalityExpression = 14
    RULE_relationalExpression = 15
    RULE_additiveExpression = 16
    RULE_multiplicativeExpression = 17
    RULE_unaryExpression = 18
    RULE_membershipExpression = 19
    RULE_rangeExpression = 20
    RULE_primaryExpression = 21
    RULE_literal = 22
    RULE_type = 23
    RULE_classDeclaration = 24
    RULE_classBody = 25
    RULE_functionDeclaration = 26
    RULE_callExpression = 27
    RULE_returnStatement = 28
    RULE_parameterList = 29
    RULE_parameter = 30
    RULE_argumentList = 31
    RULE_argument = 32
    RULE_booleanLiteral = 33
    RULE_commentStatement = 34

    ruleNames =  [ "program", "topLevelStatement", "statement", "varDeclaration", 
                   "valDeclaration", "assignmentStatement", "forStatement", 
                   "ifStatement", "readStatement", "printStatement", "block", 
                   "expression", "logicalOrExpression", "logicalAndExpression", 
                   "equalityExpression", "relationalExpression", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "membershipExpression", 
                   "rangeExpression", "primaryExpression", "literal", "type", 
                   "classDeclaration", "classBody", "functionDeclaration", 
                   "callExpression", "returnStatement", "parameterList", 
                   "parameter", "argumentList", "argument", "booleanLiteral", 
                   "commentStatement" ]

    EOF = Token.EOF
    VAR=1
    VAL=2
    TYPE_INT=3
    TYPE_STRING=4
    TYPE_BOOLEAN=5
    BOOLEAN_TRUE=6
    BOOLEAN_FALSE=7
    CLASS=8
    FUN=9
    RETURN=10
    IF=11
    ELSE=12
    FOR=13
    IN=14
    PRINTLN=15
    READLINE=16
    COMMA=17
    SEMICOLON=18
    COLON=19
    DOT=20
    LEFT_ROUND_BRACKET=21
    RIGHT_ROUND_BRACKET=22
    LEFT_CURLY_BRACKET=23
    RIGHT_CURLY_BRACKET=24
    LEFT_SQUARE_BRACKET=25
    RIGHT_SQUARE_BRACKET=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    MOD=31
    EQ=32
    EQEQ=33
    NEQ=34
    GT=35
    GTE=36
    LT=37
    LTE=38
    AND=39
    OR=40
    NOT=41
    RANGE=42
    QUOTE=43
    APEX=44
    IDENTIFIER=45
    INT_LITERAL=46
    STRING_LITERAL=47
    LINE_COMMENT=48
    BLOCK_COMMENT=49
    WS=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KotlinParser.EOF, 0)

        def topLevelStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.TopLevelStatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.TopLevelStatementContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = KotlinParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 844424930132224) != 0):
                self.state = 70
                self.topLevelStatement()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(KotlinParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ClassDeclarationContext,0)


        def commentStatement(self):
            return self.getTypedRuleContext(KotlinParser.CommentStatementContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_topLevelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelStatement" ):
                listener.enterTopLevelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelStatement" ):
                listener.exitTopLevelStatement(self)




    def topLevelStatement(self):

        localctx = KotlinParser.TopLevelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelStatement)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.classDeclaration()
                pass
            elif token in [48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.commentStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReadStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(KotlinParser.PrintStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(KotlinParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(KotlinParser.ForStatementContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.VarDeclarationContext,0)


        def valDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ValDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(KotlinParser.AssignmentStatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.FunctionDeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = KotlinParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.readStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.varDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.valDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.assignmentStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 89
                self.functionDeclaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.returnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(KotlinParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)




    def varDeclaration(self):

        localctx = KotlinParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(KotlinParser.VAR)
            self.state = 94
            self.match(KotlinParser.IDENTIFIER)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 95
                self.match(KotlinParser.COLON)
                self.state = 96
                self.type_()


            self.state = 99
            self.match(KotlinParser.EQ)
            self.state = 100
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(KotlinParser.VAL, 0)

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_valDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValDeclaration" ):
                listener.enterValDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValDeclaration" ):
                listener.exitValDeclaration(self)




    def valDeclaration(self):

        localctx = KotlinParser.ValDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(KotlinParser.VAL)
            self.state = 103
            self.match(KotlinParser.IDENTIFIER)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 104
                self.match(KotlinParser.COLON)
                self.state = 105
                self.type_()


            self.state = 108
            self.match(KotlinParser.EQ)
            self.state = 109
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = KotlinParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(KotlinParser.IDENTIFIER)
            self.state = 112
            self.match(KotlinParser.EQ)
            self.state = 113
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(KotlinParser.FOR, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def membershipExpression(self):
            return self.getTypedRuleContext(KotlinParser.MembershipExpressionContext,0)


        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def statement(self):
            return self.getTypedRuleContext(KotlinParser.StatementContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = KotlinParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(KotlinParser.FOR)
            self.state = 116
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 117
            self.membershipExpression()
            self.state = 118
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 119
                self.block()
                pass
            elif token in [1, 2, 9, 10, 11, 13, 15, 45]:
                self.state = 120
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(KotlinParser.IF, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.BlockContext)
            else:
                return self.getTypedRuleContext(KotlinParser.BlockContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(KotlinParser.ELSE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = KotlinParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(KotlinParser.IF)
            self.state = 124
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 125
            self.expression()
            self.state = 126
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 127
                self.block()
                pass
            elif token in [1, 2, 9, 10, 11, 13, 15, 45]:
                self.state = 128
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 131
                self.match(KotlinParser.ELSE)
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 132
                    self.block()
                    pass
                elif token in [1, 2, 9, 10, 11, 13, 15, 45]:
                    self.state = 133
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def READLINE(self):
            return self.getToken(KotlinParser.READLINE, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def VAR(self):
            return self.getToken(KotlinParser.VAR, 0)

        def VAL(self):
            return self.getToken(KotlinParser.VAL, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_readStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)




    def readStatement(self):

        localctx = KotlinParser.ReadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 141
            self.match(KotlinParser.IDENTIFIER)
            self.state = 142
            self.match(KotlinParser.EQ)
            self.state = 143
            self.match(KotlinParser.READLINE)
            self.state = 144
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 145
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(KotlinParser.PRINTLN, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = KotlinParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(KotlinParser.PRINTLN)
            self.state = 148
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 149
            self.expression()
            self.state = 150
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_CURLY_BRACKET, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = KotlinParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372133382) != 0):
                self.state = 153
                self.statement()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(KotlinParser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(KotlinParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = KotlinParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.OR)
            else:
                return self.getToken(KotlinParser.OR, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)




    def logicalOrExpression(self):

        localctx = KotlinParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.logicalAndExpression()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 164
                self.match(KotlinParser.OR)
                self.state = 165
                self.logicalAndExpression()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.AND)
            else:
                return self.getToken(KotlinParser.AND, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)




    def logicalAndExpression(self):

        localctx = KotlinParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.equalityExpression()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 172
                self.match(KotlinParser.AND)
                self.state = 173
                self.equalityExpression()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.RelationalExpressionContext,i)


        def EQEQ(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.EQEQ)
            else:
                return self.getToken(KotlinParser.EQEQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.NEQ)
            else:
                return self.getToken(KotlinParser.NEQ, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)




    def equalityExpression(self):

        localctx = KotlinParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.relationalExpression()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 184
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 180
                    self.match(KotlinParser.EQEQ)
                    self.state = 181
                    self.relationalExpression()
                    pass
                elif token in [34]:
                    self.state = 182
                    self.match(KotlinParser.NEQ)
                    self.state = 183
                    self.relationalExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.AdditiveExpressionContext,i)


        def GT(self):
            return self.getToken(KotlinParser.GT, 0)

        def GTE(self):
            return self.getToken(KotlinParser.GTE, 0)

        def LT(self):
            return self.getToken(KotlinParser.LT, 0)

        def LTE(self):
            return self.getToken(KotlinParser.LTE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)




    def relationalExpression(self):

        localctx = KotlinParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.additiveExpression()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0):
                self.state = 190
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.PLUS)
            else:
                return self.getToken(KotlinParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.MINUS)
            else:
                return self.getToken(KotlinParser.MINUS, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)




    def additiveExpression(self):

        localctx = KotlinParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.multiplicativeExpression()
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 195
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self.multiplicativeExpression() 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.UnaryExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.MULT)
            else:
                return self.getToken(KotlinParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.DIV)
            else:
                return self.getToken(KotlinParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.MOD)
            else:
                return self.getToken(KotlinParser.MOD, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)




    def multiplicativeExpression(self):

        localctx = KotlinParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.unaryExpression()
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 203
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.unaryExpression() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(KotlinParser.NOT, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(KotlinParser.PrimaryExpressionContext,0)


        def MINUS(self):
            return self.getToken(KotlinParser.MINUS, 0)

        def membershipExpression(self):
            return self.getTypedRuleContext(KotlinParser.MembershipExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = KotlinParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryExpression)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(KotlinParser.NOT)
                self.state = 211
                self.primaryExpression()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(KotlinParser.MINUS)
                self.state = 213
                self.primaryExpression()
                pass
            elif token in [6, 7, 21, 45, 46, 47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.membershipExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembershipExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(KotlinParser.PrimaryExpressionContext,0)


        def IN(self):
            return self.getToken(KotlinParser.IN, 0)

        def rangeExpression(self):
            return self.getTypedRuleContext(KotlinParser.RangeExpressionContext,0)


        def NOT(self):
            return self.getToken(KotlinParser.NOT, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_membershipExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembershipExpression" ):
                listener.enterMembershipExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembershipExpression" ):
                listener.exitMembershipExpression(self)




    def membershipExpression(self):

        localctx = KotlinParser.MembershipExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_membershipExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.primaryExpression()
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 218
                self.match(KotlinParser.IN)
                self.state = 219
                self.rangeExpression()
                pass
            elif token in [41]:
                self.state = 220
                self.match(KotlinParser.NOT)
                self.state = 221
                self.match(KotlinParser.IN)
                self.state = 222
                self.rangeExpression()
                pass
            elif token in [1, 2, 9, 10, 11, 12, 13, 15, 17, 22, 24, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 45]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.AdditiveExpressionContext,i)


        def RANGE(self):
            return self.getToken(KotlinParser.RANGE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_rangeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeExpression" ):
                listener.enterRangeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeExpression" ):
                listener.exitRangeExpression(self)




    def rangeExpression(self):

        localctx = KotlinParser.RangeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_rangeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.additiveExpression()
            self.state = 226
            self.match(KotlinParser.RANGE)
            self.state = 227
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def callExpression(self):
            return self.getTypedRuleContext(KotlinParser.CallExpressionContext,0)


        def literal(self):
            return self.getTypedRuleContext(KotlinParser.LiteralContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = KotlinParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_primaryExpression)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(KotlinParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 231
                self.expression()
                self.state = 232
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.callExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(KotlinParser.INT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(KotlinParser.STRING_LITERAL, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(KotlinParser.BooleanLiteralContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = KotlinParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(KotlinParser.INT_LITERAL)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(KotlinParser.STRING_LITERAL)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.booleanLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_INT(self):
            return self.getToken(KotlinParser.TYPE_INT, 0)

        def TYPE_STRING(self):
            return self.getToken(KotlinParser.TYPE_STRING, 0)

        def TYPE_BOOLEAN(self):
            return self.getToken(KotlinParser.TYPE_BOOLEAN, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = KotlinParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(KotlinParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_CURLY_BRACKET, 0)

        def classBody(self):
            return self.getTypedRuleContext(KotlinParser.ClassBodyContext,0)


        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_CURLY_BRACKET, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def parameterList(self):
            return self.getTypedRuleContext(KotlinParser.ParameterListContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)




    def classDeclaration(self):

        localctx = KotlinParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(KotlinParser.CLASS)
            self.state = 246
            self.match(KotlinParser.IDENTIFIER)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 247
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 248
                    self.parameterList()


                self.state = 251
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)


            self.state = 254
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 255
            self.classBody()
            self.state = 256
            self.match(KotlinParser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.VarDeclarationContext,i)


        def valDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ValDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ValDeclarationContext,i)


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)




    def classBody(self):

        localctx = KotlinParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 518) != 0):
                self.state = 261
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 258
                    self.varDeclaration()
                    pass
                elif token in [2]:
                    self.state = 259
                    self.valDeclaration()
                    pass
                elif token in [9]:
                    self.state = 260
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(KotlinParser.FUN, 0)

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(KotlinParser.ParameterListContext,0)


        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = KotlinParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(KotlinParser.FUN)
            self.state = 267
            self.match(KotlinParser.IDENTIFIER)
            self.state = 268
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 269
                self.parameterList()


            self.state = 272
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 273
                self.match(KotlinParser.COLON)
                self.state = 274
                self.type_()


            self.state = 277
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def argumentList(self):
            return self.getTypedRuleContext(KotlinParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_callExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallExpression" ):
                listener.enterCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallExpression" ):
                listener.exitCallExpression(self)




    def callExpression(self):

        localctx = KotlinParser.CallExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_callExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(KotlinParser.IDENTIFIER)
            self.state = 280
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 248489898410176) != 0):
                self.state = 281
                self.argumentList()


            self.state = 284
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(KotlinParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = KotlinParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(KotlinParser.RETURN)
            self.state = 287
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ParameterContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.COMMA)
            else:
                return self.getToken(KotlinParser.COMMA, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = KotlinParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.parameter()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 290
                self.match(KotlinParser.COMMA)
                self.state = 291
                self.parameter()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = KotlinParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(KotlinParser.IDENTIFIER)
            self.state = 298
            self.match(KotlinParser.COLON)
            self.state = 299
            self.type_()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 300
                self.match(KotlinParser.EQ)
                self.state = 301
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.COMMA)
            else:
                return self.getToken(KotlinParser.COMMA, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = KotlinParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.argument()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 305
                self.match(KotlinParser.COMMA)
                self.state = 306
                self.argument()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = KotlinParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 312
                self.match(KotlinParser.IDENTIFIER)
                self.state = 313
                self.match(KotlinParser.EQ)


            self.state = 316
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_TRUE(self):
            return self.getToken(KotlinParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(KotlinParser.BOOLEAN_FALSE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)




    def booleanLiteral(self):

        localctx = KotlinParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_COMMENT(self):
            return self.getToken(KotlinParser.LINE_COMMENT, 0)

        def BLOCK_COMMENT(self):
            return self.getToken(KotlinParser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_commentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentStatement" ):
                listener.enterCommentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentStatement" ):
                listener.exitCommentStatement(self)




    def commentStatement(self):

        localctx = KotlinParser.CommentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_commentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





