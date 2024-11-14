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
        4,1,36,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,57,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,66,8,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,3,4,75,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,91,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,9,3,9,109,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,5,10,120,8,10,10,10,12,10,123,9,10,1,11,1,11,1,11,1,
        11,1,11,3,11,130,8,11,1,12,1,12,1,12,1,12,3,12,136,8,12,1,12,1,12,
        1,12,3,12,141,8,12,1,12,1,12,1,13,1,13,5,13,147,8,13,10,13,12,13,
        150,9,13,1,14,1,14,1,14,1,14,3,14,156,8,14,1,14,1,14,1,14,1,14,1,
        14,1,15,1,15,1,15,5,15,166,8,15,10,15,12,15,169,9,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,180,8,16,1,16,1,16,1,16,5,
        16,185,8,16,10,16,12,16,188,9,16,1,17,1,17,1,18,1,18,1,18,0,1,32,
        19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,4,2,0,2,
        2,5,5,1,0,20,28,1,0,33,35,1,0,29,31,200,0,41,1,0,0,0,2,56,1,0,0,
        0,4,58,1,0,0,0,6,61,1,0,0,0,8,70,1,0,0,0,10,79,1,0,0,0,12,83,1,0,
        0,0,14,92,1,0,0,0,16,102,1,0,0,0,18,108,1,0,0,0,20,116,1,0,0,0,22,
        124,1,0,0,0,24,131,1,0,0,0,26,148,1,0,0,0,28,151,1,0,0,0,30,162,
        1,0,0,0,32,179,1,0,0,0,34,189,1,0,0,0,36,191,1,0,0,0,38,40,3,2,1,
        0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,
        1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,57,3,28,14,0,
        47,57,3,24,12,0,48,57,3,6,3,0,49,57,3,8,4,0,50,57,3,10,5,0,51,57,
        3,4,2,0,52,57,3,12,6,0,53,57,3,14,7,0,54,57,3,16,8,0,55,57,3,18,
        9,0,56,46,1,0,0,0,56,47,1,0,0,0,56,48,1,0,0,0,56,49,1,0,0,0,56,50,
        1,0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,
        56,55,1,0,0,0,57,3,1,0,0,0,58,59,5,1,0,0,59,60,3,32,16,0,60,5,1,
        0,0,0,61,62,5,2,0,0,62,65,5,32,0,0,63,64,5,3,0,0,64,66,3,36,18,0,
        65,63,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,4,0,0,68,69,3,
        32,16,0,69,7,1,0,0,0,70,71,5,5,0,0,71,74,5,32,0,0,72,73,5,3,0,0,
        73,75,3,36,18,0,74,72,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,
        5,4,0,0,77,78,3,32,16,0,78,9,1,0,0,0,79,80,5,32,0,0,80,81,5,4,0,
        0,81,82,3,32,16,0,82,11,1,0,0,0,83,84,5,6,0,0,84,85,5,7,0,0,85,86,
        3,32,16,0,86,87,5,8,0,0,87,90,3,30,15,0,88,89,5,9,0,0,89,91,3,30,
        15,0,90,88,1,0,0,0,90,91,1,0,0,0,91,13,1,0,0,0,92,93,5,10,0,0,93,
        94,5,7,0,0,94,95,5,32,0,0,95,96,5,11,0,0,96,97,3,32,16,0,97,98,5,
        12,0,0,98,99,3,32,16,0,99,100,5,8,0,0,100,101,3,30,15,0,101,15,1,
        0,0,0,102,103,5,13,0,0,103,104,5,7,0,0,104,105,3,32,16,0,105,106,
        5,8,0,0,106,17,1,0,0,0,107,109,7,0,0,0,108,107,1,0,0,0,108,109,1,
        0,0,0,109,110,1,0,0,0,110,111,5,32,0,0,111,112,5,4,0,0,112,113,5,
        14,0,0,113,114,5,7,0,0,114,115,5,8,0,0,115,19,1,0,0,0,116,121,3,
        22,11,0,117,118,5,15,0,0,118,120,3,22,11,0,119,117,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,121,1,
        0,0,0,124,125,5,32,0,0,125,126,5,3,0,0,126,129,3,36,18,0,127,128,
        5,4,0,0,128,130,3,34,17,0,129,127,1,0,0,0,129,130,1,0,0,0,130,23,
        1,0,0,0,131,132,5,16,0,0,132,133,5,32,0,0,133,135,5,7,0,0,134,136,
        3,20,10,0,135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,140,
        5,8,0,0,138,139,5,3,0,0,139,141,3,36,18,0,140,138,1,0,0,0,140,141,
        1,0,0,0,141,142,1,0,0,0,142,143,3,30,15,0,143,25,1,0,0,0,144,147,
        3,6,3,0,145,147,3,24,12,0,146,144,1,0,0,0,146,145,1,0,0,0,147,150,
        1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,27,1,0,0,0,150,148,1,
        0,0,0,151,152,5,17,0,0,152,153,5,32,0,0,153,155,5,7,0,0,154,156,
        3,20,10,0,155,154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,
        5,8,0,0,158,159,5,18,0,0,159,160,3,26,13,0,160,161,5,19,0,0,161,
        29,1,0,0,0,162,167,5,18,0,0,163,166,3,2,1,0,164,166,3,24,12,0,165,
        163,1,0,0,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,
        168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,5,19,0,0,171,
        31,1,0,0,0,172,173,6,16,-1,0,173,180,3,34,17,0,174,180,5,32,0,0,
        175,176,5,7,0,0,176,177,3,32,16,0,177,178,5,8,0,0,178,180,1,0,0,
        0,179,172,1,0,0,0,179,174,1,0,0,0,179,175,1,0,0,0,180,186,1,0,0,
        0,181,182,10,2,0,0,182,183,7,1,0,0,183,185,3,32,16,3,184,181,1,0,
        0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,33,1,0,0,
        0,188,186,1,0,0,0,189,190,7,2,0,0,190,35,1,0,0,0,191,192,7,3,0,0,
        192,37,1,0,0,0,17,41,56,65,74,90,108,121,129,135,140,146,148,155,
        165,167,179,186
    ]

