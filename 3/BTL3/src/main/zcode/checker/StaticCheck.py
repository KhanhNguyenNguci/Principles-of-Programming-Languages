from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
        
class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.Return = False
        
        self.listFunction = {
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    # ArrayType
    # size: List[float]
    # eleType: Type
    def comparType(self, LHS : Type, RHS : Type) -> bool:
        if type(LHS) is not type(RHS): return False
        elif type(LHS) is ArrayType:
            if len(LHS.size) != len(RHS.size): return False
            for i in range(len(LHS.size)):
                if LHS.size[i] != RHS.size[i]: return False
            return type(LHS.eleType) is type(RHS.eleType)
        return True
    

    def comparListType(self, listLHS, listRHS):
        pass  
    
    
    def visitProgram(self, ast, param):
        for i in ast.decl: 
            self.visit(i, param)
         
        for key, value in self.listFunction.items(): 
            if value.body == False:
                raise NoDefinition(key) 


        checkMain = False
        for key, value in self.listFunction.items():
            if key == 'main':
                if type(value.typ) is not VoidType:
                    raise NoEntryPoint()
                
                if value.param != []:
                    raise NoEntryPoint()
                
                checkMain = True

        if not checkMain:
            raise NoEntryPoint()
        
  

    def visitVarDecl(self, ast, param):
        for decl in param[0]:
            if decl == ast.name.name:
                raise Redeclared(Variable(), ast.name.name)
        
        if ast.varType:
            
            if not ast.varInit:
                param[0][ast.name.name] = VarZcode(self.visit(ast.varType,param))
                return
            else:
                param[0][ast.name.name] = VarZcode(ast.varType)
                ltype = self.visit(ast.varType,param)
                rtype = self.visit(ast.varInit, param) 
                

                if not self.comparType(ltype, rtype):
                    if type(rtype) is VarZcode or type(rtype) is FuncZcode:
                        
                        rtype.typ= ltype
                    else:
                        raise TypeMismatchInStatement(ast)
                
                return
        else:
            if str(ast.modifier) == 'var':
                if not ast.varInit:
                    raise TypeCannotBeInferred(ast)
                else:
                    rtype = self.visit(ast.varInit,param) 
                    if type(rtype) is VarZcode or type(rtype) is FuncZcode:
                        raise TypeCannotBeInferred(ast) 
                    param[0][ast.name.name] = VarZcode(rtype)
            else:
                param[0][ast.name.name] = VarZcode(None)
                if ast.varInit:
                    rtype = self.visit(ast.varInit,param)
                    if type(rtype) is VarZcode or type(rtype) is FuncZcode:
                        raise TypeCannotBeInferred(ast) 
                    param[0][ast.name.name].typ = rtype
     


    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ast, param):
        
        for key,value in self.listFunction.items():
            if ast.name.name == key:
                if value.body:
                    raise Redeclared(Function(), ast.name.name)
                else:
                    if not ast.body:
                        raise Redeclared(Function(), ast.name.name)
        
        
        listParam = {}
        typeParam = []

        
        for paramDecl in ast.param:
            if paramDecl.name.name in listParam:
                raise Redeclared(Parameter(), paramDecl.name.name)
                
            typeParam.append(paramDecl.varType)
            listParam[paramDecl.name.name] = VarZcode(paramDecl.varType)

        
        
        self.Return = False

        if ast.name.name in self.listFunction:
            checkFunc = self.listFunction[ast.name.name]
            prevParams = checkFunc.param

            if len(prevParams) != len(listParam):
                raise Redeclared(Function(),ast.name.name)
            
            for prevParam, currParam in zip(prevParams,typeParam):
                if not self.comparType(prevParam, currParam):
                    
                    raise Redeclared(Function(), ast.name.name)
                
            self.function = self.listFunction[ast.name.name]

        else:
            self.listFunction[ast.name.name] = FuncZcode(typeParam,None,False)
            self.function = self.listFunction[ast.name.name]
        
        if ast.body:
            env = [listParam] + param
            self.visit(ast.body, env)
            self.function.body=True
            if not self.Return:
                if self.function.typ is None:
                    self.function.typ = VoidType()
                else:
                    raise TypeMismatchInStatement(Return(None))       

        
                
        self.function = None
        self.Return = False

        param[0][ast.name.name] = self.listFunction[ast.name.name]
        
        
    # name: str
    def visitId(self, ast, param):        
        varFound = None
        for scope in param:
            for decl in scope: 
                               
                if str(ast.name) == decl and isinstance(scope[decl],VarZcode):
                    varFound = scope[decl]
        if varFound is None:
            raise Undeclared(Identifier(), ast.name)
        if varFound.typ is not None:
            return varFound.typ
        return varFound
   
    # name: Id
    # args: List[Expr]
    def visitCallExpr(self, ast, param):       
        func = None
        for key in self.listFunction:
            if ast.name.name == key:
                func = self.listFunction[key]
        
        if func is None:
            raise Undeclared(Function(), ast.name.name)
        
        args = []
        for arg in ast.args:
            args = args + [self.visit(arg, param)]

        if len(args) != len(func.param):
            raise TypeMismatchInExpression(ast)
        
        for param, arg in zip(func.param, args):
            if not self.comparType(param, arg):
                raise TypeMismatchInExpression(ast)

        
        if func.typ is None:
            return func           

        return func.typ   
       

    # name: Id
    # args: List[Expr]
    # Statement
    def visitCallStmt(self, ast, param):
        func = None
        for key in self.listFunction:
            if ast.name.name == key:
                func = self.listFunction[key]
        
        if func is None:
            raise Undeclared(Function(), ast.name.name)
        
        args = []
        for arg in ast.args:
            args = args + [self.visit(arg, param)]

        if len(args) != len(func.param):
            raise TypeMismatchInStatement(ast)
        
        for param, arg in zip(func.param, args):
            if not self.comparType(param, arg):
                if isinstance(arg,VarZcode) or isinstance(arg, FuncZcode):
                    arg.typ = param
                    continue
                raise TypeMismatchInStatement(ast)
    

    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, param):
        exprType = self.visit(ast.expr,param) # expr
        if type(exprType) is not BoolType:
            
            if isinstance(exprType,VarZcode) or isinstance(exprType,FuncZcode):
                
                exprType.typ = BoolType()
            else:
                raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, [{}]+param) # thenStmt

        if ast.elifStmt:            
            for tuple in ast.elifStmt:
                exprType = self.visit(tuple[0], param)
                if type(exprType) is not BoolType:
                    if isinstance(exprType,VarZcode) or isinstance(exprType,FuncZcode):
                        exprType.typ = BoolType()
                    else:
                        raise TypeMismatchInStatement(ast)
                
                self.visit(tuple[1], [{}]+param)
            
            if ast.elseStmt:
                self.visit(ast.elseStmt,[{}]+param)           
     
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    # Statement
    def visitFor(self, ast, param):
        nameType = self.visit(ast.name,param) #name
        if type(nameType) is not NumberType:
            if isinstance(nameType,VarZcode):
                nameType.typ = NumberType()
            else:
                raise TypeMismatchInStatement(ast)
        
        condExprType = self.visit(ast.condExpr,param) #condExpr
        if type(condExprType) is not BoolType:            
            if isinstance(condExprType,VarZcode) or isinstance(condExprType,FuncZcode):
                condExprType.typ = BoolType()
            else:
                raise TypeMismatchInStatement(ast)
        
        updExprType = self.visit(ast.updExpr, param) #updExpr
        if type(updExprType) is not NumberType:
            if isinstance(updExprType,VarZcode) or isinstance(updExprType,FuncZcode):
                updExprType.typ = NumberType()
            else:
                raise TypeMismatchInStatement(ast)       

              
        self.BlockFor += 1
        self.visit(ast.body, [{}] + param)
        self.BlockFor -= 1
    

    # expr: Expr = None
    # Statement
    def visitReturn(self, ast, param):
        if self.function is not None:            
            if self.Return == False:
                if ast.expr is not None:
                    typ = self.visit(ast.expr, param)
                    self.Return = True
                    if isinstance(typ,VarZcode) or isinstance(typ,FuncZcode):
                        raise TypeCannotBeInferred(ast)
                    if self.function.typ is None:                   
                        self.function.typ = typ
                    else:
                        if type(self.function.typ) is not type(typ):
                            raise TypeMismatchInStatement(ast)
                    

            else:
                if ast.expr is not None:                    
                    
                    typ = self.visit(ast.expr,param)
                    
                    if isinstance(typ,VarZcode) or isinstance(typ,FuncZcode):
                        typ.typ = self.function.typ
                        return
                    
                    if not self.comparType(self.function.typ,typ):
                        raise TypeMismatchInStatement(ast)
                else:    
                    raise TypeMismatchInStatement(ast)                    

    # lhs: Expr
    # rhs: Expr
    # Statement
    def visitAssign(self, ast, param):
        ltype = self.visit(ast.lhs, param)
        rtype = self.visit(ast.rhs, param)
        
        if type(ltype) is VarZcode and type(rtype) is VarZcode:
            raise TypeCannotBeInferred(ast)
        
        if type(ltype) in [VarZcode,FuncZcode]:
            
            ltype.typ = rtype
            return
        
        elif type(rtype) in [VarZcode,FuncZcode]:
            rtype.typ = ltype

        else:
            if type(rtype) is not type(ltype):
                raise TypeMismatchInStatement(ast)
            
    # op: str
    # left: Expr
    # right: Expr
    # Expression
    def visitBinaryOp(self, ast, param):
        if ast.op in ['+','-','*','/','%']:
            # Almost done
            ltype = self.visit(ast.left, param)
            rtype = self.visit(ast.right, param)         

            if type(ltype) is not NumberType and type(rtype) is not NumberType:
                if (isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode)) and (isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode)):
                    ltype.typ = NumberType()
                    rtype.typ = NumberType()
                else:
                    raise TypeMismatchInExpression(ast)
            
            elif type(ltype) is not NumberType:
                if isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode):
                    ltype.typ = rtype
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(rtype) is not NumberType:
                if isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode):
                    rtype.typ = ltype
                else:
                    raise TypeMismatchInExpression(ast)
                
            else:
                return NumberType()
            
            return NumberType()

        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            ltype = self.visit(ast.left, param)
            rtype = self.visit(ast.right,param)

            if type(ltype) is not NumberType and type(rtype) is not NumberType:
                if (isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode)) and (isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode)):
                    ltype.typ = NumberType()
                    rtype.typ = NumberType()
                else:
                    raise TypeMismatchInExpression(ast)
            
            elif type(ltype) is not NumberType:
                if isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode):
                    ltype.typ = rtype
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(rtype) is not NumberType:
                if isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode):
                    rtype.typ = ltype
                else:
                    raise TypeMismatchInExpression(ast)
                
            else:
                return BoolType()
            
            return BoolType() 
        
        elif ast.op in ['and', 'or']:
            ltype = self.visit(ast.left, param)
            rtype = self.visit(ast.right,param)

            if type(ltype) is not BoolType and type(rtype) is not BoolType:
                if (isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode)) and (isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode)):
                    ltype.typ = BoolType()
                    rtype.typ = BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            
            elif type(ltype) is not BoolType:
                if isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode):
                    ltype.typ = rtype
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(rtype) is not BoolType:
                if isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode):
                    rtype.typ = ltype
                else:
                    raise TypeMismatchInExpression(ast)
                
            else:
                return BoolType()
            
            return BoolType() 
        
        elif ast.op in ['==']:
            ltype = self.visit(ast.left, param)
            rtype = self.visit(ast.right, param)

            if type(ltype) is not StringType and type(rtype) is not StringType:
                if (isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode)) and (isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode)):
                    ltype.typ = StringType()
                    rtype.typ = StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            
            elif type(ltype) is not StringType:
                if isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode):
                    ltype.typ = rtype
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(rtype) is not StringType:
                if isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode):
                    rtype.typ = ltype
                else:
                    raise TypeMismatchInExpression(ast)
                
            else:
                return BoolType()
            
            return BoolType() 
        
        else:
            ltype = self.visit(ast.left, param)
            rtype = self.visit(ast.right, param)

            if type(ltype) is not StringType and type(rtype) is not StringType:
                if (isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode)) and (isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode)):
                    ltype.typ = StringType()
                    rtype.typ = StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            
            elif type(ltype) is not StringType:
                if isinstance(ltype,VarZcode) or isinstance(ltype,FuncZcode):
                    ltype.typ = rtype
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(rtype) is not StringType:
                if isinstance(rtype,VarZcode) or isinstance(rtype,FuncZcode):
                    rtype.typ = ltype
                else:
                    raise TypeMismatchInExpression(ast)
                
            else:
                return StringType()
            
            return StringType()

        
  
    # op: str
    # operand: Expr
    # Expression
    def visitUnaryOp(self, ast, param):
        if ast.op in ['+','-']:
            typ = self.visit(ast.operand,param)
            if type(typ) is not NumberType:
                if isinstance(typ,VarZcode) or isinstance(typ,FuncZcode):
                    typ.typ = NumberType()
                else:
                    raise TypeMismatchInExpression(ast)
            return NumberType()  
        else:
            typ = self.visit(ast.operand, param)
            if type(typ) is not BoolType:
                if isinstance(typ,VarZcode) or isinstance(typ,FuncZcode):
                    typ.typ = NumberType()
                else:
                    raise TypeMismatchInExpression(ast)
            return BoolType()     

    # arr: Expr
    # idx: List[Expr]
    # Expression
    def visitArrayCell(self, ast, param):        
        arrType = self.visit(ast.arr, param)
        if not isinstance(arrType,ArrayType):
            raise TypeMismatchInExpression(ast) 
        
        for index in ast.idx:
            indexType = self.visit(index, param)
            if not isinstance(indexType,NumberType):
                if isinstance(indexType,VarZcode) or isinstance(indexType,FuncZcode):
                    indexType.typ = NumberType()
                else:
                    raise TypeMismatchInExpression(ast)     
   
        if len(arrType.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arrType.size) == len(ast.idx): return arrType.eleType
        else:
            return ArrayType(arrType.size[1:],arrType.eleType) 

    # value: List[Expr]
    def visitArrayLiteral(self, ast, param):
        allTyp = []
        for item in ast.value: 
            allTyp = allTyp + [self.visit(item, param)]
        
        bestTyp = None
        for typ in allTyp:
            if isinstance(typ, BoolType) or isinstance(typ, StringType) or isinstance(typ, NumberType) or isinstance (typ,ArrayType):
                bestTyp = typ
                break

        for typ in allTyp:
            if isinstance(typ, VarZcode) or isinstance(typ, FuncZcode):
                typ.typ = bestTyp
                continue
            if type(typ) is not type(bestTyp):
                raise TypeMismatchInExpression(ast)

        if bestTyp is None:
            return ast
        
        typ = bestTyp
        
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)
    
    # stmt: List[Stmt]
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)
            
    def visitContinue(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()