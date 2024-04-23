import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Please note thast some of these tests are not mine
    def test_declared(self):
        input = """
            number a
        """
        expect = "Program([VarDecl(Id(a), NumberType, None, None)])"
        self.assertTrue(TestAST.test(input, expect, 301))
        
        input = """
            var a <- 10
        """
        expect = "Program([VarDecl(Id(a), None, var, NumLit(10.0))])"
        self.assertTrue(TestAST.test(input, expect, 302))
        
        input = """
            string a <- 20
        """
        expect = "Program([VarDecl(Id(a), StringType, None, NumLit(20.0))])"

        self.assertTrue(TestAST.test(input, expect, 303))
        
        input = """
             dynamic a <- 20
        """
        expect = "Program([VarDecl(Id(a), None, dynamic, NumLit(20.0))])"

        self.assertTrue(TestAST.test(input, expect, 304))
        
        input = """
            string a[2] 
        """
        expect = "Program([VarDecl(Id(a), ArrayType([2.0], StringType), None, None)])"
        self.assertTrue(TestAST.test(input, expect, 305))
        
        input = """
            dynamic a
        """
        expect = "Program([VarDecl(Id(a), None, dynamic, None)])"
        self.assertTrue(TestAST.test(input, expect, 306))
        
        input = """
            bool a
        """
        expect = "Program([VarDecl(Id(a), BoolType, None, None)])"
        self.assertTrue(TestAST.test(input, expect, 307))
        
        input = """
            dynamic a <- 20
        """
        expect = "Program([VarDecl(Id(a), None, dynamic, NumLit(20.0))])"
        self.assertTrue(TestAST.test(input, expect, 308))
        
        input = """
            string a[2] <- [20,30]
        """
        expect = "Program([VarDecl(Id(a), ArrayType([2.0], StringType), None, ArrayLit(NumLit(20.0), NumLit(30.0)))])"
        self.assertTrue(TestAST.test(input, expect, 309))

        input = """
            number a <- [10,10]
        """
        expect = "Program([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(10.0), NumLit(10.0)))])"
        self.assertTrue(TestAST.test(input, expect, 310))
                
        input = """
            func main()
        """
        expect = "Program([FuncDecl(Id(main), [], None)])"
        self.assertTrue(TestAST.test(input, expect, 311))
        input = """
            func main(number a)
        """
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"
        self.assertTrue(TestAST.test(input, expect, 312))
        input = """
            func main(string s)
        """
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(s), StringType, None, None)], None)])"
        self.assertTrue(TestAST.test(input, expect, 313))
        input = """
            func main(number n, string s, bool b)
        """
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(s), StringType, None, None), VarDecl(Id(b), BoolType, None, None)], None)])"
        self.assertTrue(TestAST.test(input, expect, 314))
        input = """
            func main()
            begin
            end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 315))
        input = """
            func main(number a)
            begin
            end
        """
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 316))
        input = """
            func main(number n, string s, bool b)
            begin
            break
            end
        """
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(s), StringType, None, None), VarDecl(Id(b), BoolType, None, None)], Block([Break]))])"
        self.assertTrue(TestAST.test(input, expect, 317))
        input = """
            func main()
            begin
                break
                break
                break
                continue
                continue
            end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Break, Break, Break, Continue, Continue]))])"
        self.assertTrue(TestAST.test(input, expect, 318))
        input = """
            func main()
            func main(number a)
            func main(bool a)
        """
        expect = "Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None), FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], None)])"
        self.assertTrue(TestAST.test(input, expect, 319))
        input = """
            var d <- 1 ## 12
        """
        expect = "Program([VarDecl(Id(d), None, var, NumLit(1.0))])"
        self.assertTrue(TestAST.test(input, expect, 320))

        
    def test_Expression(self):
        input = """
            var abcd <- "ab" ... "cd" 
        """
        expect = "Program([VarDecl(Id(abcd), None, var, BinaryOp(..., StringLit(ab), StringLit(cd)))])"
        self.assertTrue(TestAST.test(input, expect, 321))
        input = """
            var t <- 1 > "3" 
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(>, NumLit(1.0), StringLit(3)))])"
        self.assertTrue(TestAST.test(input, expect, 322))
        input = """
            var t <- 1 >= 3
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(>=, NumLit(1.0), NumLit(3.0)))])"
        self.assertTrue(TestAST.test(input, expect, 323))
        input = """
            var t <- true = "true"
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(=, BooleanLit(True), StringLit(true)))])"
        self.assertTrue(TestAST.test(input, expect, 324))
        input = """
            var t <- false == "true"
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(==, BooleanLit(False), StringLit(true)))])"
        self.assertTrue(TestAST.test(input, expect, 325))
        input = """
            var t <- true < "true"
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(<, BooleanLit(True), StringLit(true)))])"
        self.assertTrue(TestAST.test(input, expect, 326))
        input = """
            var t <- 1 <= "tuan"
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(<=, NumLit(1.0), StringLit(tuan)))])"
        self.assertTrue(TestAST.test(input, expect, 327))
        input = """
            var t <- tuan >= "ai" ... 1 > 2
        """
        expect = "Program([VarDecl(Id(t), None, var, BinaryOp(..., BinaryOp(>=, Id(tuan), StringLit(ai)), BinaryOp(>, NumLit(1.0), NumLit(2.0))))])"
        self.assertTrue(TestAST.test(input, expect, 328))
        input = """
            var b <- true and "true" or 1 
        """
        expect = "Program([VarDecl(Id(b), None, var, BinaryOp(or, BinaryOp(and, BooleanLit(True), StringLit(true)), NumLit(1.0)))])"
        self.assertTrue(TestAST.test(input, expect, 329))
        input = """
            var b <- 1 / 2 * 7 % 1
        """
        expect = "Program([VarDecl(Id(b), None, var, BinaryOp(%, BinaryOp(*, BinaryOp(/, NumLit(1.0), NumLit(2.0)), NumLit(7.0)), NumLit(1.0)))])"
        self.assertTrue(TestAST.test(input, expect, 330))
        input = """
            var b <- 1 / 2 / 7 * 3 % 2
        """
        expect = "Program([VarDecl(Id(b), None, var, BinaryOp(%, BinaryOp(*, BinaryOp(/, BinaryOp(/, NumLit(1.0), NumLit(2.0)), NumLit(7.0)), NumLit(3.0)), NumLit(2.0)))])"
        self.assertTrue(TestAST.test(input, expect, 331))
        input = """
            var bv <- -1 * not 1
        """
        expect = "Program([VarDecl(Id(bv), None, var, BinaryOp(*, UnaryOp(-, NumLit(1.0)), UnaryOp(not, NumLit(1.0))))])"
        self.assertTrue(TestAST.test(input, expect, 332))
        input = """
             var bv <- not----C
        """
        expect = "Program([VarDecl(Id(bv), None, var, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(C)))))))])"
        self.assertTrue(TestAST.test(input, expect, 333))
        input = """
            var a <- a()
        """
        expect = "Program([VarDecl(Id(a), None, var, CallExpr(Id(a), []))])"
        self.assertTrue(TestAST.test(input, expect, 334))
        input = """
            var a <- a(1,2)
        """
        expect = "Program([VarDecl(Id(a), None, var, CallExpr(Id(a), [NumLit(1.0), NumLit(2.0)]))])"
        self.assertTrue(TestAST.test(input, expect, 335))
        input = """
            var a <- a(x,array[2])[2]
        """
        expect = "Program([VarDecl(Id(a), None, var, ArrayCell(CallExpr(Id(a), [Id(x), ArrayCell(Id(array), [NumLit(2.0)])]), [NumLit(2.0)]))])"
        self.assertTrue(TestAST.test(input, expect, 336))
        input = """
            var a <- a(x,y[3] ... 2)[1,2]
        """
        expect = "Program([VarDecl(Id(a), None, var, ArrayCell(CallExpr(Id(a), [Id(x), BinaryOp(..., ArrayCell(Id(y), [NumLit(3.0)]), NumLit(2.0))]), [NumLit(1.0), NumLit(2.0)]))])"
        self.assertTrue(TestAST.test(input, expect, 337))
        input = """
            var e <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
        """
        expect = "Program([VarDecl(Id(e), None, var, BinaryOp(+, ArrayLit(StringLit(tr), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)), ArrayLit(ArrayLit(NumLit(1.0), BinaryOp(+, NumLit(2.0), BinaryOp(/, BinaryOp(*, NumLit(2.0), NumLit(2.0)), NumLit(3.0))), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))))])"
        self.assertTrue(TestAST.test(input, expect, 338))
        input = """
            var a <- "a"
            var b <- "bb"
            var c <- "ccc"
        """
        expect = "Program([VarDecl(Id(a), None, var, StringLit(a)), VarDecl(Id(b), None, var, StringLit(bb)), VarDecl(Id(c), None, var, StringLit(ccc))])"
        self.assertTrue(TestAST.test(input, expect, 339))
        input = """
            number x <- true
            number y <- false
            number z <- 1
            number x <- 1.0
            number y <- "123"
            number z <- "123.0"
        """
        expect = "Program([VarDecl(Id(x), NumberType, None, BooleanLit(True)), VarDecl(Id(y), NumberType, None, BooleanLit(False)), VarDecl(Id(z), NumberType, None, NumLit(1.0)), VarDecl(Id(x), NumberType, None, NumLit(1.0)), VarDecl(Id(y), NumberType, None, StringLit(123)), VarDecl(Id(z), NumberType, None, StringLit(123.0))])"
        self.assertTrue(TestAST.test(input, expect, 340))
        
        input = """
            var x <- [[x,y,z]]
            var x <- "123" + -2 - 3
            var x <- ------2
        """
        expect ="Program([VarDecl(Id(x), None, var, ArrayLit(ArrayLit(Id(x), Id(y), Id(z)))), VarDecl(Id(x), None, var, BinaryOp(-, BinaryOp(+, StringLit(123), UnaryOp(-, NumLit(2.0))), NumLit(3.0))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(2.0))))))))])"
        self.assertTrue(TestAST.test(input, expect, 341))
        
        input = """
            var x <- [1, "tuan", true, false]
        """
        expect = "Program([VarDecl(Id(x), None, var, ArrayLit(NumLit(1.0), StringLit(tuan), BooleanLit(True), BooleanLit(False)))])"
        self.assertTrue(TestAST.test(input, expect, 342))   
        
        input = """
            var x <- [[[1],[[2],[[3]]]],[1]]
        """
        expect = "Program([VarDecl(Id(x), None, var, ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)), ArrayLit(ArrayLit(NumLit(2.0)), ArrayLit(ArrayLit(NumLit(3.0))))), ArrayLit(NumLit(1.0))))])"
        self.assertTrue(TestAST.test(input, expect, 343))  
        
        input = """
            var x <- a[1,2,3]
        """
        expect = "Program([VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))])"
        self.assertTrue(TestAST.test(input, expect, 344))  
        
        input = """
            var x <- 2 and 3 or 3 and a[1,2,3] or not - 1 + 10
        """
        expect = "Program([VarDecl(Id(x), None, var, BinaryOp(or, BinaryOp(and, BinaryOp(or, BinaryOp(and, NumLit(2.0), NumLit(3.0)), NumLit(3.0)), ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), BinaryOp(+, UnaryOp(not, UnaryOp(-, NumLit(1.0))), NumLit(10.0))))])"
        self.assertTrue(TestAST.test(input, expect, 345))  
        
        input = """
            var x <- a[1+2,3+4]
        """
        expect = "Program([VarDecl(Id(x), None, var, ArrayCell(Id(a), [BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(+, NumLit(3.0), NumLit(4.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 346))  
        
        input = """
            var x <- foo()
        """
        expect = "Program([VarDecl(Id(x), None, var, CallExpr(Id(foo), []))])"
        self.assertTrue(TestAST.test(input, expect, 347)) 
        
        input = """
            var x <- foo(1+1, "a")
        """
        expect = "Program([VarDecl(Id(x), None, var, CallExpr(Id(foo), [BinaryOp(+, NumLit(1.0), NumLit(1.0)), StringLit(a)]))])"
        self.assertTrue(TestAST.test(input, expect, 348)) 
        
        input = """
            var x <- foo(foo(3))
        """
        expect = "Program([VarDecl(Id(x), None, var, CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])]))])"
        self.assertTrue(TestAST.test(input, expect, 349)) 
        
        input = """
            var x <- 35*10 + (30+20)/10 - (-1) 
        """
        expect = "Program([VarDecl(Id(x), None, var, BinaryOp(-, BinaryOp(+, BinaryOp(*, NumLit(35.0), NumLit(10.0)), BinaryOp(/, BinaryOp(+, NumLit(30.0), NumLit(20.0)), NumLit(10.0))), UnaryOp(-, NumLit(1.0))))])"
        self.assertTrue(TestAST.test(input, expect, 350)) 
         
    def test_Statements(self):
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Continue]))])"
        self.assertTrue(TestAST.test(input, expect, 351)) 
        input = """
            func main()
                begin
                    break
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Break]))])"
        self.assertTrue(TestAST.test(input, expect, 352)) 
        input = """
            func main()
                begin
                    break
                    continue
                    break
                    continue
                end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Break, Continue, Break, Continue]))])"
        self.assertTrue(TestAST.test(input, expect, 353)) 
        input = """
            func main()
                begin
                    begin
                        begin
                            break
                        end
                    end
                    begin
                        continue
                    end
                end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Block([Block([Break])]), Block([Continue])]))])"
        self.assertTrue(TestAST.test(input, expect, 354)) 
        input = """
            func main()
                begin
                    pi <- 3.14
                end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(pi), NumLit(3.14))]))])"
        self.assertTrue(TestAST.test(input, expect, 355)) 
        input = """
            func main()
                begin
                    x <- 35*10 + (30+20)/10 - (-1) 
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(x), BinaryOp(-, BinaryOp(+, BinaryOp(*, NumLit(35.0), NumLit(10.0)), BinaryOp(/, BinaryOp(+, NumLit(30.0), NumLit(20.0)), NumLit(10.0))), UnaryOp(-, NumLit(1.0))))]))])"
        self.assertTrue(TestAST.test(input, expect, 356)) 
        input = """
            func main()
                begin  
                    a <- 10
                end
            func main()
                begin
                    a <- 1
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(10.0))])), FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 357)) 
        input = """
            func main()
                begin
                    pi[1] <- 3.14 
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(pi), [NumLit(1.0)]), NumLit(3.14))]))])"
        self.assertTrue(TestAST.test(input, expect, 358)) 
        input = """
            func main()
                begin
                    pi[1,2,3] <- 3.14
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(pi), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), NumLit(3.14))]))])"
        self.assertTrue(TestAST.test(input, expect, 359)) 
        input = """
            func main()
                begin
                    if (true)
                        pi <- 3.14
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), AssignStmt(Id(pi), NumLit(3.14))), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 360)) 
        input = """
            func main()
                begin
                    if (true)
                        pi <- 3.14
                    else pi <- -3.14
                end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), AssignStmt(Id(pi), NumLit(3.14))), [], AssignStmt(Id(pi), UnaryOp(-, NumLit(3.14))))]))])"
        self.assertTrue(TestAST.test(input, expect, 361)) 
        input = """
            func main()
                begin
                    if (true) pi <- 3.14
                    elif (true) break
                    else pi <- -3.14
                end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), AssignStmt(Id(pi), NumLit(3.14))), [(BooleanLit(True), Break)], AssignStmt(Id(pi), UnaryOp(-, NumLit(3.14))))]))])"
        self.assertTrue(TestAST.test(input, expect, 362)) 
        input = """
            func main()
                begin
                    if (true) pi <- 3.14
                    elif (1 + 2 != 3) 
                        break
                    elif (10 ... 10) 
                        continue
                    elif (1 + 1) 
                        continue
                    else pi <- -3.14
                end  
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), AssignStmt(Id(pi), NumLit(3.14))), [(BinaryOp(!=, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), Break), (BinaryOp(..., NumLit(10.0), NumLit(10.0)), Continue), (BinaryOp(+, NumLit(1.0), NumLit(1.0)), Continue)], AssignStmt(Id(pi), UnaryOp(-, NumLit(3.14))))]))])"
        self.assertTrue(TestAST.test(input, expect, 363)) 
        input = """
            func main()
                begin
                    if (true)
                        if (true)   
                            if (true) break
                            else continue
                        else continue
                end  
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), If((BooleanLit(True), If((BooleanLit(True), Break), [], Continue)), [], Continue)), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 364)) 
        input = """
            func main()
                begin
                    if (true)
                        pi <- 3.14
                    elif (1 + 2 != 3) 
                        if (true) continue
                        elif (1 + 2) break
                        else a <- 1
                    elif ("a" == "a") 
                        continue
                    else pi <- -3.14
                end  
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), AssignStmt(Id(pi), NumLit(3.14))), [(BinaryOp(!=, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), If((BooleanLit(True), Continue), [(BinaryOp(+, NumLit(1.0), NumLit(2.0)), Break)], AssignStmt(Id(a), NumLit(1.0)))), (BinaryOp(==, StringLit(a), StringLit(a)), Continue)], AssignStmt(Id(pi), UnaryOp(-, NumLit(3.14))))]))])"
        self.assertTrue(TestAST.test(input, expect, 365)) 
        input = """
            func main()
            begin
            for i until i >= 10 by 1 + 1
                begin  
                    a <- 1
                end
            end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), BinaryOp(+, NumLit(1.0), NumLit(1.0)), Block([AssignStmt(Id(a), NumLit(1.0))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 366)) 
        input = """
            func main()
            begin
            for i until i >= 10 by 1 + 1  
                a <- 1
            end 
        """
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), BinaryOp(+, NumLit(1.0), NumLit(1.0)), AssignStmt(Id(a), NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 367)) 
        input = """
            func main()
            begin 
                continue ## dsa is good
                break
                for i until i >= 32 by 1 + 1 ... 1 / 1
                    begin
                        break
                        continue
                    end
                ## why am i here
            end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Continue, Break, For(Id(i), BinaryOp(>=, Id(i), NumLit(32.0)), BinaryOp(..., BinaryOp(+, NumLit(1.0), NumLit(1.0)), BinaryOp(/, NumLit(1.0), NumLit(1.0))), Block([Break, Continue]))]))])"
        self.assertTrue(TestAST.test(input, expect, 368)) 
        input = """
            func main()
            return
        """
        expect = "Program([FuncDecl(Id(main), [], Return())])"
        self.assertTrue(TestAST.test(input, expect, 369)) 
        input = """
            func main()
            return 10
        """
        expect = "Program([FuncDecl(Id(main), [], Return(NumLit(10.0)))])"
        self.assertTrue(TestAST.test(input, expect, 370)) 
        
        input = """
            func main()
            begin
            main()
            main()
            mainy()
            end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(main), []), CallStmt(Id(main), []), CallStmt(Id(mainy), [])]))])"
        self.assertTrue(TestAST.test(input, expect, 371))
        
        input = """
            func main()
                return foo()
        """
        expect = "Program([FuncDecl(Id(main), [], Return(CallExpr(Id(foo), [])))])"
        self.assertTrue(TestAST.test(input, expect, 372))

        input = """
            func main()
                begin 
                    return ([1,2,3]) + 1
                    return main()
                    main([1,2,3], 1+2, a, c ... e)
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Return(BinaryOp(+, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))), Return(CallExpr(Id(main), [])), CallStmt(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), BinaryOp(+, NumLit(1.0), NumLit(2.0)), Id(a), BinaryOp(..., Id(c), Id(e))])]))])"
        self.assertTrue(TestAST.test(input, expect, 373))
        
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1.0)), AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), NumLit(2.0)), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0)]), BinaryOp(+, NumLit(4.0), NumLit(2.0)))])), FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [BinaryOp(+, NumLit(1.0), NumLit(1.0)), NumLit(3.0)]), NumLit(1.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 374))
        
        input = """
            func main()
                begin
                    for i until i >= 32 by 1
                    begin
                        for i until i >= 32 by 1
                            begin
                                i <- i + 1  
                            end
                    end
                end
            
        """
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(32.0)), NumLit(1.0), Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(32.0)), NumLit(1.0), Block([AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 375))
        
        input = """
            func main()
                begin
                    return 10
                end
            func main()
                begin
                    if (a) return 10
                    else break
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([Return(NumLit(10.0))])), FuncDecl(Id(main), [], Block([If((Id(a), Return(NumLit(10.0))), [], Break)]))])"
        self.assertTrue(TestAST.test(input, expect, 376))
        

        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 2
                    elif (true) return 3
                    else return 4
                end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), Return(NumLit(1.0))), [(BooleanLit(True), Return(NumLit(2.0))), (BooleanLit(True), Return(NumLit(3.0)))], Return(NumLit(4.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 377))     
        
        input = """
            func main()
            begin
                var c <- a[1,2]
                number c <- fun()[1,2]
                bool c <- fun(1,2)[1,3]
            end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(c), None, var, ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)])), VarDecl(Id(c), NumberType, None, ArrayCell(CallExpr(Id(fun), []), [NumLit(1.0), NumLit(2.0)])), VarDecl(Id(c), BoolType, None, ArrayCell(CallExpr(Id(fun), [NumLit(1.0), NumLit(2.0)]), [NumLit(1.0), NumLit(3.0)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 378))    
        
        input = """
            func main()
            begin
                if (x <= 1) return false
                if (x <= 1 )
                    return false 
                else return true
            end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], Return(BooleanLit(True)))]))])"
        self.assertTrue(TestAST.test(input, expect, 379))    
        
        
        input = """
            func main()
                begin
                     a["string",10,true] <- 1
                end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [StringLit(string), NumLit(10.0), BooleanLit(True)]), NumLit(1.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 380))     

    def test_Source_Code(self):
        input = """
            func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect ="Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(..., BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 381))   
        
        input = """
        func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end

        """
        expect ="Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), BinaryOp(+, NumLit(1.0), NumLit(1.0)), VarDecl(Id(c), None, var, NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 382))   
        
        input = """
        func helloworld()
        begin
            writeString()
        end
        func main()
        begin
            helloworld() 
        end
        """
        expect ="Program([FuncDecl(Id(helloworld), [], Block([CallStmt(Id(writeString), [])])), FuncDecl(Id(main), [], Block([CallStmt(Id(helloworld), [])]))])"
        self.assertTrue(TestAST.test(input, expect, 383))   
        
        input = """
        func checkOddEven(number n)
        begin
            if (n % 2 = 0) 
                return "Even"
            else return "Odd"
        end

        func main()
        begin
            number num <- 7
            string result <- checkOddEven(num)
            writeString(result)
        end
        """
        expect ="Program([FuncDecl(Id(checkOddEven), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)), Return(StringLit(Even))), [], Return(StringLit(Odd)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(num), NumberType, None, NumLit(7.0)), VarDecl(Id(result), StringType, None, CallExpr(Id(checkOddEven), [Id(num)])), CallStmt(Id(writeString), [Id(result)])]))])"
        self.assertTrue(TestAST.test(input, expect, 384))  
        input = """
        func compareArrays(number arr1[5], number arr2[5])
        begin
            if (length(arr1) != length(arr2)) 
                return "Arrays are not equal"

            number len <- length(arr1)
            number i <- 0

            for i until i < len by i + 1
                if (arr1[i] != arr2[i]) 
                    return "Arrays are not equal"
            return "Arrays are equal"
        end

        func main()
        begin
            number array1[5] <- [1, 2, 3, 4, 5]
            number array2[5] <- [1, 2, 3, 4, 5]

            string result <- compareArrays(array1, array2)
            writeString(result)
        end
        """
        expect ="Program([FuncDecl(Id(compareArrays), [VarDecl(Id(arr1), ArrayType([5.0], NumberType), None, None), VarDecl(Id(arr2), ArrayType([5.0], NumberType), None, None)], Block([If((BinaryOp(!=, CallExpr(Id(length), [Id(arr1)]), CallExpr(Id(length), [Id(arr2)])), Return(StringLit(Arrays are not equal))), [], None), VarDecl(Id(len), NumberType, None, CallExpr(Id(length), [Id(arr1)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<, Id(i), Id(len)), BinaryOp(+, Id(i), NumLit(1.0)), If((BinaryOp(!=, ArrayCell(Id(arr1), [Id(i)]), ArrayCell(Id(arr2), [Id(i)])), Return(StringLit(Arrays are not equal))), [], None)), Return(StringLit(Arrays are equal))])), FuncDecl(Id(main), [], Block([VarDecl(Id(array1), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(array2), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(result), StringType, None, CallExpr(Id(compareArrays), [Id(array1), Id(array2)])), CallStmt(Id(writeString), [Id(result)])]))])"
        self.assertTrue(TestAST.test(input, expect, 385))  
        input = """
            func main()
            begin
                var i <- 0
                while (i < 5)
                begin
                    print(i)
                    i <- i + 1
                end
            end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), CallStmt(Id(while), [BinaryOp(<, Id(i), NumLit(5.0))]), Block([CallStmt(Id(print), [Id(i)]), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])]))])"
        self.assertTrue(TestAST.test(input, expect, 386))  
        input = """
            func main()
            begin
                var i <- 0
                for i until i < 5 by 1
                begin
                    if (i % 2 = 0) print(i)
                end
            end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(<, Id(i), NumLit(5.0)), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(i), NumLit(2.0)), NumLit(0.0)), CallStmt(Id(print), [Id(i)])), [], None)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 387))  
        input = """
            func factorial(number n)
            begin
                if (n <= 1) return 1
                else return n * factorial(n - 1)
            end

            func main()
            begin
                var num <- 5
                var result <- factorial(num)
                print(result)
            end
        """
        expect ="Program([FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<=, Id(n), NumLit(1.0)), Return(NumLit(1.0))), [], Return(BinaryOp(*, Id(n), CallExpr(Id(factorial), [BinaryOp(-, Id(n), NumLit(1.0))]))))])), FuncDecl(Id(main), [], Block([VarDecl(Id(num), None, var, NumLit(5.0)), VarDecl(Id(result), None, var, CallExpr(Id(factorial), [Id(num)])), CallStmt(Id(print), [Id(result)])]))])"
        self.assertTrue(TestAST.test(input, expect, 388))  
        input = """
        func calculateSquare(number n)
        return n * n

        func main()
        begin
            var num <- 5
            var result <- calculateSquare(num)
            print(result)
        end
        """
        expect ="Program([FuncDecl(Id(calculateSquare), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(*, Id(n), Id(n)))), FuncDecl(Id(main), [], Block([VarDecl(Id(num), None, var, NumLit(5.0)), VarDecl(Id(result), None, var, CallExpr(Id(calculateSquare), [Id(num)])), CallStmt(Id(print), [Id(result)])]))])"
        self.assertTrue(TestAST.test(input, expect, 389))  
        input = """
        func main()
        begin
            var x <- 10
            if (x > 0) 
            begin
                print(x)
                if (x <= 5) printString("Small")
                elif (x <= 10) printString("Medium")
                else printString("Large")
            end
            else printString("Non-positive")
        end    
        """
        expect ="Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), None, var, NumLit(10.0)), If((BinaryOp(>, Id(x), NumLit(0.0)), Block([CallStmt(Id(print), [Id(x)]), If((BinaryOp(<=, Id(x), NumLit(5.0)), CallStmt(Id(printString), [StringLit(Small)])), [(BinaryOp(<=, Id(x), NumLit(10.0)), CallStmt(Id(printString), [StringLit(Medium)]))], CallStmt(Id(printString), [StringLit(Large)]))])), [], CallStmt(Id(printString), [StringLit(Non-positive)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 390))  
        input = """
        func multiplyArray(number arr[5])
        begin
            var result <- 1
            var i <- 0
            for i until i < length(arr) by 1
                result <- result * arr[i]
            return result
        end

        func main()
        begin
            number numbers[5] <- [1, 2, 3, 4, 5]
            var product <- multiplyArray(numbers)
            print(product)
        end    
        """
        expect ="Program([FuncDecl(Id(multiplyArray), [VarDecl(Id(arr), ArrayType([5.0], NumberType), None, None)], Block([VarDecl(Id(result), None, var, NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(<, Id(i), CallExpr(Id(length), [Id(arr)])), NumLit(1.0), AssignStmt(Id(result), BinaryOp(*, Id(result), ArrayCell(Id(arr), [Id(i)])))), Return(Id(result))])), FuncDecl(Id(main), [], Block([VarDecl(Id(numbers), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(product), None, var, CallExpr(Id(multiplyArray), [Id(numbers)])), CallStmt(Id(print), [Id(product)])]))])"
        self.assertTrue(TestAST.test(input, expect, 391))  
        input = """
        func isEven(number n)
        return n % 2 = 0

        func isPositive(number n)
        return n > 0

        func main()
        begin
            number num <- 8
            if (isEven(num) and isPositive(num))
                printString("Even and Positive")
            elif (not isEven(num) and isPositive(num))
                printString("Odd and Positive")
            else printString("Not Odd and Positive")
        end
        """
        expect ="Program([FuncDecl(Id(isEven), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(=, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)))), FuncDecl(Id(isPositive), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(>, Id(n), NumLit(0.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(num), NumberType, None, NumLit(8.0)), If((BinaryOp(and, CallExpr(Id(isEven), [Id(num)]), CallExpr(Id(isPositive), [Id(num)])), CallStmt(Id(printString), [StringLit(Even and Positive)])), [(BinaryOp(and, UnaryOp(not, CallExpr(Id(isEven), [Id(num)])), CallExpr(Id(isPositive), [Id(num)])), CallStmt(Id(printString), [StringLit(Odd and Positive)]))], CallStmt(Id(printString), [StringLit(Not Odd and Positive)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 392))  
        input = """
        func greet(string name, string greeting)
        return greeting + ", " + name + "!"

        func main()
        begin
            var username <- "Alice"
            var message <- greet(username, "Hello")
            printString(message)
        end
        """
        expect ="Program([FuncDecl(Id(greet), [VarDecl(Id(name), StringType, None, None), VarDecl(Id(greeting), StringType, None, None)], Return(BinaryOp(+, BinaryOp(+, BinaryOp(+, Id(greeting), StringLit(, )), Id(name)), StringLit(!)))), FuncDecl(Id(main), [], Block([VarDecl(Id(username), None, var, StringLit(Alice)), VarDecl(Id(message), None, var, CallExpr(Id(greet), [Id(username), StringLit(Hello)])), CallStmt(Id(printString), [Id(message)])]))])"
        self.assertTrue(TestAST.test(input, expect, 393))  
    def test_Some_More(self):
        # mostly copying
        input = """
            number a <- fun()[1]
        """
        expect ="Program([VarDecl(Id(a), NumberType, None, ArrayCell(CallExpr(Id(fun), []), [NumLit(1.0)]))])"
        self.assertTrue(TestAST.test(input, expect, 394))  
        input = """
            number a[1.820, 1.8203, 1.8204, 1.8205]
        """
        expect ="Program([VarDecl(Id(a), ArrayType([1.82, 1.8203, 1.8204, 1.8205], NumberType), None, None)])"
        self.assertTrue(TestAST.test(input, expect, 395))  
        input = """
            var a <- 10.2e30
        """
        expect ="Program([VarDecl(Id(a), None, var, NumLit(1.02e+31))])"
        self.assertTrue(TestAST.test(input, expect, 396))  
        input = """
            func main ()
            begin
                if (1)
                    b()
                elif (2)
                    if (3)
                        c()
                    elif (4)
                        d()
                    else e()
            end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(b), [])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(c), [])), [(NumLit(4.0), CallStmt(Id(d), []))], CallStmt(Id(e), [])))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 397))  
        input = """
            func main() begin
            if (1)
                if (2)
                    b()
                elif (3)
                    if (4)
                        c()
                    elif (5)
                        d()
                    else e()
                elif(6)
                    f()
                else g()
            elif (7) h()
            end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), CallStmt(Id(b), [])), [(NumLit(3.0), If((NumLit(4.0), CallStmt(Id(c), [])), [(NumLit(5.0), CallStmt(Id(d), []))], CallStmt(Id(e), []))), (NumLit(6.0), CallStmt(Id(f), []))], CallStmt(Id(g), []))), [(NumLit(7.0), CallStmt(Id(h), []))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 398))  
        input = """
        ## if nested with for
        func main() begin
        var i<-0 
        if (1) 
            for i until i=10 by 1
                if (2) return
                elif (3) return
                else  return
        end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), If((NumLit(1.0), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), If((NumLit(2.0), Return()), [(NumLit(3.0), Return())], Return()))), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 399))  
        input = """
        func main() 
        begin
            print("This is the end of assignment 2")
        end
        """
        expect ="Program([FuncDecl(Id(main), [], Block([CallStmt(Id(print), [StringLit(This is the end of assignment 2)])]))])"
        self.assertTrue(TestAST.test(input, expect, 400))