from ply.lex import lex
from ply.yacc import yacc

t_token = ...

def t_token(t):
    ...

t_ignore = ' \t\n' # ignora espaços e tabs

def t_error(t): # nos dizer qual caractere ilegal e se tem erro
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

tokens = ...

lexer = lex(debug=True) # construção do lexer

def p_REGRA(regras):
    '''
    REGRA : ...
          | ...
    '''
    regras[0] = ...

def p_error(regras):
    print("Erro de sintaxe"+ str(regras))

parser = yacc(debug=True) # construção do parser

parser.parse("...") # execução do parser