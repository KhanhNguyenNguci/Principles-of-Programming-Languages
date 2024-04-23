from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # Visit a parse tree produced by ZCodeParser#list_declared.
    def visitList_declared(self, ctx:ZCodeParser.List_declaredContext):
        if ctx.list_declared():
            return [self.visit(ctx.declared())] + self.visit(ctx.list_declared())
        return [self.visit(ctx.declared())]


    # Visit a parse tree produced by ZCodeParser#declared.
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        if ctx.variables():
            return self.visit(ctx.variables())
        return self.visit(ctx.function())


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        name = Id(ctx.ID().getText())
        param = []
        body = None
        if ctx.parameters_list():
            param = self.visit(ctx.parameters_list())
        if ctx.return_stmt():
            body = self.visit(ctx.return_stmt())
        elif ctx.block_stmt():
            body = self.visit(ctx.block_stmt())
        return FuncDecl(name, param, body)

    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        return self.visit(ctx.implicit_dynamic())


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        name = Id(ctx.ID().getText())
        varType = None
        modifier = ctx.VAR().getText()
        varInit = self.visit(ctx.exp())
        return VarDecl(name, varType, modifier, varInit)

    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        name = Id(ctx.ID().getText())
        varType = None
        modifier = ctx.DYNAMIC().getText()
        varInit = None
        if ctx.ASSIGNINIT():
            varInit = self.visit(ctx.exp())
        return VarDecl(name, varType, modifier, varInit)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        name = Id(ctx.ID().getText())
        varType = self.visit(ctx.type_prime())
        modifier = None
        varInit = None
        if ctx.list_NUMBER_LIT():
            arrType = self.visit(ctx.type_prime())
            size = self.visit(ctx.list_NUMBER_LIT())
            varType = ArrayType(size,arrType)
        
        if ctx.exp():
            varInit = self.visit(ctx.exp())
            
        return VarDecl(name,varType,modifier, varInit)
            
            


    # Visit a parse tree produced by ZCodeParser#list_NUMBER_LIT.
    def visitList_NUMBER_LIT(self, ctx:ZCodeParser.List_NUMBER_LITContext):
        if ctx.COMMA():
            return [float(ctx.NUMBER_LITERAL().getText())] + self.visit(ctx.list_NUMBER_LIT())
        return [float(ctx.NUMBER_LITERAL().getText())]


    # Visit a parse tree produced by ZCodeParser#parameters_list.
    def visitParameters_list(self, ctx:ZCodeParser.Parameters_listContext):
        if ctx.COMMA():
            return [self.visit(ctx.parameter())] + self.visit(ctx.parameters_list())
        return [self.visit(ctx.parameter())]


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        name = Id(ctx.ID().getText())
        modifier = None
        varInit = None
        varType = self.visit(ctx.type_prime())
        if ctx.list_NUMBER_LIT():
            varType = ArrayType(self.visit(ctx.list_NUMBER_LIT()), self.visit(ctx.type_prime()))
        
        return VarDecl(name,varType,modifier,varInit)
            
    def visitType_prime(self, ctx:ZCodeParser.Type_primeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()

    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBER_LITERAL():
            return NumberLiteral(float(ctx.NUMBER_LITERAL().getText()))
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if ctx.TRUE():
            return BooleanLiteral(True)
        if ctx.FALSE():
            return BooleanLiteral(False)
        return ArrayLiteral(self.visit(ctx.array_literal()))
    
    
    # Visit a parse tree produced by ZCodeParser#list_expr.
    def visitList_expr(self, ctx:ZCodeParser.List_exprContext):
        if ctx.COMMA():
            return [self.visit(ctx.exp())] + self.visit(ctx.list_expr())
        return [self.visit(ctx.exp())]


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visit(ctx.list_literal())


    # Visit a parse tree produced by ZCodeParser#list_literal.
    def visitList_literal(self, ctx:ZCodeParser.List_literalContext):
        if ctx.COMMA():
            return [self.visit(ctx.exp())] + self.visit(ctx.list_literal())
        return [self.visit(ctx.exp())]


    # Visit a parse tree produced by ZCodeParser#exp.
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        if ctx.CONCAT():
            op = ctx.CONCAT().getText()
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinaryOp(op,left,right)
        
        return self.visit(ctx.exp1(0))


    # Visit a parse tree produced by ZCodeParser#exp1.
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 3:
            if ctx.EQUAL_NUMBER():
                op = ctx.EQUAL_NUMBER().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
            elif ctx.EQUAL_STRING():
                op = ctx.EQUAL_STRING().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
            elif ctx.NOT_EQUAL():
                op = ctx.NOT_EQUAL().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
            elif ctx.LESS():
                op = ctx.LESS().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
            elif ctx.GREATER():
                op = ctx.GREATER().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
            elif ctx.LESS_EQUAL():
                op = ctx.LESS_EQUAL().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
            else:
                op = ctx.GREATER_EQUAL().getText()
                left = self.visit(ctx.exp2(0))
                right = self.visit(ctx.exp2(1))
                return BinaryOp(op,left,right)
            
        return self.visit(ctx.exp2(0))


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        if ctx.getChildCount() == 3:
            if ctx.AND():
                op = ctx.AND().getText()
                left = self.visit(ctx.exp2())
                right = self.visit(ctx.exp3())
                return BinaryOp(op,left,right)
            else:
                op = ctx.OR().getText()
                left = self.visit(ctx.exp2())
                right = self.visit(ctx.exp3())
                return BinaryOp(op,left,right)
            
        return self.visit(ctx.exp3())


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                op = ctx.ADD().getText()
                left = self.visit(ctx.exp3())
                right = self.visit(ctx.exp4())
                return BinaryOp(op,left,right)
            else:
                op = ctx.MINUS().getText()
                left = self.visit(ctx.exp3())
                right = self.visit(ctx.exp4())
                return BinaryOp(op,left,right)
        return self.visit(ctx.exp4())


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        if ctx.getChildCount() == 3:
            if ctx.MULTIPLY():
                op = ctx.MULTIPLY().getText()
                left = self.visit(ctx.exp4())
                right = self.visit(ctx.exp5())
                return BinaryOp(op,left,right)
            elif ctx.DIVIDE():
                op = ctx.DIVIDE().getText()
                left = self.visit(ctx.exp4())
                right = self.visit(ctx.exp5())
                return BinaryOp(op,left,right)
            else:
                op = ctx.MODULO().getText()
                left = self.visit(ctx.exp4())
                right = self.visit(ctx.exp5())
                return BinaryOp(op,left,right)
        return self.visit(ctx.exp5())
            


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            operand = self.visit(ctx.exp5())
            return UnaryOp(op,operand)
        return self.visit(ctx.exp6())


    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        if ctx.MINUS():
            op = ctx.MINUS().getText()
            operand = self.visit(ctx.exp6())
            return UnaryOp(op,operand)
        return self.visit(ctx.exp7())


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        if ctx.index_operators():
            return self.visit(ctx.index_operators())
        return self.visit(ctx.exp8())


    # Visit a parse tree produced by ZCodeParser#exp8.
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        if ctx.list_expr():
            return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.list_expr()))
        elif ctx.ID() and ctx.LPARENT():
            return CallExpr(Id(ctx.ID().getText()), [])
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.literal():
            return self.visit(ctx.literal())
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by ZCodeParser#list_stmts.
    def visitList_stmts(self, ctx:ZCodeParser.List_stmtsContext):
        if ctx.list_stmts():
            return [self.visit(ctx.stmt())] + self.visit(ctx.list_stmts())
        return [self.visit(ctx.stmt())]


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.declaration_stmt():
            return self.visit(ctx.declaration_stmt())
        elif ctx.assignment_stmt():
            return self.visit(ctx.assignment_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        return self.visit(ctx.block_stmt())


    # Visit a parse tree produced by ZCodeParser#declaration_stmt.
    def visitDeclaration_stmt(self, ctx:ZCodeParser.Declaration_stmtContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        elif ctx.keyword_var():
            return self.visit(ctx.keyword_var())
        else: return self.visit(ctx.implicit_dynamic())


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.stmt())
        elifStmt = self.visit(ctx.elif_stmt())
        elseStmt = self.visit(ctx.else_stmt())

        return If(expr,thenStmt,elifStmt,elseStmt)


    # # Visit a parse tree produced by ZCodeParser#list_elif_stmts.
    # def visitList_elif_stmts(self, ctx:ZCodeParser.List_elif_stmtsContext):
    #     if ctx.list_elif_stmts():
    #         return self.visit(ctx.elif_stmt()) + self.visit(ctx.list_elif_stmts())
    #     return self.visit(ctx.elif_stmt())

    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        if ctx.getChildCount() == 0:
            return []
        
        exp = self.visit(ctx.exp())
        stmt = self.visit(ctx.stmt())
        return [(exp,stmt)] + self.visit(ctx.elif_stmt())

    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        return None


    # Visit a parse tree produced by ZCodeParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        lhs = []
        rhs = self.visit(ctx.exp())
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else: lhs = self.visit(ctx.index_operators1())
        
        return Assign(lhs,rhs)
            


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        if ctx.ID():
            arr = Id(ctx.ID().getText())
            idx = self.visit(ctx.list_expr())
            return ArrayCell(arr,idx)
        
        arr = self.visit(ctx.call_stmt1())
        idx = self.visit(ctx.list_expr())
        return ArrayCell(arr,idx)

    # Visit a parse tree produced by ZCodeParser#index_operators1.
    def visitIndex_operators1(self, ctx:ZCodeParser.Index_operators1Context):
        name = Id(ctx.ID().getText())
        args = self.visit(ctx.list_expr())
        return ArrayCell(name,args)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        name = Id(ctx.ID().getText())
        condExpr =  self.visit(ctx.exp(0))
        updExpr = self.visit(ctx.exp(1))
        body = self.visit(ctx.stmt())
        
        return For(name,condExpr,updExpr,body)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return()


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        name = Id(ctx.ID().getText())
        if ctx.list_expr():
            args = self.visit(ctx.list_expr())
            return CallStmt(name,args)
        return CallStmt(name,[])


    # Visit a parse tree produced by ZCodeParser#call_stmt1.
    def visitCall_stmt1(self, ctx:ZCodeParser.Call_stmt1Context):
        name = Id(ctx.ID().getText())
        if ctx.list_expr():
            args = self.visit(ctx.list_expr())
            return CallExpr(name,args)
        return CallExpr(name,[])

    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        if ctx.list_stmts():
            return Block(self.visit(ctx.list_stmts()))
        return Block([])

    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)