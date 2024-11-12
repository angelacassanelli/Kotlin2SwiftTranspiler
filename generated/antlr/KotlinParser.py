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
        4,1,32,196,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,3,2,
        56,8,2,1,2,1,2,3,2,60,8,2,1,2,3,2,63,8,2,1,3,1,3,1,3,1,3,3,3,69,
        8,3,1,3,1,3,3,3,73,8,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,90,8,4,10,4,12,4,93,9,4,1,4,1,4,3,4,97,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        3,6,114,8,6,1,7,3,7,117,8,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,125,8,7,
        1,8,1,8,1,8,5,8,130,8,8,10,8,12,8,133,9,8,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,3,10,143,8,10,1,10,1,10,1,10,1,11,1,11,5,11,150,8,11,
        10,11,12,11,153,9,11,1,12,1,12,1,12,1,12,3,12,159,8,12,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,5,13,168,8,13,10,13,12,13,171,9,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,182,8,14,1,14,1,14,
        1,14,5,14,187,8,14,10,14,12,14,190,9,14,1,15,1,15,1,16,1,16,1,16,
        0,1,28,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,4,2,0,
        1,1,5,5,1,0,20,24,1,0,29,31,1,0,25,27,205,0,37,1,0,0,0,2,49,1,0,
        0,0,4,51,1,0,0,0,6,64,1,0,0,0,8,77,1,0,0,0,10,98,1,0,0,0,12,108,
        1,0,0,0,14,116,1,0,0,0,16,126,1,0,0,0,18,134,1,0,0,0,20,138,1,0,
        0,0,22,151,1,0,0,0,24,154,1,0,0,0,26,165,1,0,0,0,28,181,1,0,0,0,
        30,191,1,0,0,0,32,193,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,
        40,41,5,0,0,1,41,1,1,0,0,0,42,50,3,4,2,0,43,50,3,6,3,0,44,50,3,8,
        4,0,45,50,3,10,5,0,46,50,3,12,6,0,47,50,3,14,7,0,48,50,3,24,12,0,
        49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,1,
        0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,52,5,1,0,0,52,
        55,5,28,0,0,53,54,5,2,0,0,54,56,3,32,16,0,55,53,1,0,0,0,55,56,1,
        0,0,0,56,59,1,0,0,0,57,58,5,3,0,0,58,60,3,28,14,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,62,1,0,0,0,61,63,5,4,0,0,62,61,1,0,0,0,62,63,1,
        0,0,0,63,5,1,0,0,0,64,65,5,5,0,0,65,68,5,28,0,0,66,67,5,2,0,0,67,
        69,3,32,16,0,68,66,1,0,0,0,68,69,1,0,0,0,69,72,1,0,0,0,70,71,5,3,
        0,0,71,73,3,28,14,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,
        76,5,4,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,7,1,0,0,0,77,78,5,6,0,
        0,78,79,5,7,0,0,79,80,3,28,14,0,80,81,5,8,0,0,81,91,3,26,13,0,82,
        83,5,9,0,0,83,84,5,6,0,0,84,85,5,7,0,0,85,86,3,28,14,0,86,87,5,8,
        0,0,87,88,3,26,13,0,88,90,1,0,0,0,89,82,1,0,0,0,90,93,1,0,0,0,91,
        89,1,0,0,0,91,92,1,0,0,0,92,96,1,0,0,0,93,91,1,0,0,0,94,95,5,9,0,
        0,95,97,3,26,13,0,96,94,1,0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,99,
        5,10,0,0,99,100,5,7,0,0,100,101,5,28,0,0,101,102,5,11,0,0,102,103,
        3,28,14,0,103,104,5,12,0,0,104,105,3,28,14,0,105,106,5,8,0,0,106,
        107,3,26,13,0,107,11,1,0,0,0,108,109,5,13,0,0,109,110,5,7,0,0,110,
        111,3,28,14,0,111,113,5,8,0,0,112,114,5,4,0,0,113,112,1,0,0,0,113,
        114,1,0,0,0,114,13,1,0,0,0,115,117,7,0,0,0,116,115,1,0,0,0,116,117,
        1,0,0,0,117,118,1,0,0,0,118,119,5,28,0,0,119,120,5,3,0,0,120,121,
        5,14,0,0,121,122,5,7,0,0,122,124,5,8,0,0,123,125,5,4,0,0,124,123,
        1,0,0,0,124,125,1,0,0,0,125,15,1,0,0,0,126,131,3,18,9,0,127,128,
        5,15,0,0,128,130,3,18,9,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,17,1,0,0,0,133,131,1,0,0,0,134,135,5,
        28,0,0,135,136,5,2,0,0,136,137,3,32,16,0,137,19,1,0,0,0,138,139,
        5,16,0,0,139,140,5,28,0,0,140,142,5,7,0,0,141,143,3,16,8,0,142,141,
        1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,5,8,0,0,145,146,
        3,26,13,0,146,21,1,0,0,0,147,150,3,4,2,0,148,150,3,20,10,0,149,147,
        1,0,0,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,
        1,0,0,0,152,23,1,0,0,0,153,151,1,0,0,0,154,155,5,17,0,0,155,156,
        5,28,0,0,156,158,5,7,0,0,157,159,3,16,8,0,158,157,1,0,0,0,158,159,
        1,0,0,0,159,160,1,0,0,0,160,161,5,8,0,0,161,162,5,18,0,0,162,163,
        3,22,11,0,163,164,5,19,0,0,164,25,1,0,0,0,165,169,5,18,0,0,166,168,
        3,2,1,0,167,166,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,
        1,0,0,0,170,172,1,0,0,0,171,169,1,0,0,0,172,173,5,19,0,0,173,27,
        1,0,0,0,174,175,6,14,-1,0,175,182,3,30,15,0,176,182,5,28,0,0,177,
        178,5,7,0,0,178,179,3,28,14,0,179,180,5,8,0,0,180,182,1,0,0,0,181,
        174,1,0,0,0,181,176,1,0,0,0,181,177,1,0,0,0,182,188,1,0,0,0,183,
        184,10,2,0,0,184,185,7,1,0,0,185,187,3,28,14,3,186,183,1,0,0,0,187,
        190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,29,1,0,0,0,190,188,
        1,0,0,0,191,192,7,2,0,0,192,31,1,0,0,0,193,194,7,3,0,0,194,33,1,
        0,0,0,21,37,49,55,59,62,68,72,75,91,96,113,116,124,131,142,149,151,
        158,169,181,188
    ]

