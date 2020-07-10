
from ply.lex import lex
reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'echo': 'ECHO'
}

tokens = [
             "VAR",
             "INT",
             "BOOL",
             "STRING",
             "LIST",
             "SET",
             "MENOS",
             "MAS",
             "PRODUCTO",
             "DIVISION",
             "LPAREN",
             "RPAREN",
             "POTENCIA",
             "MAP",
             "ID",
             "NUM",
             "COMPARA",
             "IGUAL"


         ] + list(reserved.values())

t_MENOS = r'-'
t_MAS = r'\+'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_INT = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IGUAL = r'='
t_VAR = r'[a-z]+'
t_COMPARA = r'[!<>=]='
t_IF = r'if'