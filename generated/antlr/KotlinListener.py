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


    # Enter a parse tree produced by KotlinParser#varDeclaration.
    def enterVarDeclaration(self, ctx:KotlinParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#varDeclaration.
    def exitVarDeclaration(self, ctx:KotlinParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#valDeclaration.
    def enterValDeclaration(self, ctx:KotlinParser.ValDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#valDeclaration.
    def exitValDeclaration(self, ctx:KotlinParser.ValDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:KotlinParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:KotlinParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#forStatement.
    def enterForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#forStatement.
    def exitForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#ifStatement.
    def enterIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#ifStatement.
    def exitIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#readStatement.
    def enterReadStatement(self, ctx:KotlinParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#readStatement.
    def exitReadStatement(self, ctx:KotlinParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#printStatement.
    def enterPrintStatement(self, ctx:KotlinParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#printStatement.
    def exitPrintStatement(self, ctx:KotlinParser.PrintStatementContext):
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


    # Enter a parse tree produced by KotlinParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:KotlinParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:KotlinParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:KotlinParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:KotlinParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#equalityExpression.
    def enterEqualityExpression(self, ctx:KotlinParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#equalityExpression.
    def exitEqualityExpression(self, ctx:KotlinParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#relationalExpression.
    def enterRelationalExpression(self, ctx:KotlinParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#relationalExpression.
    def exitRelationalExpression(self, ctx:KotlinParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:KotlinParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:KotlinParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:KotlinParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:KotlinParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#unaryExpression.
    def enterUnaryExpression(self, ctx:KotlinParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#unaryExpression.
    def exitUnaryExpression(self, ctx:KotlinParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#membershipExpression.
    def enterMembershipExpression(self, ctx:KotlinParser.MembershipExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#membershipExpression.
    def exitMembershipExpression(self, ctx:KotlinParser.MembershipExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#rangeExpression.
    def enterRangeExpression(self, ctx:KotlinParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#rangeExpression.
    def exitRangeExpression(self, ctx:KotlinParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:KotlinParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:KotlinParser.PrimaryExpressionContext):
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


    # Enter a parse tree produced by KotlinParser#classDeclaration.
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#classDeclaration.
    def exitClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#classBody.
    def enterClassBody(self, ctx:KotlinParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by KotlinParser#classBody.
    def exitClassBody(self, ctx:KotlinParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#returnStatement.
    def enterReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#returnStatement.
    def exitReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
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


    # Enter a parse tree produced by KotlinParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:KotlinParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:KotlinParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by KotlinParser#commentStatement.
    def enterCommentStatement(self, ctx:KotlinParser.CommentStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#commentStatement.
    def exitCommentStatement(self, ctx:KotlinParser.CommentStatementContext):
        pass



del KotlinParser