class KotlinParser ( Parser ):

    grammarFileName = "Kotlin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "':'", "'='", "';'", "'val'", 
                     "'if'", "'('", "')'", "'else'", "'for'", "'in'", "'..'", 
                     "'println'", "'readLine'", "','", "'fun'", "'class'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'=='", "'Int'", 
                     "'Boolean'", "'String'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "INT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_valDeclaration = 3
    RULE_ifStatement = 4
    RULE_forStatement = 5
    RULE_printStatement = 6
    RULE_readStatement = 7
    RULE_parameterList = 8
    RULE_parameter = 9
    RULE_functionDeclaration = 10
    RULE_classBody = 11
    RULE_classDeclaration = 12
    RULE_block = 13
    RULE_expression = 14
    RULE_literal = 15
    RULE_type = 16

    ruleNames =  [ "program", "statement", "varDeclaration", "valDeclaration", 
                   "ifStatement", "forStatement", "printStatement", "readStatement", 
                   "parameterList", "parameter", "functionDeclaration", 
                   "classBody", "classDeclaration", "block", "expression", 
                   "literal", "type" ]

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
    T__26=27
    IDENTIFIER=28
    INT_LITERAL=29
    BOOLEAN_LITERAL=30
    STRING_LITERAL=31
    WS=32

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268575842) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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

        def varDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.VarDeclarationContext,0)


        def valDeclaration(self):
            return self.getTypedRuleContext(KotlinParser.ValDeclarationContext,0)


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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.varDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.valDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.printStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.readStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.classDeclaration()
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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


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
            self.state = 51
            self.match(KotlinParser.T__0)
            self.state = 52
            self.match(KotlinParser.IDENTIFIER)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 53
                self.match(KotlinParser.T__1)
                self.state = 54
                self.type_()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 57
                self.match(KotlinParser.T__2)
                self.state = 58
                self.expression(0)


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 61
                self.match(KotlinParser.T__3)


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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


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
            self.state = 64
            self.match(KotlinParser.T__4)
            self.state = 65
            self.match(KotlinParser.IDENTIFIER)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 66
                self.match(KotlinParser.T__1)
                self.state = 67
                self.type_()


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 70
                self.match(KotlinParser.T__2)
                self.state = 71
                self.expression(0)


            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 74
                self.match(KotlinParser.T__3)


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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


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
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(KotlinParser.T__5)
            self.state = 78
            self.match(KotlinParser.T__6)
            self.state = 79
            self.expression(0)
            self.state = 80
            self.match(KotlinParser.T__7)
            self.state = 81
            self.block()
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.match(KotlinParser.T__8)
                    self.state = 83
                    self.match(KotlinParser.T__5)
                    self.state = 84
                    self.match(KotlinParser.T__6)
                    self.state = 85
                    self.expression(0)
                    self.state = 86
                    self.match(KotlinParser.T__7)
                    self.state = 87
                    self.block() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 94
                self.match(KotlinParser.T__8)
                self.state = 95
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
        self.enterRule(localctx, 10, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(KotlinParser.T__9)
            self.state = 99
            self.match(KotlinParser.T__6)
            self.state = 100
            self.match(KotlinParser.IDENTIFIER)
            self.state = 101
            self.match(KotlinParser.T__10)
            self.state = 102
            self.expression(0)
            self.state = 103
            self.match(KotlinParser.T__11)
            self.state = 104
            self.expression(0)
            self.state = 105
            self.match(KotlinParser.T__7)
            self.state = 106
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
        self.enterRule(localctx, 12, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(KotlinParser.T__12)
            self.state = 109
            self.match(KotlinParser.T__6)
            self.state = 110
            self.expression(0)
            self.state = 111
            self.match(KotlinParser.T__7)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 112
                self.match(KotlinParser.T__3)


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
        self.enterRule(localctx, 14, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==5:
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==1 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 118
            self.match(KotlinParser.IDENTIFIER)
            self.state = 119
            self.match(KotlinParser.T__2)
            self.state = 120
            self.match(KotlinParser.T__13)
            self.state = 121
            self.match(KotlinParser.T__6)
            self.state = 122
            self.match(KotlinParser.T__7)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 123
                self.match(KotlinParser.T__3)


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
        self.enterRule(localctx, 16, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.parameter()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 127
                self.match(KotlinParser.T__14)
                self.state = 128
                self.parameter()
                self.state = 133
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
        self.enterRule(localctx, 18, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(KotlinParser.IDENTIFIER)
            self.state = 135
            self.match(KotlinParser.T__1)
            self.state = 136
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
        self.enterRule(localctx, 20, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(KotlinParser.T__15)
            self.state = 139
            self.match(KotlinParser.IDENTIFIER)
            self.state = 140
            self.match(KotlinParser.T__6)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 141
                self.parameterList()


            self.state = 144
            self.match(KotlinParser.T__7)
            self.state = 145
            self.block()
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
        self.enterRule(localctx, 22, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==16:
                self.state = 149
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 147
                    self.varDeclaration()
                    pass
                elif token in [16]:
                    self.state = 148
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 24, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(KotlinParser.T__16)
            self.state = 155
            self.match(KotlinParser.IDENTIFIER)
            self.state = 156
            self.match(KotlinParser.T__6)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 157
                self.parameterList()


            self.state = 160
            self.match(KotlinParser.T__7)
            self.state = 161
            self.match(KotlinParser.T__17)
            self.state = 162
            self.classBody()
            self.state = 163
            self.match(KotlinParser.T__18)
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
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(KotlinParser.T__17)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268575842) != 0):
                self.state = 166
                self.statement()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(KotlinParser.T__18)
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31]:
                self.state = 175
                self.literal()
                pass
            elif token in [28]:
                self.state = 176
                self.match(KotlinParser.IDENTIFIER)
                pass
            elif token in [7]:
                self.state = 177
                self.match(KotlinParser.T__6)
                self.state = 178
                self.expression(0)
                self.state = 179
                self.match(KotlinParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 183
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 184
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 185
                    self.expression(3) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
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
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




