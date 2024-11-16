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
        4,1,51,217,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,3,2,68,8,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        3,6,102,8,6,1,6,1,6,1,6,3,6,107,8,6,3,6,109,8,6,1,7,3,7,112,8,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,
        129,8,9,10,9,12,9,132,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,145,8,10,1,10,1,10,1,10,5,10,150,8,10,10,10,
        12,10,153,9,10,1,11,1,11,1,11,3,11,158,8,11,1,12,1,12,1,13,1,13,
        1,13,1,13,3,13,166,8,13,1,13,3,13,169,8,13,1,13,1,13,1,13,1,13,1,
        14,1,14,5,14,177,8,14,10,14,12,14,180,9,14,1,15,1,15,1,15,1,15,3,
        15,186,8,15,1,15,1,15,1,15,3,15,191,8,15,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,1,17,5,17,201,8,17,10,17,12,17,204,9,17,1,18,1,18,1,18,
        1,18,1,18,3,18,211,8,18,1,19,1,19,1,20,1,20,1,20,0,1,20,21,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,6,1,0,1,2,
        2,0,28,28,41,41,2,0,27,31,33,40,1,0,3,5,1,0,6,7,1,0,49,50,229,0,
        45,1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,0,6,72,1,0,0,0,8,81,1,0,0,0,10,
        85,1,0,0,0,12,95,1,0,0,0,14,111,1,0,0,0,16,119,1,0,0,0,18,124,1,
        0,0,0,20,144,1,0,0,0,22,157,1,0,0,0,24,159,1,0,0,0,26,161,1,0,0,
        0,28,178,1,0,0,0,30,181,1,0,0,0,32,194,1,0,0,0,34,197,1,0,0,0,36,
        205,1,0,0,0,38,212,1,0,0,0,40,214,1,0,0,0,42,44,3,2,1,0,43,42,1,
        0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,
        45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,62,3,26,13,0,51,62,3,30,
        15,0,52,62,3,4,2,0,53,62,3,6,3,0,54,62,3,8,4,0,55,62,3,32,16,0,56,
        62,3,12,6,0,57,62,3,10,5,0,58,62,3,16,8,0,59,62,3,14,7,0,60,62,3,
        40,20,0,61,50,1,0,0,0,61,51,1,0,0,0,61,52,1,0,0,0,61,53,1,0,0,0,
        61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,
        0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,64,5,1,0,0,64,
        67,5,45,0,0,65,66,5,19,0,0,66,68,3,24,12,0,67,65,1,0,0,0,67,68,1,
        0,0,0,68,69,1,0,0,0,69,70,5,32,0,0,70,71,3,20,10,0,71,5,1,0,0,0,
        72,73,5,2,0,0,73,76,5,45,0,0,74,75,5,19,0,0,75,77,3,24,12,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,5,32,0,0,79,80,3,20,10,
        0,80,7,1,0,0,0,81,82,5,45,0,0,82,83,5,32,0,0,83,84,3,20,10,0,84,
        9,1,0,0,0,85,86,5,13,0,0,86,87,5,21,0,0,87,88,5,45,0,0,88,89,5,14,
        0,0,89,90,3,20,10,0,90,91,5,42,0,0,91,92,3,20,10,0,92,93,5,22,0,
        0,93,94,3,18,9,0,94,11,1,0,0,0,95,96,5,11,0,0,96,97,5,21,0,0,97,
        98,3,20,10,0,98,101,5,22,0,0,99,102,3,18,9,0,100,102,3,2,1,0,101,
        99,1,0,0,0,101,100,1,0,0,0,102,108,1,0,0,0,103,106,5,12,0,0,104,
        107,3,18,9,0,105,107,3,2,1,0,106,104,1,0,0,0,106,105,1,0,0,0,107,
        109,1,0,0,0,108,103,1,0,0,0,108,109,1,0,0,0,109,13,1,0,0,0,110,112,
        7,0,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,
        5,45,0,0,114,115,5,32,0,0,115,116,5,16,0,0,116,117,5,21,0,0,117,
        118,5,22,0,0,118,15,1,0,0,0,119,120,5,15,0,0,120,121,5,21,0,0,121,
        122,3,20,10,0,122,123,5,22,0,0,123,17,1,0,0,0,124,130,5,23,0,0,125,
        129,3,4,2,0,126,129,3,30,15,0,127,129,3,2,1,0,128,125,1,0,0,0,128,
        126,1,0,0,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,
        131,1,0,0,0,131,133,1,0,0,0,132,130,1,0,0,0,133,134,5,24,0,0,134,
        19,1,0,0,0,135,136,6,10,-1,0,136,145,3,22,11,0,137,145,5,45,0,0,
        138,139,7,1,0,0,139,145,3,20,10,3,140,141,5,21,0,0,141,142,3,20,
        10,0,142,143,5,22,0,0,143,145,1,0,0,0,144,135,1,0,0,0,144,137,1,
        0,0,0,144,138,1,0,0,0,144,140,1,0,0,0,145,151,1,0,0,0,146,147,10,
        2,0,0,147,148,7,2,0,0,148,150,3,20,10,3,149,146,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,21,1,0,0,0,153,151,1,
        0,0,0,154,158,5,46,0,0,155,158,5,47,0,0,156,158,3,38,19,0,157,154,
        1,0,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,23,1,0,0,0,159,160,7,
        3,0,0,160,25,1,0,0,0,161,162,5,8,0,0,162,168,5,45,0,0,163,165,5,
        21,0,0,164,166,3,34,17,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,
        1,0,0,0,167,169,5,22,0,0,168,163,1,0,0,0,168,169,1,0,0,0,169,170,
        1,0,0,0,170,171,5,23,0,0,171,172,3,28,14,0,172,173,5,24,0,0,173,
        27,1,0,0,0,174,177,3,4,2,0,175,177,3,30,15,0,176,174,1,0,0,0,176,
        175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        29,1,0,0,0,180,178,1,0,0,0,181,182,5,9,0,0,182,183,5,45,0,0,183,
        185,5,21,0,0,184,186,3,34,17,0,185,184,1,0,0,0,185,186,1,0,0,0,186,
        187,1,0,0,0,187,190,5,22,0,0,188,189,5,19,0,0,189,191,3,24,12,0,
        190,188,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,3,18,9,0,
        193,31,1,0,0,0,194,195,5,10,0,0,195,196,3,20,10,0,196,33,1,0,0,0,
        197,202,3,36,18,0,198,199,5,17,0,0,199,201,3,36,18,0,200,198,1,0,
        0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,35,1,0,0,
        0,204,202,1,0,0,0,205,206,5,45,0,0,206,207,5,19,0,0,207,210,3,24,
        12,0,208,209,5,32,0,0,209,211,3,22,11,0,210,208,1,0,0,0,210,211,
        1,0,0,0,211,37,1,0,0,0,212,213,7,4,0,0,213,39,1,0,0,0,214,215,7,
        5,0,0,215,41,1,0,0,0,21,45,61,67,76,101,106,108,111,128,130,144,
        151,157,165,168,176,178,185,190,202,210
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
                      "STRING_LITERAL", "INTERPOLATION", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

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
    RULE_literal = 11
    RULE_type = 12
    RULE_classDeclaration = 13
    RULE_classBody = 14
    RULE_functionDeclaration = 15
    RULE_returnStatement = 16
    RULE_parameterList = 17
    RULE_parameter = 18
    RULE_booleanLiteral = 19
    RULE_commentStatement = 20

    ruleNames =  [ "program", "statement", "varDeclaration", "valDeclaration", 
                   "assignmentStatement", "forStatement", "ifStatement", 
                   "readStatement", "printStatement", "block", "expression", 
                   "literal", "type", "classDeclaration", "classBody", "functionDeclaration", 
                   "returnStatement", "parameterList", "parameter", "booleanLiteral", 
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
    INTERPOLATION=48
    LINE_COMMENT=49
    BLOCK_COMMENT=50
    WS=51

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
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1724034232397574) != 0):
                self.state = 42
                self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.functionDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.varDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.valDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.assignmentStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.ifStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.forStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 58
                self.printStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 59
                self.readStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 60
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
            self.state = 63
            self.match(KotlinParser.VAR)
            self.state = 64
            self.match(KotlinParser.IDENTIFIER)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 65
                self.match(KotlinParser.COLON)
                self.state = 66
                self.type_()


            self.state = 69
            self.match(KotlinParser.EQ)
            self.state = 70
            self.expression(0)
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
            self.state = 72
            self.match(KotlinParser.VAL)
            self.state = 73
            self.match(KotlinParser.IDENTIFIER)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 74
                self.match(KotlinParser.COLON)
                self.state = 75
                self.type_()


            self.state = 78
            self.match(KotlinParser.EQ)
            self.state = 79
            self.expression(0)
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
            self.state = 81
            self.match(KotlinParser.IDENTIFIER)
            self.state = 82
            self.match(KotlinParser.EQ)
            self.state = 83
            self.expression(0)
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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(KotlinParser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


        def RANGE(self):
            return self.getToken(KotlinParser.RANGE, 0)

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
            self.state = 85
            self.match(KotlinParser.FOR)
            self.state = 86
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 87
            self.match(KotlinParser.IDENTIFIER)
            self.state = 88
            self.match(KotlinParser.IN)
            self.state = 89
            self.expression(0)
            self.state = 90
            self.match(KotlinParser.RANGE)
            self.state = 91
            self.expression(0)
            self.state = 92
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 93
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
            self.state = 95
            self.match(KotlinParser.IF)
            self.state = 96
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 97
            self.expression(0)
            self.state = 98
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 99
                self.block()
                pass
            elif token in [1, 2, 8, 9, 10, 11, 13, 15, 45, 49, 50]:
                self.state = 100
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 103
                self.match(KotlinParser.ELSE)
                self.state = 106
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 104
                    self.block()
                    pass
                elif token in [1, 2, 8, 9, 10, 11, 13, 15, 45, 49, 50]:
                    self.state = 105
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
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 113
            self.match(KotlinParser.IDENTIFIER)
            self.state = 114
            self.match(KotlinParser.EQ)
            self.state = 115
            self.match(KotlinParser.READLINE)
            self.state = 116
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 117
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
            self.state = 119
            self.match(KotlinParser.PRINTLN)
            self.state = 120
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 121
            self.expression(0)
            self.state = 122
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
            self.state = 124
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1724034232397574) != 0):
                self.state = 128
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 125
                    self.varDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 126
                    self.functionDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 127
                    self.statement()
                    pass


                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
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

        def literal(self):
            return self.getTypedRuleContext(KotlinParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


        def NOT(self):
            return self.getToken(KotlinParser.NOT, 0)

        def MINUS(self):
            return self.getToken(KotlinParser.MINUS, 0)

        def LEFT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.LEFT_ROUND_BRACKET, 0)

        def RIGHT_ROUND_BRACKET(self):
            return self.getToken(KotlinParser.RIGHT_ROUND_BRACKET, 0)

        def PLUS(self):
            return self.getToken(KotlinParser.PLUS, 0)

        def MULT(self):
            return self.getToken(KotlinParser.MULT, 0)

        def DIV(self):
            return self.getToken(KotlinParser.DIV, 0)

        def MOD(self):
            return self.getToken(KotlinParser.MOD, 0)

        def EQEQ(self):
            return self.getToken(KotlinParser.EQEQ, 0)

        def NEQ(self):
            return self.getToken(KotlinParser.NEQ, 0)

        def GT(self):
            return self.getToken(KotlinParser.GT, 0)

        def GTE(self):
            return self.getToken(KotlinParser.GTE, 0)

        def LT(self):
            return self.getToken(KotlinParser.LT, 0)

        def LTE(self):
            return self.getToken(KotlinParser.LTE, 0)

        def AND(self):
            return self.getToken(KotlinParser.AND, 0)

        def OR(self):
            return self.getToken(KotlinParser.OR, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KotlinParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 46, 47]:
                self.state = 136
                self.literal()
                pass
            elif token in [45]:
                self.state = 137
                self.match(KotlinParser.IDENTIFIER)
                pass
            elif token in [28, 41]:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==28 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.expression(3)
                pass
            elif token in [21]:
                self.state = 140
                self.match(KotlinParser.LEFT_ROUND_BRACKET)
                self.state = 141
                self.expression(0)
                self.state = 142
                self.match(KotlinParser.RIGHT_ROUND_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 146
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 147
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2194594070528) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 148
                    self.expression(3) 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(KotlinParser.INT_LITERAL)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(KotlinParser.STRING_LITERAL)
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
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
        self.enterRule(localctx, 24, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
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
        self.enterRule(localctx, 26, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(KotlinParser.CLASS)
            self.state = 162
            self.match(KotlinParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
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
            self.match(KotlinParser.LEFT_CURLY_BRACKET)
            self.state = 171
            self.classBody()
            self.state = 172
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
        self.enterRule(localctx, 28, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==9:
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 174
                    self.varDeclaration()
                    pass
                elif token in [9]:
                    self.state = 175
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 180
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
        self.enterRule(localctx, 30, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(KotlinParser.FUN)
            self.state = 182
            self.match(KotlinParser.IDENTIFIER)
            self.state = 183
            self.match(KotlinParser.LEFT_ROUND_BRACKET)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 184
                self.parameterList()


            self.state = 187
            self.match(KotlinParser.RIGHT_ROUND_BRACKET)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 188
                self.match(KotlinParser.COLON)
                self.state = 189
                self.type_()


            self.state = 192
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
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(KotlinParser.RETURN)
            self.state = 195
            self.expression(0)
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
        self.enterRule(localctx, 34, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.parameter()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 198
                self.match(KotlinParser.COMMA)
                self.state = 199
                self.parameter()
                self.state = 204
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
        self.enterRule(localctx, 36, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(KotlinParser.IDENTIFIER)
            self.state = 206
            self.match(KotlinParser.COLON)
            self.state = 207
            self.type_()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 208
                self.match(KotlinParser.EQ)
                self.state = 209
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
        self.enterRule(localctx, 38, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
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
        self.enterRule(localctx, 40, self.RULE_commentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==49 or _la==50):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




