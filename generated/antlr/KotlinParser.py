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
        4,1,31,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,55,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,
        4,72,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,1,6,1,6,1,6,1,6,3,6,
        86,8,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,96,8,7,10,7,12,7,99,9,
        7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,5,9,108,8,9,10,9,12,9,111,9,9,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,122,8,11,1,11,1,11,
        1,11,1,12,1,12,5,12,129,8,12,10,12,12,12,132,9,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,143,8,13,1,13,1,13,1,13,5,13,
        148,8,13,10,13,12,13,151,9,13,1,14,1,14,1,15,1,15,1,15,0,1,26,16,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,3,1,0,20,23,1,0,28,
        30,1,0,24,26,157,0,35,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,56,1,0,
        0,0,8,66,1,0,0,0,10,73,1,0,0,0,12,81,1,0,0,0,14,92,1,0,0,0,16,100,
        1,0,0,0,18,109,1,0,0,0,20,112,1,0,0,0,22,117,1,0,0,0,24,126,1,0,
        0,0,26,142,1,0,0,0,28,152,1,0,0,0,30,154,1,0,0,0,32,34,3,2,1,0,33,
        32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,
        0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,46,3,4,2,0,41,46,3,
        6,3,0,42,46,3,8,4,0,43,46,3,10,5,0,44,46,3,12,6,0,45,40,1,0,0,0,
        45,41,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,
        0,0,47,48,5,1,0,0,48,49,5,2,0,0,49,50,3,26,13,0,50,51,5,3,0,0,51,
        54,3,24,12,0,52,53,5,4,0,0,53,55,3,24,12,0,54,52,1,0,0,0,54,55,1,
        0,0,0,55,5,1,0,0,0,56,57,5,5,0,0,57,58,5,2,0,0,58,59,5,27,0,0,59,
        60,5,6,0,0,60,61,3,26,13,0,61,62,5,7,0,0,62,63,3,26,13,0,63,64,5,
        3,0,0,64,65,3,24,12,0,65,7,1,0,0,0,66,67,5,8,0,0,67,68,5,2,0,0,68,
        69,3,26,13,0,69,71,5,3,0,0,70,72,5,9,0,0,71,70,1,0,0,0,71,72,1,0,
        0,0,72,9,1,0,0,0,73,74,5,27,0,0,74,75,5,10,0,0,75,76,5,11,0,0,76,
        77,5,2,0,0,77,79,5,3,0,0,78,80,5,9,0,0,79,78,1,0,0,0,79,80,1,0,0,
        0,80,11,1,0,0,0,81,82,5,12,0,0,82,83,5,27,0,0,83,85,5,2,0,0,84,86,
        3,14,7,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,3,0,0,
        88,89,5,13,0,0,89,90,3,18,9,0,90,91,5,14,0,0,91,13,1,0,0,0,92,97,
        3,16,8,0,93,94,5,15,0,0,94,96,3,16,8,0,95,93,1,0,0,0,96,99,1,0,0,
        0,97,95,1,0,0,0,97,98,1,0,0,0,98,15,1,0,0,0,99,97,1,0,0,0,100,101,
        5,16,0,0,101,102,5,27,0,0,102,103,5,17,0,0,103,104,3,30,15,0,104,
        17,1,0,0,0,105,108,3,20,10,0,106,108,3,22,11,0,107,105,1,0,0,0,107,
        106,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        19,1,0,0,0,111,109,1,0,0,0,112,113,5,18,0,0,113,114,5,27,0,0,114,
        115,5,17,0,0,115,116,3,30,15,0,116,21,1,0,0,0,117,118,5,19,0,0,118,
        119,5,27,0,0,119,121,5,2,0,0,120,122,3,14,7,0,121,120,1,0,0,0,121,
        122,1,0,0,0,122,123,1,0,0,0,123,124,5,3,0,0,124,125,3,24,12,0,125,
        23,1,0,0,0,126,130,5,13,0,0,127,129,3,2,1,0,128,127,1,0,0,0,129,
        132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,
        130,1,0,0,0,133,134,5,14,0,0,134,25,1,0,0,0,135,136,6,13,-1,0,136,
        143,3,28,14,0,137,143,5,27,0,0,138,139,5,2,0,0,139,140,3,26,13,0,
        140,141,5,3,0,0,141,143,1,0,0,0,142,135,1,0,0,0,142,137,1,0,0,0,
        142,138,1,0,0,0,143,149,1,0,0,0,144,145,10,2,0,0,145,146,7,0,0,0,
        146,148,3,26,13,3,147,144,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,
        0,149,150,1,0,0,0,150,27,1,0,0,0,151,149,1,0,0,0,152,153,7,1,0,0,
        153,29,1,0,0,0,154,155,7,2,0,0,155,31,1,0,0,0,13,35,45,54,71,79,
        85,97,107,109,121,130,142,149
    ]

