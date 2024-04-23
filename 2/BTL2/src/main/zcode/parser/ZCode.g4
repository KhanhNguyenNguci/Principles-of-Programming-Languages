//2013444
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

//! SYNTAX
//! declare
program: NEWLINE* list_declared EOF;
list_declared:  (declared list_declared) | declared;
declared: function | (variables ignore);

function: FUNC ID LPARENT parameters_list? RPARENT  (ignore? return_stmt | ignore? block_stmt | ignore);

variables: implicit_var | keyword_var | implicit_dynamic;

//! implicit var, implicit dynamic, keyword var
implicit_var: VAR ID ASSIGNINIT exp;

implicit_dynamic: DYNAMIC ID (ASSIGNINIT exp)?;

keyword_var: type_prime ID (LBRACKET list_NUMBER_LIT RBRACKET)? (ASSIGNINIT exp)?; 
list_NUMBER_LIT: (NUMBER_LITERAL COMMA list_NUMBER_LIT) | NUMBER_LITERAL;

//! parameters_list
parameters_list: parameter COMMA parameters_list | parameter;
parameter: type_prime ID (LBRACKET list_NUMBER_LIT RBRACKET)?;
type_prime: NUMBER | BOOL | STRING;

//! Value
literal: NUMBER_LITERAL | STRING_LITERAL | TRUE | FALSE | array_literal;
list_expr: (exp COMMA list_expr) | exp;
array_literal: LBRACKET (list_literal) RBRACKET;
list_literal: (exp COMMA list_literal) | exp;

//! Expression
exp: exp1 CONCAT exp1 | exp1;
exp1: exp2 (EQUAL_NUMBER | EQUAL_STRING | NOT_EQUAL | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | MINUS) exp4 | exp4;
exp4: exp4 (MULTIPLY | DIVIDE | MODULO) exp5 | exp5;
exp5: (NOT) exp5 | exp6;
exp6: (MINUS) exp6 | exp7;
exp7: index_operators | exp8;
exp8: ID | literal | (LPARENT exp RPARENT) | (ID LPARENT list_expr? RPARENT);

//! Statements
list_stmts: stmt (ignore? list_stmts)?;
stmt: declaration_stmt 
			| assignment_stmt 
            | if_stmt 
			| for_stmt 
            | break_stmt 
			| continue_stmt 
            | return_stmt  
			| call_stmt 
			| block_stmt;

declaration_stmt: (implicit_var | keyword_var | implicit_dynamic) ignore;

if_stmt: IF LPARENT exp RPARENT ignore? stmt ignore? elif_stmt else_stmt;
elif_stmt: ELIF LPARENT exp RPARENT ignore? stmt ignore? elif_stmt |;
else_stmt: ELSE ignore? stmt ignore? |;

assignment_stmt: (ID | index_operators1) ASSIGNINIT exp ignore;
index_operators: (ID | call_stmt1) LBRACKET list_expr RBRACKET; //arrCell

index_operators1: ID LBRACKET list_expr RBRACKET; //arrCell

for_stmt: FOR ID UNTIL exp BY exp ignore? stmt;

break_stmt: BREAK ignore;

continue_stmt: CONTINUE ignore;

return_stmt: RETURN exp? ignore;

call_stmt: ID LPARENT list_expr? RPARENT ignore;
call_stmt1: ID LPARENT list_expr? RPARENT;

block_stmt: BEGIN ignore list_stmts? END ignore;

//! character skip
ignore: NEWLINE+;


//!==========================================
//! LEXICAL
//! KeyWord
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
AND: 'and';
OR: 'or';
NOT: 'not';

//! Operators
ADD: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
ASSIGNINIT: '<-';
EQUAL_NUMBER: '=';
EQUAL_STRING: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';
CONCAT: '...';

//! Separators
LBRACKET: '[';
RBRACKET: ']';
LPARENT: '(';
RPARENT: ')';
COMMA: ',';

//! Identifiers
ID: (LETTER | '_') (LETTER | '_' | DIGIT)*;
fragment LETTER : [A-Za-z];
fragment DIGIT : [0-9];

//! Literal
NUMBER_LITERAL: INTERGER DECIMAL? EXPONENT?;
fragment INTERGER: [0-9]+;
fragment DECIMAL: '.' [0-9]*;
fragment EXPONENT: ('e' | 'E') ('-' | '+')? [0-9]+;

STRING_LITERAL : '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | [']["])* '"' {self.text = self.text[1:-1]};

//! NEWLINE, COMMENTS, WS
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r]* -> skip; // Comments
WS : [ \t\r\f\b]+ -> skip ;  // Spaces, Tabs

//! ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | [']["])* ('\r\n' | '\n' | EOF)
	{
	if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
    	raise UncloseString(self.text[1:-2])
	elif self.text[-1] == '\n':
    	raise UncloseString(self.text[1:-1])
	else:
    	raise UncloseString(self.text[1:])
	};
ILLEGAL_ESCAPE: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | [']["])* ([\r\f\\] | '\\' ~[bfrnt'\\] | ['] ~["])
{
	raise IllegalEscape(self.text[1:])
};