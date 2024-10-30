# Generated from antlr/Kotlin.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KotlinParser import KotlinParser
else:
    from KotlinParser import KotlinParser

# This class defines a complete listener for a parse tree produced by KotlinParser.
class KotlinListener(ParseTreeListener):

    # Enter a parse tree produced by KotlinParser#program.
    def enterProgram(self, ctx:KotlinParser.ProgramContext):
        pass

    # Exit a parse tree produced by KotlinParser#program.
    def exitProgram(self, ctx:KotlinParser.ProgramContext):
        pass


    # Enter a parse tree produced by KotlinParser#statement.
    def enterStatement(self, ctx:KotlinParser.StatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#statement.
    def exitStatement(self, ctx:KotlinParser.StatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#ifStatement.
    def enterIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#ifStatement.
    def exitIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#forStatement.
    def enterForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#forStatement.
    def exitForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#printStatement.
    def enterPrintStatement(self, ctx:KotlinParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#printStatement.
    def exitPrintStatement(self, ctx:KotlinParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#readStatement.
    def enterReadStatement(self, ctx:KotlinParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#readStatement.
    def exitReadStatement(self, ctx:KotlinParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#classDeclaration.
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#classDeclaration.
    def exitClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#parameterList.
    def enterParameterList(self, ctx:KotlinParser.ParameterListContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameterList.
    def exitParameterList(self, ctx:KotlinParser.ParameterListContext):
        pass


    # Enter a parse tree produced by KotlinParser#parameter.
    def enterParameter(self, ctx:KotlinParser.ParameterContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameter.
    def exitParameter(self, ctx:KotlinParser.ParameterContext):
        pass


    # Enter a parse tree produced by KotlinParser#classBody.
    def enterClassBody(self, ctx:KotlinParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by KotlinParser#classBody.
    def exitClassBody(self, ctx:KotlinParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by KotlinParser#varDeclaration.
    def enterVarDeclaration(self, ctx:KotlinParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#varDeclaration.
    def exitVarDeclaration(self, ctx:KotlinParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#block.
    def enterBlock(self, ctx:KotlinParser.BlockContext):
        pass

    # Exit a parse tree produced by KotlinParser#block.
    def exitBlock(self, ctx:KotlinParser.BlockContext):
        pass


    # Enter a parse tree produced by KotlinParser#expression.
    def enterExpression(self, ctx:KotlinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#expression.
    def exitExpression(self, ctx:KotlinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#literal.
    def enterLiteral(self, ctx:KotlinParser.LiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#literal.
    def exitLiteral(self, ctx:KotlinParser.LiteralContext):
        pass


    # Enter a parse tree produced by KotlinParser#type.
    def enterType(self, ctx:KotlinParser.TypeContext):
        pass

    # Exit a parse tree produced by KotlinParser#type.
    def exitType(self, ctx:KotlinParser.TypeContext):
        pass



del KotlinParser