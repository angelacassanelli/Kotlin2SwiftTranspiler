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
        4,1,50,325,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,0,1,0,1,1,1,1,3,
        1,81,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,3,1,3,
        5,3,96,8,3,10,3,12,3,99,9,3,1,3,1,3,1,4,3,4,104,8,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,123,
        8,6,1,6,1,6,1,6,3,6,128,8,6,3,6,130,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,138,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,148,8,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,3,10,157,8,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,3,11,166,8,11,1,11,1,11,1,11,3,11,171,8,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,3,13,182,8,13,1,13,3,13,185,8,13,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,196,8,14,10,14,12,
        14,199,9,14,1,15,1,15,1,15,5,15,204,8,15,10,15,12,15,207,9,15,1,
        16,1,16,1,16,1,16,1,16,3,16,214,8,16,1,17,1,17,1,17,5,17,219,8,17,
        10,17,12,17,222,9,17,1,18,1,18,3,18,226,8,18,1,18,1,18,1,19,1,19,
        1,20,1,20,1,20,5,20,235,8,20,10,20,12,20,238,9,20,1,21,1,21,1,21,
        5,21,243,8,21,10,21,12,21,246,9,21,1,22,1,22,1,22,1,22,1,22,5,22,
        253,8,22,10,22,12,22,256,9,22,1,23,1,23,1,23,3,23,261,8,23,1,24,
        1,24,1,24,5,24,266,8,24,10,24,12,24,269,9,24,1,25,1,25,1,25,5,25,
        274,8,25,10,25,12,25,277,9,25,1,26,1,26,1,26,1,26,1,26,3,26,284,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,292,8,27,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,3,28,301,8,28,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,3,30,310,8,30,1,30,1,30,1,31,1,31,1,31,3,31,317,8,31,1,32,1,
        32,1,33,1,33,1,34,1,34,1,34,0,0,35,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,0,7,1,0,1,2,1,0,35,38,1,0,27,28,1,0,29,31,1,0,6,7,1,0,48,49,1,
        0,3,5,337,0,73,1,0,0,0,2,80,1,0,0,0,4,91,1,0,0,0,6,93,1,0,0,0,8,
        103,1,0,0,0,10,111,1,0,0,0,12,116,1,0,0,0,14,131,1,0,0,0,16,139,
        1,0,0,0,18,143,1,0,0,0,20,152,1,0,0,0,22,161,1,0,0,0,24,174,1,0,
        0,0,26,177,1,0,0,0,28,197,1,0,0,0,30,200,1,0,0,0,32,208,1,0,0,0,
        34,215,1,0,0,0,36,225,1,0,0,0,38,229,1,0,0,0,40,231,1,0,0,0,42,239,
        1,0,0,0,44,247,1,0,0,0,46,257,1,0,0,0,48,262,1,0,0,0,50,270,1,0,
        0,0,52,283,1,0,0,0,54,285,1,0,0,0,56,300,1,0,0,0,58,302,1,0,0,0,
        60,306,1,0,0,0,62,316,1,0,0,0,64,318,1,0,0,0,66,320,1,0,0,0,68,322,
        1,0,0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,
        73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,0,0,1,77,1,1,0,
        0,0,78,81,3,26,13,0,79,81,3,66,33,0,80,78,1,0,0,0,80,79,1,0,0,0,
        81,3,1,0,0,0,82,92,3,8,4,0,83,92,3,10,5,0,84,92,3,12,6,0,85,92,3,
        14,7,0,86,92,3,16,8,0,87,92,3,18,9,0,88,92,3,20,10,0,89,92,3,24,
        12,0,90,92,3,66,33,0,91,82,1,0,0,0,91,83,1,0,0,0,91,84,1,0,0,0,91,
        85,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,
        0,91,90,1,0,0,0,92,5,1,0,0,0,93,97,5,23,0,0,94,96,3,4,2,0,95,94,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,
        99,97,1,0,0,0,100,101,5,24,0,0,101,7,1,0,0,0,102,104,7,0,0,0,103,
        102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,45,0,0,106,
        107,5,32,0,0,107,108,5,16,0,0,108,109,5,21,0,0,109,110,5,22,0,0,
        110,9,1,0,0,0,111,112,5,15,0,0,112,113,5,21,0,0,113,114,3,38,19,
        0,114,115,5,22,0,0,115,11,1,0,0,0,116,117,5,11,0,0,117,118,5,21,
        0,0,118,119,3,38,19,0,119,122,5,22,0,0,120,123,3,6,3,0,121,123,3,
        4,2,0,122,120,1,0,0,0,122,121,1,0,0,0,123,129,1,0,0,0,124,127,5,
        12,0,0,125,128,3,6,3,0,126,128,3,4,2,0,127,125,1,0,0,0,127,126,1,
        0,0,0,128,130,1,0,0,0,129,124,1,0,0,0,129,130,1,0,0,0,130,13,1,0,
        0,0,131,132,5,13,0,0,132,133,5,21,0,0,133,134,3,54,27,0,134,137,
        5,22,0,0,135,138,3,6,3,0,136,138,3,4,2,0,137,135,1,0,0,0,137,136,
        1,0,0,0,138,15,1,0,0,0,139,140,5,45,0,0,140,141,5,32,0,0,141,142,
        3,38,19,0,142,17,1,0,0,0,143,144,5,1,0,0,144,147,5,45,0,0,145,146,
        5,19,0,0,146,148,3,68,34,0,147,145,1,0,0,0,147,148,1,0,0,0,148,149,
        1,0,0,0,149,150,5,32,0,0,150,151,3,38,19,0,151,19,1,0,0,0,152,153,
        5,2,0,0,153,156,5,45,0,0,154,155,5,19,0,0,155,157,3,68,34,0,156,
        154,1,0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,5,32,0,0,159,
        160,3,38,19,0,160,21,1,0,0,0,161,162,5,9,0,0,162,163,5,45,0,0,163,
        165,5,21,0,0,164,166,3,30,15,0,165,164,1,0,0,0,165,166,1,0,0,0,166,
        167,1,0,0,0,167,170,5,22,0,0,168,169,5,19,0,0,169,171,3,68,34,0,
        170,168,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,3,6,3,0,
        173,23,1,0,0,0,174,175,5,10,0,0,175,176,3,38,19,0,176,25,1,0,0,0,
        177,178,5,8,0,0,178,184,5,45,0,0,179,181,5,21,0,0,180,182,3,30,15,
        0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,185,5,22,0,
        0,184,179,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,187,5,23,0,
        0,187,188,3,28,14,0,188,189,5,24,0,0,189,27,1,0,0,0,190,196,3,18,
        9,0,191,196,3,20,10,0,192,196,3,16,8,0,193,196,3,22,11,0,194,196,
        3,66,33,0,195,190,1,0,0,0,195,191,1,0,0,0,195,192,1,0,0,0,195,193,
        1,0,0,0,195,194,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,
        1,0,0,0,198,29,1,0,0,0,199,197,1,0,0,0,200,205,3,32,16,0,201,202,
        5,17,0,0,202,204,3,32,16,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,31,1,0,0,0,207,205,1,0,0,0,208,209,5,
        45,0,0,209,210,5,19,0,0,210,213,3,68,34,0,211,212,5,32,0,0,212,214,
        3,38,19,0,213,211,1,0,0,0,213,214,1,0,0,0,214,33,1,0,0,0,215,220,
        3,36,18,0,216,217,5,17,0,0,217,219,3,36,18,0,218,216,1,0,0,0,219,
        222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,35,1,0,0,0,222,220,
        1,0,0,0,223,224,5,45,0,0,224,226,5,32,0,0,225,223,1,0,0,0,225,226,
        1,0,0,0,226,227,1,0,0,0,227,228,3,38,19,0,228,37,1,0,0,0,229,230,
        3,40,20,0,230,39,1,0,0,0,231,236,3,42,21,0,232,233,5,40,0,0,233,
        235,3,42,21,0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,
        237,1,0,0,0,237,41,1,0,0,0,238,236,1,0,0,0,239,244,3,44,22,0,240,
        241,5,39,0,0,241,243,3,44,22,0,242,240,1,0,0,0,243,246,1,0,0,0,244,
        242,1,0,0,0,244,245,1,0,0,0,245,43,1,0,0,0,246,244,1,0,0,0,247,254,
        3,46,23,0,248,249,5,33,0,0,249,253,3,46,23,0,250,251,5,34,0,0,251,
        253,3,46,23,0,252,248,1,0,0,0,252,250,1,0,0,0,253,256,1,0,0,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,45,1,0,0,0,256,254,1,0,0,0,257,260,
        3,48,24,0,258,259,7,1,0,0,259,261,3,48,24,0,260,258,1,0,0,0,260,
        261,1,0,0,0,261,47,1,0,0,0,262,267,3,50,25,0,263,264,7,2,0,0,264,
        266,3,50,25,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,49,1,0,0,0,269,267,1,0,0,0,270,275,3,52,26,0,271,
        272,7,3,0,0,272,274,3,52,26,0,273,271,1,0,0,0,274,277,1,0,0,0,275,
        273,1,0,0,0,275,276,1,0,0,0,276,51,1,0,0,0,277,275,1,0,0,0,278,279,
        5,41,0,0,279,284,3,56,28,0,280,281,5,28,0,0,281,284,3,56,28,0,282,
        284,3,54,27,0,283,278,1,0,0,0,283,280,1,0,0,0,283,282,1,0,0,0,284,
        53,1,0,0,0,285,291,3,56,28,0,286,287,5,14,0,0,287,292,3,58,29,0,
        288,289,5,41,0,0,289,290,5,14,0,0,290,292,3,58,29,0,291,286,1,0,
        0,0,291,288,1,0,0,0,291,292,1,0,0,0,292,55,1,0,0,0,293,301,5,45,
        0,0,294,295,5,21,0,0,295,296,3,38,19,0,296,297,5,22,0,0,297,301,
        1,0,0,0,298,301,3,60,30,0,299,301,3,62,31,0,300,293,1,0,0,0,300,
        294,1,0,0,0,300,298,1,0,0,0,300,299,1,0,0,0,301,57,1,0,0,0,302,303,
        3,48,24,0,303,304,5,42,0,0,304,305,3,48,24,0,305,59,1,0,0,0,306,
        307,5,45,0,0,307,309,5,21,0,0,308,310,3,34,17,0,309,308,1,0,0,0,
        309,310,1,0,0,0,310,311,1,0,0,0,311,312,5,22,0,0,312,61,1,0,0,0,
        313,317,5,46,0,0,314,317,5,47,0,0,315,317,3,64,32,0,316,313,1,0,
        0,0,316,314,1,0,0,0,316,315,1,0,0,0,317,63,1,0,0,0,318,319,7,4,0,
        0,319,65,1,0,0,0,320,321,7,5,0,0,321,67,1,0,0,0,322,323,7,6,0,0,
        323,69,1,0,0,0,33,73,80,91,97,103,122,127,129,137,147,156,165,170,
        181,184,195,197,205,213,220,225,236,244,252,254,260,267,275,283,
        291,300,309,316
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
    RULE_block = 3
    RULE_readStatement = 4
    RULE_printStatement = 5
    RULE_ifStatement = 6
    RULE_forStatement = 7
    RULE_assignmentStatement = 8
    RULE_varDeclaration = 9
    RULE_valDeclaration = 10
    RULE_functionDeclaration = 11
    RULE_returnStatement = 12
    RULE_classDeclaration = 13
    RULE_classBody = 14
    RULE_parameterList = 15
    RULE_parameter = 16
    RULE_argumentList = 17
    RULE_argument = 18
    RULE_expression = 19
    RULE_logicalOrExpression = 20
    RULE_logicalAndExpression = 21
    RULE_equalityExpression = 22
    RULE_relationalExpression = 23
    RULE_additiveExpression = 24
    RULE_multiplicativeExpression = 25
    RULE_unaryExpression = 26
    RULE_membershipExpression = 27
    RULE_primaryExpression = 28
    RULE_rangeExpression = 29
    RULE_callExpression = 30
    RULE_literal = 31
    RULE_booleanLiteral = 32
    RULE_commentStatement = 33
    RULE_type = 34

    ruleNames =  [ "program", "topLevelStatement", "statement", "block", 
                   "readStatement", "printStatement", "ifStatement", "forStatement", 
                   "assignmentStatement", "varDeclaration", "valDeclaration", 
                   "functionDeclaration", "returnStatement", "classDeclaration", 
                   "classBody", "parameterList", "parameter", "argumentList", 
                   "argument", "expression", "logicalOrExpression", "logicalAndExpression", 
                   "equalityExpression", "relationalExpression", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "membershipExpression", 
                   "primaryExpression", "rangeExpression", "callExpression", 
                   "literal", "booleanLiteral", "commentStatement", "type" ]

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


        def assignmentStatement(self):
            return self.getTypedRuleContext(KotlinParser.AssignmentStatementContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.VarDeclarationContext,0)


        def valDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ValDeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReturnStatementContext,0)


        def commentStatement(self):
            return self.getTypedRuleContext(KotlinParser.CommentStatementContext,0)


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
                self.assignmentStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.varDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.valDeclaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 89
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.commentStatement()
                pass


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
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 879609302264838) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(KotlinParser.RIGHT_CURLY_BRACKET)
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
        self.enterRule(localctx, 8, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 102
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 105
            self.match(KotlinParser.IDENTIFIER)
            self.state = 106
            self.match(KotlinParser.EQ)
            self.state = 107
            self.match(KotlinParser.READLINE)
            self.state = 108
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 109
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
        self.enterRule(localctx, 10, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(KotlinParser.PRINTLN)
            self.state = 112
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
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
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(KotlinParser.IF)
            self.state = 117
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 118
            self.expression()
            self.state = 119
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 120
                self.block()
                pass
            elif token in [1, 2, 10, 11, 13, 15, 45, 48, 49]:
                self.state = 121
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 124
                self.match(KotlinParser.ELSE)
                self.state = 127
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 125
                    self.block()
                    pass
                elif token in [1, 2, 10, 11, 13, 15, 45, 48, 49]:
                    self.state = 126
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
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(KotlinParser.FOR)
            self.state = 132
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 133
            self.membershipExpression()
            self.state = 134
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 135
                self.block()
                pass
            elif token in [1, 2, 10, 11, 13, 15, 45, 48, 49]:
                self.state = 136
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
        self.enterRule(localctx, 16, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(KotlinParser.IDENTIFIER)
            self.state = 140
            self.match(KotlinParser.EQ)
            self.state = 141
            self.expression()
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
        self.enterRule(localctx, 18, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(KotlinParser.VAR)
            self.state = 144
            self.match(KotlinParser.IDENTIFIER)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 145
                self.match(KotlinParser.COLON)
                self.state = 146
                self.type_()


            self.state = 149
            self.match(KotlinParser.EQ)
            self.state = 150
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
        self.enterRule(localctx, 20, self.RULE_valDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(KotlinParser.VAL)
            self.state = 153
            self.match(KotlinParser.IDENTIFIER)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 154
                self.match(KotlinParser.COLON)
                self.state = 155
                self.type_()


            self.state = 158
            self.match(KotlinParser.EQ)
            self.state = 159
            self.expression()
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
        self.enterRule(localctx, 22, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(KotlinParser.FUN)
            self.state = 162
            self.match(KotlinParser.IDENTIFIER)
            self.state = 163
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 164
                self.parameterList()


            self.state = 167
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 168
                self.match(KotlinParser.COLON)
                self.state = 169
                self.type_()


            self.state = 172
            self.block()
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
        self.enterRule(localctx, 24, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(KotlinParser.RETURN)
            self.state = 175
            self.expression()
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
        self.enterRule(localctx, 26, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(KotlinParser.CLASS)
            self.state = 178
            self.match(KotlinParser.IDENTIFIER)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 179
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 180
                    self.parameterList()


                self.state = 183
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)


            self.state = 186
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 187
            self.classBody()
            self.state = 188
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


        def assignmentStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.AssignmentStatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.AssignmentStatementContext,i)


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.FunctionDeclarationContext,i)


        def commentStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.CommentStatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.CommentStatementContext,i)


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
        self.enterRule(localctx, 28, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 879609302221318) != 0):
                self.state = 195
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 190
                    self.varDeclaration()
                    pass
                elif token in [2]:
                    self.state = 191
                    self.valDeclaration()
                    pass
                elif token in [45]:
                    self.state = 192
                    self.assignmentStatement()
                    pass
                elif token in [9]:
                    self.state = 193
                    self.functionDeclaration()
                    pass
                elif token in [48, 49]:
                    self.state = 194
                    self.commentStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 30, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.parameter()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 201
                self.match(KotlinParser.COMMA)
                self.state = 202
                self.parameter()
                self.state = 207
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
        self.enterRule(localctx, 32, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(KotlinParser.IDENTIFIER)
            self.state = 209
            self.match(KotlinParser.COLON)
            self.state = 210
            self.type_()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 211
                self.match(KotlinParser.EQ)
                self.state = 212
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
        self.enterRule(localctx, 34, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.argument()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 216
                self.match(KotlinParser.COMMA)
                self.state = 217
                self.argument()
                self.state = 222
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
        self.enterRule(localctx, 36, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 223
                self.match(KotlinParser.IDENTIFIER)
                self.state = 224
                self.match(KotlinParser.EQ)


            self.state = 227
            self.expression()
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
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
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
        self.enterRule(localctx, 40, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.logicalAndExpression()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 232
                self.match(KotlinParser.OR)
                self.state = 233
                self.logicalAndExpression()
                self.state = 238
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
        self.enterRule(localctx, 42, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.equalityExpression()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 240
                self.match(KotlinParser.AND)
                self.state = 241
                self.equalityExpression()
                self.state = 246
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
        self.enterRule(localctx, 44, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.relationalExpression()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 252
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 248
                    self.match(KotlinParser.EQEQ)
                    self.state = 249
                    self.relationalExpression()
                    pass
                elif token in [34]:
                    self.state = 250
                    self.match(KotlinParser.NEQ)
                    self.state = 251
                    self.relationalExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 256
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
        self.enterRule(localctx, 46, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.additiveExpression()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0):
                self.state = 258
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 259
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
        self.enterRule(localctx, 48, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.multiplicativeExpression()
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 263
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.multiplicativeExpression() 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.unaryExpression()
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 271
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 272
                    self.unaryExpression() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 52, self.RULE_unaryExpression)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(KotlinParser.NOT)
                self.state = 279
                self.primaryExpression()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(KotlinParser.MINUS)
                self.state = 281
                self.primaryExpression()
                pass
            elif token in [6, 7, 21, 45, 46, 47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
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
        self.enterRule(localctx, 54, self.RULE_membershipExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.primaryExpression()
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 286
                self.match(KotlinParser.IN)
                self.state = 287
                self.rangeExpression()
                pass
            elif token in [41]:
                self.state = 288
                self.match(KotlinParser.NOT)
                self.state = 289
                self.match(KotlinParser.IN)
                self.state = 290
                self.rangeExpression()
                pass
            elif token in [1, 2, 9, 10, 11, 12, 13, 15, 17, 22, 24, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 45, 48, 49]:
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
        self.enterRule(localctx, 56, self.RULE_primaryExpression)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(KotlinParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 295
                self.expression()
                self.state = 296
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.callExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.literal()
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
        self.enterRule(localctx, 58, self.RULE_rangeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.additiveExpression()
            self.state = 303
            self.match(KotlinParser.RANGE)
            self.state = 304
            self.additiveExpression()
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
        self.enterRule(localctx, 60, self.RULE_callExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(KotlinParser.IDENTIFIER)
            self.state = 307
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 248489898410176) != 0):
                self.state = 308
                self.argumentList()


            self.state = 311
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
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
        self.enterRule(localctx, 62, self.RULE_literal)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(KotlinParser.INT_LITERAL)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(KotlinParser.STRING_LITERAL)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
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
        self.enterRule(localctx, 64, self.RULE_booleanLiteral)
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
        self.enterRule(localctx, 66, self.RULE_commentStatement)
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
        self.enterRule(localctx, 68, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
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





