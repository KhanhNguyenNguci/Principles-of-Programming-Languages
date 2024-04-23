//2013444
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

//! declare
program: ((COMMENTS NEWLINE) | NEWLINE)* list_declared EOF;
list_declared:  (declared list_declared) | declared;
declared: function | (variables ignore);

variables: implicit_var | keyword_var | implicit_dynamic;
//! implicit_var, keyword_var , implicit_dynamic
implicit_var: VAR ID ASSIGNINIT expression;

keyword_var: (NUMBER | BOOL | STRING) ID (LBRACKET list_NUMBER_LIT RBRACKET)? (ASSIGNINIT expression)?; 
list_NUMBER_LIT: (NUMBER_LITERAL COMMA list_NUMBER_LIT) | NUMBER_LITERAL;

implicit_dynamic: DYNAMIC ID (ASSIGNINIT expression)?;

function: FUNC ID LPARENT parameters_list? RPARENT  (ignore? return_statement | ignore? block_statement | ignore);
//! parameters_list
parameters_list: parameter COMMA parameters_list | parameter;
parameter: (NUMBER | BOOL | STRING) ID (LBRACKET list_NUMBER_LIT RBRACKET)?;

//! Expression
expression: expression1 CONCAT expression1 | expression1;
expression1: expression2 (EQUAL_NUMBER | EQUAL_STRING | NOT_EQUAL | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 (ADD | MINUS) expression4 | expression4;
expression4: expression4 (MULTIPLY | DIVIDE | MODULO) expression5 | expression5;
expression5: (NOT) expression5 | expression6;
expression6: (MINUS) expression6 | expression7;
expression7: index_operators | expression8;
expression8: ID | literal | (LPARENT expression RPARENT) | (ID LPARENT list_expr? RPARENT);
//! Value
literal: NUMBER_LITERAL | STRING_LITERAL | TRUE | FALSE | array_literal;
list_expr: (expression COMMA list_expr) | expression;
array_literal: LBRACKET (list_literal) RBRACKET;
list_literal: (expression COMMA list_literal) | expression;

//! Statements
list_statements: statement (ignore? list_statements)?;
statement: declaration_statement | assignment_statement 
            | if_statement | for_statement 
            | break_statement | continue_statement 
            | return_statement  | call_statement | block_statement;

declaration_statement: (implicit_var | keyword_var | implicit_dynamic) ignore;

assignment_statement: (ID | index_operators1) ASSIGNINIT expression ignore;
index_operators: (ID | call_statement1) LBRACKET list_expr RBRACKET;
index_operators1: ID LBRACKET list_expr RBRACKET;

if_statement: IF LPARENT expression RPARENT ignore? list_statements ignore? list_elif_statements? else_statement?;
list_elif_statements: (elif_statement list_elif_statements) | elif_statement;
elif_statement: ELIF LPARENT expression RPARENT ignore? list_statements ignore?;
else_statement: ELSE ignore? list_statements ignore?;

for_statement: FOR ID UNTIL expression BY expression ignore? statement;
break_statement: BREAK ignore;
continue_statement: CONTINUE ignore;

return_statement: RETURN expression? ignore;
call_statement: ID LPARENT list_expr? RPARENT ignore;
call_statement1: ID LPARENT list_expr? RPARENT;
block_statement: BEGIN ignore list_statements? END ignore;

//! kí tự bỏ qua
ignore: ((NEWLINE COMMENTS) | NEWLINE)+;


//! --------------------------  Lexical structure ----------------------- //
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

//! NEWLINE COMMENTS WS
NEWLINE: [\n]; // 
COMMENTS: '##' ~[\n\r]* -> skip; // Comments
WS : [ \t\r\f\b]+ -> skip ;  // skip spaces, tabs

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

//!  -------------------------- end Lexical structure ------------------- //