class KotlinParser ( Parser ):

    grammarFileName = "Kotlin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'else'", "'for'", 
                     "'in'", "'..'", "'println'", "';'", "'='", "'readline'", 
                     "'class'", "'{'", "'}'", "','", "'val'", "':'", "'var'", 
                     "'fun'", "'+'", "'-'", "'*'", "'/'", "'Int'", "'Boolean'", 
                     "'String'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_ifStatement = 2
    RULE_forStatement = 3
    RULE_printStatement = 4
    RULE_readStatement = 5
    RULE_classDeclaration = 6
    RULE_parameterList = 7
    RULE_parameter = 8
    RULE_classBody = 9
    RULE_varDeclaration = 10
    RULE_functionDeclaration = 11
    RULE_block = 12
    RULE_expression = 13
    RULE_literal = 14
    RULE_type = 15

    ruleNames =  [ "program", "statement", "ifStatement", "forStatement", 
                   "printStatement", "readStatement", "classDeclaration", 
                   "parameterList", "parameter", "classBody", "varDeclaration", 
                   "functionDeclaration", "block", "expression", "literal", 
                   "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    IDENTIFIER=27
    INT_LITERAL=28
    BOOLEAN_LITERAL=29
    STRING_LITERAL=30
    WS=31

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134222114) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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

        def ifStatement(self):
            return self.getTypedRuleContext(KotlinParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(KotlinParser.ForStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(KotlinParser.PrintStatementContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReadStatementContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ClassDeclarationContext,0)


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
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.ifStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.forStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.printStatement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.readStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.classDeclaration()
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

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.BlockContext)
            else:
                return self.getTypedRuleContext(KotlinParser.BlockContext,i)


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
        self.enterRule(localctx, 4, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(KotlinParser.T__0)
            self.state = 48
            self.match(KotlinParser.T__1)
            self.state = 49
            self.expression(0)
            self.state = 50
            self.match(KotlinParser.T__2)
            self.state = 51
            self.block()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 52
                self.match(KotlinParser.T__3)
                self.state = 53
                self.block()


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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


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
        self.enterRule(localctx, 6, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(KotlinParser.T__4)
            self.state = 57
            self.match(KotlinParser.T__1)
            self.state = 58
            self.match(KotlinParser.IDENTIFIER)
            self.state = 59
            self.match(KotlinParser.T__5)
            self.state = 60
            self.expression(0)
            self.state = 61
            self.match(KotlinParser.T__6)
            self.state = 62
            self.expression(0)
            self.state = 63
            self.match(KotlinParser.T__2)
            self.state = 64
            self.block()
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

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(KotlinParser.T__7)
            self.state = 67
            self.match(KotlinParser.T__1)
            self.state = 68
            self.expression(0)
            self.state = 69
            self.match(KotlinParser.T__2)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 70
                self.match(KotlinParser.T__8)


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
        self.enterRule(localctx, 10, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(KotlinParser.IDENTIFIER)
            self.state = 74
            self.match(KotlinParser.T__9)
            self.state = 75
            self.match(KotlinParser.T__10)
            self.state = 76
            self.match(KotlinParser.T__1)
            self.state = 77
            self.match(KotlinParser.T__2)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 78
                self.match(KotlinParser.T__8)


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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def classBody(self):
            return self.getTypedRuleContext(KotlinParser.ClassBodyContext,0)


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
        self.enterRule(localctx, 12, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(KotlinParser.T__11)
            self.state = 82
            self.match(KotlinParser.IDENTIFIER)
            self.state = 83
            self.match(KotlinParser.T__1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 84
                self.parameterList()


            self.state = 87
            self.match(KotlinParser.T__2)
            self.state = 88
            self.match(KotlinParser.T__12)
            self.state = 89
            self.classBody()
            self.state = 90
            self.match(KotlinParser.T__13)
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
        self.enterRule(localctx, 14, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.parameter()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 93
                self.match(KotlinParser.T__14)
                self.state = 94
                self.parameter()
                self.state = 99
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

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


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
        self.enterRule(localctx, 16, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(KotlinParser.T__15)
            self.state = 101
            self.match(KotlinParser.IDENTIFIER)
            self.state = 102
            self.match(KotlinParser.T__16)
            self.state = 103
            self.type_()
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
        self.enterRule(localctx, 18, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 107
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 105
                    self.varDeclaration()
                    pass
                elif token in [19]:
                    self.state = 106
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 20, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(KotlinParser.T__17)
            self.state = 113
            self.match(KotlinParser.IDENTIFIER)
            self.state = 114
            self.match(KotlinParser.T__16)
            self.state = 115
            self.type_()
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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(KotlinParser.ParameterListContext,0)


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
            self.state = 117
            self.match(KotlinParser.T__18)
            self.state = 118
            self.match(KotlinParser.IDENTIFIER)
            self.state = 119
            self.match(KotlinParser.T__1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 120
                self.parameterList()


            self.state = 123
            self.match(KotlinParser.T__2)
            self.state = 124
            self.block()
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
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(KotlinParser.T__12)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134222114) != 0):
                self.state = 127
                self.statement()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(KotlinParser.T__13)
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30]:
                self.state = 136
                self.literal()
                pass
            elif token in [27]:
                self.state = 137
                self.match(KotlinParser.IDENTIFIER)
                pass
            elif token in [2]:
                self.state = 138
                self.match(KotlinParser.T__1)
                self.state = 139
                self.expression(0)
                self.state = 140
                self.match(KotlinParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 144
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 145
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 146
                    self.expression(3) 
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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

        def BOOLEAN_LITERAL(self):
            return self.getToken(KotlinParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(KotlinParser.STRING_LITERAL, 0)

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
        self.enterRule(localctx, 28, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
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
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