class KotlinParser ( Parser ):

    grammarFileName = "Kotlin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'var'", "':'", "'='", "'val'", 
                     "'if'", "'('", "')'", "'else'", "'for'", "'in'", "'..'", 
                     "'println'", "'readLine'", "','", "'fun'", "'class'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'=='", "'>'", 
                     "'>='", "'<'", "'<='", "'Int'", "'Boolean'", "'String'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_returnStatement = 2
    RULE_varDeclaration = 3
    RULE_valDeclaration = 4
    RULE_assignmentStatement = 5
    RULE_ifStatement = 6
    RULE_forStatement = 7
    RULE_printStatement = 8
    RULE_readStatement = 9
    RULE_parameterList = 10
    RULE_parameter = 11
    RULE_functionDeclaration = 12
    RULE_classBody = 13
    RULE_classDeclaration = 14
    RULE_block = 15
    RULE_expression = 16
    RULE_literal = 17
    RULE_type = 18

    ruleNames =  [ "program", "statement", "returnStatement", "varDeclaration", 
                   "valDeclaration", "assignmentStatement", "ifStatement", 
                   "forStatement", "printStatement", "readStatement", "parameterList", 
                   "parameter", "functionDeclaration", "classBody", "classDeclaration", 
                   "block", "expression", "literal", "type" ]

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
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    IDENTIFIER=32
    INT_LITERAL=33
    BOOLEAN_LITERAL=34
    STRING_LITERAL=35
    WS=36

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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4295173222) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.functionDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.varDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.valDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.assignmentStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.ifStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.forStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.printStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 55
                self.readStatement()
                pass


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
        self.enterRule(localctx, 4, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(KotlinParser.T__0)
            self.state = 59
            self.expression(0)
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

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


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
            self.state = 61
            self.match(KotlinParser.T__1)
            self.state = 62
            self.match(KotlinParser.IDENTIFIER)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 63
                self.match(KotlinParser.T__2)
                self.state = 64
                self.type_()


            self.state = 67
            self.match(KotlinParser.T__3)
            self.state = 68
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

        def IDENTIFIER(self):
            return self.getToken(KotlinParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


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
            self.state = 70
            self.match(KotlinParser.T__4)
            self.state = 71
            self.match(KotlinParser.IDENTIFIER)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 72
                self.match(KotlinParser.T__2)
                self.state = 73
                self.type_()


            self.state = 76
            self.match(KotlinParser.T__3)
            self.state = 77
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
            self.state = 79
            self.match(KotlinParser.IDENTIFIER)
            self.state = 80
            self.match(KotlinParser.T__3)
            self.state = 81
            self.expression(0)
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
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
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
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 88
                self.match(KotlinParser.T__8)
                self.state = 89
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
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(KotlinParser.T__9)
            self.state = 93
            self.match(KotlinParser.T__6)
            self.state = 94
            self.match(KotlinParser.IDENTIFIER)
            self.state = 95
            self.match(KotlinParser.T__10)
            self.state = 96
            self.expression(0)
            self.state = 97
            self.match(KotlinParser.T__11)
            self.state = 98
            self.expression(0)
            self.state = 99
            self.match(KotlinParser.T__7)
            self.state = 100
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
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(KotlinParser.T__12)
            self.state = 103
            self.match(KotlinParser.T__6)
            self.state = 104
            self.expression(0)
            self.state = 105
            self.match(KotlinParser.T__7)
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
        self.enterRule(localctx, 18, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==5:
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==2 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 110
            self.match(KotlinParser.IDENTIFIER)
            self.state = 111
            self.match(KotlinParser.T__3)
            self.state = 112
            self.match(KotlinParser.T__13)
            self.state = 113
            self.match(KotlinParser.T__6)
            self.state = 114
            self.match(KotlinParser.T__7)
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
        self.enterRule(localctx, 20, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.parameter()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 117
                self.match(KotlinParser.T__14)
                self.state = 118
                self.parameter()
                self.state = 123
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
        self.enterRule(localctx, 22, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(KotlinParser.IDENTIFIER)
            self.state = 125
            self.match(KotlinParser.T__2)
            self.state = 126
            self.type_()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 127
                self.match(KotlinParser.T__3)
                self.state = 128
                self.literal()


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
        self.enterRule(localctx, 24, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(KotlinParser.T__15)
            self.state = 132
            self.match(KotlinParser.IDENTIFIER)
            self.state = 133
            self.match(KotlinParser.T__6)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 134
                self.parameterList()


            self.state = 137
            self.match(KotlinParser.T__7)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 138
                self.match(KotlinParser.T__2)
                self.state = 139
                self.type_()


            self.state = 142
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
        self.enterRule(localctx, 26, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==16:
                self.state = 146
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 144
                    self.varDeclaration()
                    pass
                elif token in [16]:
                    self.state = 145
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 150
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
        self.enterRule(localctx, 28, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(KotlinParser.T__16)
            self.state = 152
            self.match(KotlinParser.IDENTIFIER)
            self.state = 153
            self.match(KotlinParser.T__6)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 154
                self.parameterList()


            self.state = 157
            self.match(KotlinParser.T__7)
            self.state = 158
            self.match(KotlinParser.T__17)
            self.state = 159
            self.classBody()
            self.state = 160
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


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(KotlinParser.FunctionDeclarationContext,i)


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
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(KotlinParser.T__17)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4295173222) != 0):
                self.state = 165
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 163
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 164
                    self.functionDeclaration()
                    pass


                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35]:
                self.state = 173
                self.literal()
                pass
            elif token in [32]:
                self.state = 174
                self.match(KotlinParser.IDENTIFIER)
                pass
            elif token in [7]:
                self.state = 175
                self.match(KotlinParser.T__6)
                self.state = 176
                self.expression(0)
                self.state = 177
                self.match(KotlinParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 535822336) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 183
                    self.expression(3) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_type)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




