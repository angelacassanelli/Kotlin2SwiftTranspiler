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
        4,1,50,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,82,
        8,1,1,2,1,2,1,2,1,2,3,2,88,8,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,97,
        8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,118,8,6,1,6,1,6,1,6,3,6,123,8,6,3,6,125,8,6,
        1,7,3,7,128,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,5,9,145,8,9,10,9,12,9,148,9,9,1,9,1,9,1,10,1,10,1,11,
        1,11,1,11,5,11,157,8,11,10,11,12,11,160,9,11,1,12,1,12,1,12,5,12,
        165,8,12,10,12,12,12,168,9,12,1,13,1,13,1,13,1,13,1,13,5,13,175,
        8,13,10,13,12,13,178,9,13,1,14,1,14,1,14,3,14,183,8,14,1,15,1,15,
        1,15,5,15,188,8,15,10,15,12,15,191,9,15,1,16,1,16,1,16,5,16,196,
        8,16,10,16,12,16,199,9,16,1,17,1,17,1,17,1,17,1,17,3,17,206,8,17,
        1,18,1,18,1,18,1,18,1,18,1,18,3,18,214,8,18,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,20,3,20,226,8,20,1,21,1,21,1,21,3,21,
        231,8,21,1,22,1,22,1,23,1,23,1,23,1,23,3,23,239,8,23,1,23,3,23,242,
        8,23,1,23,1,23,1,23,1,23,1,24,1,24,5,24,250,8,24,10,24,12,24,253,
        9,24,1,25,1,25,1,25,1,25,3,25,259,8,25,1,25,1,25,1,25,3,25,264,8,
        25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,5,27,274,8,27,10,27,12,
        27,277,9,27,1,28,1,28,1,28,1,28,1,28,3,28,284,8,28,1,29,1,29,1,30,
        1,30,1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,0,7,1,0,1,2,1,0,35,38,1,0,
        27,28,1,0,29,31,1,0,3,5,1,0,6,7,1,0,48,49,301,0,65,1,0,0,0,2,81,
        1,0,0,0,4,83,1,0,0,0,6,92,1,0,0,0,8,101,1,0,0,0,10,105,1,0,0,0,12,
        111,1,0,0,0,14,127,1,0,0,0,16,135,1,0,0,0,18,140,1,0,0,0,20,151,
        1,0,0,0,22,153,1,0,0,0,24,161,1,0,0,0,26,169,1,0,0,0,28,179,1,0,
        0,0,30,184,1,0,0,0,32,192,1,0,0,0,34,205,1,0,0,0,36,207,1,0,0,0,
        38,215,1,0,0,0,40,225,1,0,0,0,42,230,1,0,0,0,44,232,1,0,0,0,46,234,
        1,0,0,0,48,251,1,0,0,0,50,254,1,0,0,0,52,267,1,0,0,0,54,270,1,0,
        0,0,56,278,1,0,0,0,58,285,1,0,0,0,60,287,1,0,0,0,62,64,3,2,1,0,63,
        62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,
        0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,82,3,46,23,0,71,82,
        3,50,25,0,72,82,3,4,2,0,73,82,3,6,3,0,74,82,3,8,4,0,75,82,3,52,26,
        0,76,82,3,12,6,0,77,82,3,10,5,0,78,82,3,16,8,0,79,82,3,14,7,0,80,
        82,3,60,30,0,81,70,1,0,0,0,81,71,1,0,0,0,81,72,1,0,0,0,81,73,1,0,
        0,0,81,74,1,0,0,0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,81,78,
        1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,84,5,1,0,0,84,
        87,5,45,0,0,85,86,5,19,0,0,86,88,3,44,22,0,87,85,1,0,0,0,87,88,1,
        0,0,0,88,89,1,0,0,0,89,90,5,32,0,0,90,91,3,20,10,0,91,5,1,0,0,0,
        92,93,5,2,0,0,93,96,5,45,0,0,94,95,5,19,0,0,95,97,3,44,22,0,96,94,
        1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,32,0,0,99,100,3,20,10,
        0,100,7,1,0,0,0,101,102,5,45,0,0,102,103,5,32,0,0,103,104,3,20,10,
        0,104,9,1,0,0,0,105,106,5,13,0,0,106,107,5,21,0,0,107,108,3,36,18,
        0,108,109,5,22,0,0,109,110,3,18,9,0,110,11,1,0,0,0,111,112,5,11,
        0,0,112,113,5,21,0,0,113,114,3,20,10,0,114,117,5,22,0,0,115,118,
        3,18,9,0,116,118,3,2,1,0,117,115,1,0,0,0,117,116,1,0,0,0,118,124,
        1,0,0,0,119,122,5,12,0,0,120,123,3,18,9,0,121,123,3,2,1,0,122,120,
        1,0,0,0,122,121,1,0,0,0,123,125,1,0,0,0,124,119,1,0,0,0,124,125,
        1,0,0,0,125,13,1,0,0,0,126,128,7,0,0,0,127,126,1,0,0,0,127,128,1,
        0,0,0,128,129,1,0,0,0,129,130,5,45,0,0,130,131,5,32,0,0,131,132,
        5,16,0,0,132,133,5,21,0,0,133,134,5,22,0,0,134,15,1,0,0,0,135,136,
        5,15,0,0,136,137,5,21,0,0,137,138,3,20,10,0,138,139,5,22,0,0,139,
        17,1,0,0,0,140,146,5,23,0,0,141,145,3,4,2,0,142,145,3,50,25,0,143,
        145,3,2,1,0,144,141,1,0,0,0,144,142,1,0,0,0,144,143,1,0,0,0,145,
        148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,
        146,1,0,0,0,149,150,5,24,0,0,150,19,1,0,0,0,151,152,3,22,11,0,152,
        21,1,0,0,0,153,158,3,24,12,0,154,155,5,40,0,0,155,157,3,24,12,0,
        156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,
        159,23,1,0,0,0,160,158,1,0,0,0,161,166,3,26,13,0,162,163,5,39,0,
        0,163,165,3,26,13,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,
        0,0,166,167,1,0,0,0,167,25,1,0,0,0,168,166,1,0,0,0,169,176,3,28,
        14,0,170,171,5,33,0,0,171,175,3,28,14,0,172,173,5,34,0,0,173,175,
        3,28,14,0,174,170,1,0,0,0,174,172,1,0,0,0,175,178,1,0,0,0,176,174,
        1,0,0,0,176,177,1,0,0,0,177,27,1,0,0,0,178,176,1,0,0,0,179,182,3,
        30,15,0,180,181,7,1,0,0,181,183,3,30,15,0,182,180,1,0,0,0,182,183,
        1,0,0,0,183,29,1,0,0,0,184,189,3,32,16,0,185,186,7,2,0,0,186,188,
        3,32,16,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,31,1,0,0,0,191,189,1,0,0,0,192,197,3,34,17,0,193,194,
        7,3,0,0,194,196,3,34,17,0,195,193,1,0,0,0,196,199,1,0,0,0,197,195,
        1,0,0,0,197,198,1,0,0,0,198,33,1,0,0,0,199,197,1,0,0,0,200,201,5,
        41,0,0,201,206,3,40,20,0,202,203,5,28,0,0,203,206,3,40,20,0,204,
        206,3,36,18,0,205,200,1,0,0,0,205,202,1,0,0,0,205,204,1,0,0,0,206,
        35,1,0,0,0,207,213,3,40,20,0,208,209,5,14,0,0,209,214,3,38,19,0,
        210,211,5,41,0,0,211,212,5,14,0,0,212,214,3,38,19,0,213,208,1,0,
        0,0,213,210,1,0,0,0,213,214,1,0,0,0,214,37,1,0,0,0,215,216,3,30,
        15,0,216,217,5,42,0,0,217,218,3,30,15,0,218,39,1,0,0,0,219,226,5,
        45,0,0,220,226,3,42,21,0,221,222,5,21,0,0,222,223,3,20,10,0,223,
        224,5,22,0,0,224,226,1,0,0,0,225,219,1,0,0,0,225,220,1,0,0,0,225,
        221,1,0,0,0,226,41,1,0,0,0,227,231,5,46,0,0,228,231,5,47,0,0,229,
        231,3,58,29,0,230,227,1,0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,
        43,1,0,0,0,232,233,7,4,0,0,233,45,1,0,0,0,234,235,5,8,0,0,235,241,
        5,45,0,0,236,238,5,21,0,0,237,239,3,54,27,0,238,237,1,0,0,0,238,
        239,1,0,0,0,239,240,1,0,0,0,240,242,5,22,0,0,241,236,1,0,0,0,241,
        242,1,0,0,0,242,243,1,0,0,0,243,244,5,23,0,0,244,245,3,48,24,0,245,
        246,5,24,0,0,246,47,1,0,0,0,247,250,3,4,2,0,248,250,3,50,25,0,249,
        247,1,0,0,0,249,248,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,
        252,1,0,0,0,252,49,1,0,0,0,253,251,1,0,0,0,254,255,5,9,0,0,255,256,
        5,45,0,0,256,258,5,21,0,0,257,259,3,54,27,0,258,257,1,0,0,0,258,
        259,1,0,0,0,259,260,1,0,0,0,260,263,5,22,0,0,261,262,5,19,0,0,262,
        264,3,44,22,0,263,261,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,
        266,3,18,9,0,266,51,1,0,0,0,267,268,5,10,0,0,268,269,3,20,10,0,269,
        53,1,0,0,0,270,275,3,56,28,0,271,272,5,17,0,0,272,274,3,56,28,0,
        273,271,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,
        276,55,1,0,0,0,277,275,1,0,0,0,278,279,5,45,0,0,279,280,5,19,0,0,
        280,283,3,44,22,0,281,282,5,32,0,0,282,284,3,42,21,0,283,281,1,0,
        0,0,283,284,1,0,0,0,284,57,1,0,0,0,285,286,7,5,0,0,286,59,1,0,0,
        0,287,288,7,6,0,0,288,61,1,0,0,0,29,65,81,87,96,117,122,124,127,
        144,146,158,166,174,176,182,189,197,205,213,225,230,238,241,249,
        251,258,263,275,283
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
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_valDeclaration = 3
    RULE_assignmentStatement = 4
    RULE_forStatement = 5
    RULE_ifStatement = 6
    RULE_readStatement = 7
    RULE_printStatement = 8
    RULE_block = 9
    RULE_expression = 10
    RULE_logicalOrExpression = 11
    RULE_logicalAndExpression = 12
    RULE_equalityExpression = 13
    RULE_relationalExpression = 14
    RULE_additiveExpression = 15
    RULE_multiplicativeExpression = 16
    RULE_unaryExpression = 17
    RULE_membershipExpression = 18
    RULE_rangeExpression = 19
    RULE_primaryExpression = 20
    RULE_literal = 21
    RULE_type = 22
    RULE_classDeclaration = 23
    RULE_classBody = 24
    RULE_functionDeclaration = 25
    RULE_returnStatement = 26
    RULE_parameterList = 27
    RULE_parameter = 28
    RULE_booleanLiteral = 29
    RULE_commentStatement = 30

    ruleNames =  [ "program", "statement", "varDeclaration", "valDeclaration", 
                   "assignmentStatement", "forStatement", "ifStatement", 
                   "readStatement", "printStatement", "block", "expression", 
                   "logicalOrExpression", "logicalAndExpression", "equalityExpression", 
                   "relationalExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "membershipExpression", "rangeExpression", 
                   "primaryExpression", "literal", "type", "classDeclaration", 
                   "classBody", "functionDeclaration", "returnStatement", 
                   "parameterList", "parameter", "booleanLiteral", "commentStatement" ]

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 879609302265606) != 0):
                self.state = 62
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(KotlinParser.EOF)
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

        def classDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ClassDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.FunctionDeclarationContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.VarDeclarationContext,0)


        def valDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ValDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(KotlinParser.AssignmentStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReturnStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(KotlinParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(KotlinParser.ForStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(KotlinParser.PrintStatementContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReadStatementContext,0)


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
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.functionDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.varDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.valDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.assignmentStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.ifStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.forStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.printStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 79
                self.readStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 80
                self.commentStatement()
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
        self.enterRule(localctx, 4, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(KotlinParser.VAR)
            self.state = 84
            self.match(KotlinParser.IDENTIFIER)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 85
                self.match(KotlinParser.COLON)
                self.state = 86
                self.type_()


            self.state = 89
            self.match(KotlinParser.EQ)
            self.state = 90
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
        self.enterRule(localctx, 6, self.RULE_valDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(KotlinParser.VAL)
            self.state = 93
            self.match(KotlinParser.IDENTIFIER)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 94
                self.match(KotlinParser.COLON)
                self.state = 95
                self.type_()


            self.state = 98
            self.match(KotlinParser.EQ)
            self.state = 99
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
        self.enterRule(localctx, 8, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(KotlinParser.IDENTIFIER)
            self.state = 102
            self.match(KotlinParser.EQ)
            self.state = 103
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
        self.enterRule(localctx, 10, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(KotlinParser.FOR)
            self.state = 106
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 107
            self.membershipExpression()
            self.state = 108
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 109
            self.block()
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
            self.state = 111
            self.match(KotlinParser.IF)
            self.state = 112
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 115
                self.block()
                pass
            elif token in [1, 2, 8, 9, 10, 11, 13, 15, 45, 48, 49]:
                self.state = 116
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 119
                self.match(KotlinParser.ELSE)
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 120
                    self.block()
                    pass
                elif token in [1, 2, 8, 9, 10, 11, 13, 15, 45, 48, 49]:
                    self.state = 121
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
        self.enterRule(localctx, 14, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 126
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 129
            self.match(KotlinParser.IDENTIFIER)
            self.state = 130
            self.match(KotlinParser.EQ)
            self.state = 131
            self.match(KotlinParser.READLINE)
            self.state = 132
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 133
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
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(KotlinParser.PRINTLN)
            self.state = 136
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 137
            self.expression()
            self.state = 138
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

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.VarDeclarationContext,i)


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.FunctionDeclarationContext,i)


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
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 879609302265606) != 0):
                self.state = 144
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 141
                    self.varDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 142
                    self.functionDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 143
                    self.statement()
                    pass


                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
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
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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
        self.enterRule(localctx, 22, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.logicalAndExpression()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 154
                self.match(KotlinParser.OR)
                self.state = 155
                self.logicalAndExpression()
                self.state = 160
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
        self.enterRule(localctx, 24, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.equalityExpression()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 162
                self.match(KotlinParser.AND)
                self.state = 163
                self.equalityExpression()
                self.state = 168
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
        self.enterRule(localctx, 26, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.relationalExpression()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 170
                    self.match(KotlinParser.EQEQ)
                    self.state = 171
                    self.relationalExpression()
                    pass
                elif token in [34]:
                    self.state = 172
                    self.match(KotlinParser.NEQ)
                    self.state = 173
                    self.relationalExpression()
                    pass
                else:
                    raise NoViableAltException(self)

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
        self.enterRule(localctx, 28, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.additiveExpression()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0):
                self.state = 180
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 515396075520) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
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
        self.enterRule(localctx, 30, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.multiplicativeExpression()
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    _la = self._input.LA(1)
                    if not(_la==27 or _la==28):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.multiplicativeExpression() 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.unaryExpression()
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.unaryExpression() 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_unaryExpression)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(KotlinParser.NOT)
                self.state = 201
                self.primaryExpression()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(KotlinParser.MINUS)
                self.state = 203
                self.primaryExpression()
                pass
            elif token in [6, 7, 21, 45, 46, 47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
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
        self.enterRule(localctx, 36, self.RULE_membershipExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.primaryExpression()
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 208
                self.match(KotlinParser.IN)
                self.state = 209
                self.rangeExpression()
                pass
            elif token in [41]:
                self.state = 210
                self.match(KotlinParser.NOT)
                self.state = 211
                self.match(KotlinParser.IN)
                self.state = 212
                self.rangeExpression()
                pass
            elif token in [-1, 1, 2, 8, 9, 10, 11, 12, 13, 15, 22, 24, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42, 45, 48, 49]:
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
        self.enterRule(localctx, 38, self.RULE_rangeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.additiveExpression()
            self.state = 216
            self.match(KotlinParser.RANGE)
            self.state = 217
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

        def literal(self):
            return self.getTypedRuleContext(KotlinParser.LiteralContext,0)


        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

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
        self.enterRule(localctx, 40, self.RULE_primaryExpression)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(KotlinParser.IDENTIFIER)
                pass
            elif token in [6, 7, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.literal()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 222
                self.expression()
                self.state = 223
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)
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
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(KotlinParser.INT_LITERAL)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(KotlinParser.STRING_LITERAL)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
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
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
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
        self.enterRule(localctx, 46, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(KotlinParser.CLASS)
            self.state = 235
            self.match(KotlinParser.IDENTIFIER)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 236
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 237
                    self.parameterList()


                self.state = 240
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)


            self.state = 243
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 244
            self.classBody()
            self.state = 245
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
        self.enterRule(localctx, 48, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==9:
                self.state = 249
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 247
                    self.varDeclaration()
                    pass
                elif token in [9]:
                    self.state = 248
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 253
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
        self.enterRule(localctx, 50, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(KotlinParser.FUN)
            self.state = 255
            self.match(KotlinParser.IDENTIFIER)
            self.state = 256
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 257
                self.parameterList()


            self.state = 260
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 261
                self.match(KotlinParser.COLON)
                self.state = 262
                self.type_()


            self.state = 265
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
        self.enterRule(localctx, 52, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(KotlinParser.RETURN)
            self.state = 268
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
        self.enterRule(localctx, 54, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.parameter()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 271
                self.match(KotlinParser.COMMA)
                self.state = 272
                self.parameter()
                self.state = 277
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

        def literal(self):
            return self.getTypedRuleContext(KotlinParser.LiteralContext,0)


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
        self.enterRule(localctx, 56, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(KotlinParser.IDENTIFIER)
            self.state = 279
            self.match(KotlinParser.COLON)
            self.state = 280
            self.type_()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 281
                self.match(KotlinParser.EQ)
                self.state = 282
                self.literal()


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
        self.enterRule(localctx, 58, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
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
        self.enterRule(localctx, 60, self.RULE_commentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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





